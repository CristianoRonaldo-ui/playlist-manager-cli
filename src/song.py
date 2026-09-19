class Song:
    def __init__(self, title, artist, duration_sec):
        self.title = title
        self.artist = artist
        self.duration = duration_sec

    def __str__(self) -> str:
        minutes = self.duration // 60
        seconds = self.duration % 60 
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    

