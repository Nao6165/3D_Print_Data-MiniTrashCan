from solid import *
from solid.utils import *
shape1=circle(r = 45)
shape2=circle(r = 43)

taper1 = linear_extrude(height=100,center=True,scale=1.22)(shape1)
taper2 = linear_extrude(height=100,center=True,scale=1.22)(shape2)

taper1 = up(50)(taper1)
taper2 = up(53)(taper2)

differences = (taper1 - taper2)

print(scad_render(differences))