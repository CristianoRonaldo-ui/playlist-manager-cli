import json

from src.song import Song
from src.playlist import Playlist


def save_playlist(playlist: Playlist, filepath: str) -> None:
    data = {
        "name": playlist.name,
        "songs": [
            {"title": song.title, "artist": song.artist, "duration_sec": song.duration_sec}
            for song in playlist.songs
        ],
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def load_playlist(filepath: str) -> Playlist:
    with open(filepath, "r") as f:
        data = json.load(f)

    playlist = Playlist(data["name"])
    for song_data in data["songs"]:
        playlist.add_song(Song(song_data["title"], song_data["artist"], song_data["duration_sec"]))

    return playlist 