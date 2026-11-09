class Horse:
    def __init__(self, name: str, color: str, year: int, distance_aptitudes: dict, track_aptitudes: dict):
        self.name = name
        self.color = color
        self.year = year
        self.distance_aptitudes = distance_aptitudes
        self.track_aptitudes = track_aptitudes

    def speak(self):
        return f"{self.name} says neigh!"

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color,
            "year": self.year,
            "distance_aptitudes": self.distance_aptitudes,
            "track_aptitudes": self.track_aptitudes
        }