from src.playlist import Playlist
from src.song import Song
from src.storage import save_playlist, load_playlist


def test_save_and_load_playlist_roundtrip(tmp_path):
    filepath = tmp_path / "playlist.json"

    playlist = Playlist("Chill Vibes")
    playlist.add_song(Song("Blinding Lights", "The Weeknd", 200))
    playlist.add_song(Song("Levitating", "Dua Lipa", 203))

    save_playlist(playlist, str(filepath))
    loaded = load_playlist(str(filepath))

    assert loaded.name == "Chill Vibes"
    assert loaded.total_duration() == 403
    assert len(loaded.songs) == 2


def test_load_playlist_preserves_song_order(tmp_path):
    filepath = tmp_path / "playlist.json"

    playlist = Playlist("Chill Vibes")
    playlist.add_song(Song("First", "Artist A", 100))
    playlist.add_song(Song("Second", "Artist B", 150))

    save_playlist(playlist, str(filepath))
    loaded = load_playlist(str(filepath))

    assert loaded.songs[0].title == "First"
    assert loaded.songs[1].title == "Second" 