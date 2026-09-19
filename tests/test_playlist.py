from src.playlist import Playlist
from src.song import Song


def test_add_song_increases_count():
    playlist = Playlist("Chill Vibes")
    playlist.add_song(Song("Blinding Lights", "The Weeknd", 200))
    assert len(playlist.songs) == 1


def test_total_duration_sums_all_songs():
    playlist = Playlist("Chill Vibes")
    playlist.add_song(Song("Blinding Lights", "The Weeknd", 200))
    playlist.add_song(Song("Levitating", "Dua Lipa", 203))
    assert playlist.total_duration() == 403


def test_remove_song_returns_true_when_found():
    playlist = Playlist("Chill Vibes")
    playlist.add_song(Song("Blinding Lights", "The Weeknd", 200))
    result = playlist.remove_song("Blinding Lights")
    assert result is True
    assert len(playlist.songs) == 0


def test_remove_song_returns_false_when_not_found():
    playlist = Playlist("Chill Vibes")
    result = playlist.remove_song("Nonexistent")
    assert result is False


def test_find_by_artist_filters_correctly():
    playlist = Playlist("Chill Vibes")
    playlist.add_song(Song("Blinding Lights", "The Weeknd", 200))
    playlist.add_song(Song("Levitating", "Dua Lipa", 203))
    results = playlist.find_by_artist("The Weeknd")
    assert len(results) == 1
    assert results[0].title == "Blinding Lights" 
    