# create 3 instances of Horses and Races

from horse import Horse
from race import Race

def init_horses():

    horse1 = Horse("Symboli Rudolf", "Brown", 1989, {"sprint": 'E', "mile": 'C', "medium": 'A', "long": 'A'}, {"turf": 'A', "dirt": 'G'})
    horse2 = Horse("Gold Ship", "Gray", 2017, {"sprint": 'G', "mile": 'C', "medium": 'A', "long": 'A'}, {"turf": 'A', "dirt": 'G'})
    horse3 = Horse("Kitasan Black", "Black", 2016, {"sprint": 'F', "mile": 'D', "medium": 'A', "long": 'A'}, {"turf": 'A', "dirt": 'G'})

    horse_dict = {
        horse1.name: horse1.to_dict(),
        horse2.name: horse2.to_dict(),
        horse3.name: horse3.to_dict()
    }

    return horse_dict

def init_races():

    race1 = Race("Arima Kinen", 2500, "long", "turf")
    race2 = Race("Teio Sho", 2000, "medium", "dirt")
    race3 = Race("Tenno Sho (Autumn)", 2400, "medium", "turf")

    race_dict = {
        race1.name: race1.to_dict(),
        race2.name: race2.to_dict(),
        race3.name: race3.to_dict()
    }

    return race_dict
