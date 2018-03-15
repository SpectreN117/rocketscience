from ggrocket import Rocket, Planet
from math import radians, sqrt
from ggmath import Slider

earth = Planet (viewscale = 0.00005)

Re = 6.371E6
Me = 5.972E24
G = 6.674E-11

Ve=sqrt(2*Me*G/Re)

tz = Slider ((10, 400) , 0, 5, 0, positioning ="physical")

rocket = Rocket (earth, heading = radians(90), directiond = 90, velocity=Ve, timezoom = tz)
earth.run (rocket)