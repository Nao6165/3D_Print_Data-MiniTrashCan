from solid import *
from solid.utils import *
shape1=circle(r = 45)
shape2=circle(r = 43)

taper1 = linear_extrude(height=100,center=True,scale=1.22)(shape1)
taper2 = linear_extrude(height=100,center=True,scale=1.22)(shape2)

taper1 = up(50)(taper1)
taper2 = up(53)(taper2)

differences1 = (taper1 - taper2)

differences1 = right(120)(differences1)

shape3 = circle(r = ((45*1.22)+1.5))

shaft3 = linear_extrude(height=8)(shape3)

taper3 = linear_extrude(height=15, scale=0.33)(shape3)

taper3 = up(8)(taper3)

shape4 = circle(r=18)

shaft4 = linear_extrude(height=5)(shape4)

shaft4 = up(23)(shaft4)

futa_outer = shaft3 + taper3 + shaft4

shape5 = circle(r = (45*1.22))

shaft5 = linear_extrude(height=9)(shape5)

shaft5 = down(1)(shaft5)

taper5 = linear_extrude(height=15, scale=0.33)(shape5)

taper5 = up(8)(taper5)

shape6 = circle(r=(18-1.5))

shaft6 = linear_extrude(height=(5 - 1.5))(shape6)

shaft6 = up(23)(shaft6)

futa_inner = shaft5 + taper5 + shaft6

print(scad_render(differences1))
print(scad_render(futa_outer - futa_inner))
