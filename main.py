from avacgrf import AvocadoStats
from logger import logg


ch = int(input("Задание: (0-1) "))

match ch:
    case 0:
        logg()
    case 1:
        av = AvocadoStats('avocado.csv')
        av.preprocess_data()
        av.time_series()
