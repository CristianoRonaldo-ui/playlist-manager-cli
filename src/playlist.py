from src.song import Song 

class Playlist:
    def __init__ (self, name):
        self.name = name 
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def total_duration(self) -> int:
        total = 0
        for song in self.songs:
            total += song.duration_sec
        return total 
    def find_by_artist(self, artist_name: str):
        result = []
        for song in self.songs:
            if song.artist == artist_name:
                result.append(song)
        return result 

    def remove_song(self, title: str) -> bool:
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                return True 
        return False
        