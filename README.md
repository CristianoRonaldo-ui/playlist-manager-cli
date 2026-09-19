# Playlist Manager CLI

A command-line playlist manager built with Python, demonstrating **object composition** (a `Playlist` *has-a* list of `Song` objects), JSON file persistence, and a full `pytest` test suite.

## Features

- Add songs to a playlist (title, artist, duration)
- List all songs in a playlist with total duration
- Remove a song by title
- Persist the playlist to a local JSON file between runs
- Look up songs by artist

## Project Structure 
```
playlist-manager-cli/
├── src/
│ ├── song.py # Song class (single music track)
│ ├── playlist.py # Playlist class (composition: has-a list of Song)
│ ├── storage.py # Save/load a Playlist to/from JSON
│ └── cli.py # Command-line interface (argparse)
├── tests/
│ ├── test_playlist.py
│ └── test_storage.py
├── requirements.txt
└── pytest.ini
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run commands from the project root using Python's module flag (`-m`), since the source files use absolute imports (`src.song`, `src.playlist`):

```bash
python3 -m src.cli add "Blinding Lights" "The Weeknd" 200
python3 -m src.cli add "Levitating" "Dua Lipa" 203
python3 -m src.cli list
python3 -m src.cli remove "Levitating"
```

## Example
```
$ python3 -m src.cli add "Blinding Lights" "The Weeknd" 200
Added: Blinding Lights by The Weeknd

$ python3 -m src.cli list
Playlist: My Playlist

Blinding Lights by The Weeknd (3:20)

$ python3 -m src.cli remove "Blinding Lights"
Removed: Blinding Lights
```

## Running Tests

```bash
pytest
```

## Complexity Analysis

| Operation | Time Complexity | Notes |
|---|---|---|
| `add_song` | O(1) | Python list `.append()` is amortized constant time |
| `remove_song` | O(n) | Must scan the list to find a matching title |
| `total_duration` | O(n) | Sums every song's duration |
| `find_by_artist` | O(n) | Scans every song, builds a new list of matches |

## What I Learned

- **Composition (has-a):** `Playlist` doesn't inherit from `Song` — it *contains* a list of `Song` objects and delegates work to them (`song.duration_sec`, `song.artist`). This mirrors the same pattern I learned in Java (`Library` has-a `Book[]`), but Python's dynamic `list` removes the need for manual capacity tracking that a fixed-size Java array requires.
- **Parameter name vs. attribute name are independent:** I hit a real bug where `self.duration = duration_sec` stored the value under `self.duration` instead of `self.duration_sec`, even though the constructor parameter was named `duration_sec`. The name on the left of `self.X =` is entirely separate from the name of the incoming parameter — they only look related because I chose similar names.
- **Manual JSON serialization:** the `json` module only understands basic types (dict, list, str, int...), so saving custom objects like `Song` requires manually converting them to/from plain dictionaries — there's no automatic way to `json.dump()` an arbitrary object.
- **`tmp_path` pytest fixture:** lets file I/O tests run against a real, isolated temporary directory instead of writing into the actual project folder, so tests never pollute each other or the repo
