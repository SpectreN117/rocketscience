from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer

earth = Planet(planetmass=0, viewscale=0.0005)

RocketStarted = False
StartTime = None
BurnTime = 0

#Falcon heavy specs
Me = 25600
Mf = 119100
Mo = 276600
Mp = Mf + Mo
F1d = 716000
N1d = 9
Ftotal = N1d * F1d
Tburn = 180

Vmaxre = Ftotal*Tburn/Mp*log((Me+Mp) / Me)
print(Vmaxre)

def GetThrust ():
    global BurnTime
    global RocketStarted
    if RocketStarted:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= Tburn:
            RocketStarted = False
            return 0
        else:
            return Ftotal
    else:
        return 0
        
def StartRocket ():
    global RocketStarted
    global StartTime
    if not RocketStarted:
        RocketStarted = True
        StartTime = rocket.shiptime
        
def GetMass ():
    global RocketStarted
    if RocketStarted:
        return Me + Mp * (Tburn - BurnTime)/Tburn
    else:
        return Me + Mp
        
start = InputButton ((10, 400), "START", StartRocket, positioning = "physical", size=15)

rocket = Rocket(earth, thrust=GetThrust, mass=GetMass, heading=radians(90))
earth.run(rocket)