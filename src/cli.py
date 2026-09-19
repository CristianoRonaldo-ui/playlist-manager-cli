import argparse

from src.playlist import Playlist
from src.song import Song
from src.storage import save_playlist, load_playlist

DATA_FILE = "playlist_data.json"


def get_or_create_playlist():
    try:
        return load_playlist(DATA_FILE)
    except FileNotFoundError:
        return Playlist("My Playlist")


def add_command(args):
    playlist = get_or_create_playlist()
    playlist.add_song(Song(args.title, args.artist, args.duration))
    save_playlist(playlist, DATA_FILE)
    print(f"Added: {args.title} by {args.artist}")


def list_command(args):
    playlist = get_or_create_playlist()
    if not playlist.songs:
        print("Playlist is empty.")
        return
    print(f"Playlist: {playlist.name}")
    for song in playlist.songs:
        print(f"  - {song}")


def remove_command(args):
    playlist = get_or_create_playlist()
    if playlist.remove_song(args.title):
        save_playlist(playlist, DATA_FILE)
        print(f"Removed: {args.title}")
    else:
        print(f"Song not found: {args.title}")


def main():
    parser = argparse.ArgumentParser(description="Playlist Manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a song to the playlist")
    add_parser.add_argument("title")
    add_parser.add_argument("artist")
    add_parser.add_argument("duration", type=int, help="Duration in seconds")
    add_parser.set_defaults(func=add_command)

    list_parser = subparsers.add_parser("list", help="List all songs")
    list_parser.set_defaults(func=list_command)

    remove_parser = subparsers.add_parser("remove", help="Remove a song by title")
    remove_parser.add_argument("title")
    remove_parser.set_defaults(func=remove_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main() 