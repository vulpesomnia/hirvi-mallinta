import math
import settings
class Simulation():
    def __init__(self, id):
        self.id = id
        self.time = 0
        self.cost = settings.INVESTMENT_COSTS
        self.mooseFound = 0

    def show_results(self):
        print("- - > SIMULAATIO " + str(self.id) + " < - -")
        timeHours = math.floor(self.time /3600)
        timeMinutes =  (self.time/3600 - timeHours) * 60
        print("AIKA: " + str(timeHours) + "h " + str(round(timeMinutes, 2)) + "m")
        print("KALUSTEHINTA: " + str(self.cost))
        self.cost += timeHours*settings.DRONE_HOURLY_COST + timeMinutes/60*settings.DRONE_HOURLY_COST
        print("HINTA YHTEENSÄ: " + str(self.cost))
        print("HIRVIÄ LÖYDETTY: " + str(self.mooseFound) + "/" + str(settings.MOOSE_AMOUNT))
        virhe = settings.MOOSE_AMOUNT - self.mooseFound
        print("VIRHE: " + str(virhe))
        print("SUHTEELLINEN VIRHE: " + str(virhe/settings.MOOSE_AMOUNT * 100) + "%")
        return (self.time, self.cost, self.mooseFound, virhe)

