from ggrocket import Rocket, Planet

earth = Planet (viewscale=0.00005)
rocket = Rocket (earth, altitude=400000)
earth.run (rocket)