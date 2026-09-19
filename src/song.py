class Song:
    def __init__(self, title, artist, duration_sec):
        self.title = title
        self.artist = artist
        self.duration_sec = duration_sec

    def __str__(self) -> str:
        minutes = self.duration_sec // 60
        seconds = self.duration_sec % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"