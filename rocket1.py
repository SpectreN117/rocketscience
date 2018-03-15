from ggrocket import Rocket, Planet
from math import radians

earth = Planet (viewscale=0.00005)
rocket = Rocket (earth, heading = radians(90), directiond = 90, velocity=10)
earth.run (rocket)