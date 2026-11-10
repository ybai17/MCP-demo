class Race:
    """
    Represents a horse race with its name, distance (in meters), distance type, and track type.
    """
    def __init__(self, name: str, distance: int, distance_type: str, track_type: str):
        """
        Initializes a Race instance.

        Args:
            name (str): The name of the race.
            distance (int): The distance of the race in meters.
            distance_type (str): The type of distance (sprint, mile, medium, long).
            track_type (str): The type of track (turf, dirt).
        """
        self.name = name
        self.distance = distance
        self.distance_type = distance_type
        self.track_type = track_type

    def to_dict(self):
        """
        Converts the Race instance into a dictionary.

        Returns:
            dict: A dictionary representation of the Race instance.
        """
        return {
            "name": self.name,
            "distance": self.distance,
            "distance_type": self.distance_type,
            "track_type": self.track_type
        }

ARIMA_KINEN = Race("Arima Kinen", 2500, "long", "turf")
TEIO_SHO = Race("Teio Sho", 2000, "medium", "dirt")
TENNO_SHO_AUTUMN = Race("Tenno Sho (Autumn)", 2400, "medium", "turf")
