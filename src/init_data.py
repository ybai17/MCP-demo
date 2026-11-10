# create 3 Horse class instances and 3 Race class instances
# These are the data in some arbitrary, simulated database that the server application pulls data from

from horse import Horse, SYMBOLI_RUDOLF, GOLD_SHIP, KITASAN_BLACK
from race import Race, ARIMA_KINEN, TEIO_SHO, TENNO_SHO_AUTUMN

def init_horses():

    horse_list = {
        SYMBOLI_RUDOLF.name: SYMBOLI_RUDOLF.to_dict(),
        GOLD_SHIP.name: GOLD_SHIP.to_dict(),
        KITASAN_BLACK.name: KITASAN_BLACK.to_dict()
    }

    return horse_list

def init_races():

    race_list = {
        ARIMA_KINEN.name: ARIMA_KINEN.to_dict(),
        TEIO_SHO.name: TEIO_SHO.to_dict(),
        TENNO_SHO_AUTUMN.name: TENNO_SHO_AUTUMN.to_dict()
    }

    return race_list
