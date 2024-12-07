
import settings
class Simulation():
    def __init__(self, id):
        self.id = id
        self.time = 0
        self.cost = settings.INVESTMENT_COSTS
        self.mooseFound = 0

    def show_results(self):
        print("- - > SIMULAATIO " + str(self.id) + " < - -")
        realTime = settings.time_to_hour(self.time)
        print("AIKA: " + str(realTime[0]) + "h " + str(realTime[1]) + "m")
        print("KALUSTEHINTA: " + str(self.cost))
        self.cost += realTime[0]*settings.DRONE_HOURLY_COST + realTime[1]/60*settings.DRONE_HOURLY_COST
        print("HINTA YHTEENSÄ: " + str(self.cost))
        print("HIRVIÄ LÖYDETTY: " + str(self.mooseFound) + "/" + str(settings.MOOSE_AMOUNT))
        virhe = settings.MOOSE_AMOUNT - self.mooseFound
        print("VIRHE: " + str(virhe))
        print("SUHTEELLINEN VIRHE: " + str(virhe/settings.MOOSE_AMOUNT * 100) + "%")

