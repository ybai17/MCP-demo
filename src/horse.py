class Horse:
    """
    Represents a horse with its name, color, year of birth, and aptitudes for different distances and track types.
    """
    def __init__(self, name: str, color: str, year: int, distance_aptitudes: dict, track_aptitudes: dict):
        """
        Initializes a Horse instance.

        Args:
            name (str): The name of the horse.
            color (str): The color of the horse.
            year (int): A year in which the horse was active.
            distance_aptitudes (dict): The horse's aptitudes (A = high, G = low) for different distances (sprint, mile, medium, long).
            track_aptitudes (dict): The horse's aptitudes (A = high, G = low) for different track types (turf, dirt).
        """
        self.name = name
        self.color = color
        self.year = year
        self.distance_aptitudes = distance_aptitudes
        self.track_aptitudes = track_aptitudes

    def speak(self):
        return f"{self.name} says neigh!"

    def to_dict(self):
        """
        Converts the Horse instance into a dictionary.

        Returns:
            dict: A dictionary representation of the Horse instance.
        """
        return {
            "name": self.name,
            "color": self.color,
            "year": self.year,
            "distance_aptitudes": self.distance_aptitudes,
            "track_aptitudes": self.track_aptitudes
        }

SYMBOLI_RUDOLF = Horse("Symboli Rudolf", "Brown", 1989, {"sprint": 'E', "mile": 'C', "medium": 'A', "long": 'A'}, {"turf": 'A', "dirt": 'G'})
GOLD_SHIP = Horse("Gold Ship", "Gray", 2017, {"sprint": 'G', "mile": 'C', "medium": 'A', "long": 'A'}, {"turf": 'A', "dirt": 'G'})
KITASAN_BLACK = Horse("Kitasan Black", "Black", 2016, {"sprint": 'F', "mile": 'D', "medium": 'A', "long": 'A'}, {"turf": 'A', "dirt": 'G'})
