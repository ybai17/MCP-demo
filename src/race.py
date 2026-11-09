class Race:
    def __init__(self, name: str, distance: int, distance_type: str, track_type: str):
        self.name = name
        self.distance = distance
        self.distance_type = distance_type
        self.track_type = track_type

    def to_dict(self):
        return {
            "name": self.name,
            "distance": self.distance,
            "distance_type": self.distance_type,
            "track_type": self.track_type
        }