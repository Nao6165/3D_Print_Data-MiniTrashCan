from solid import *
from solid.utils import *
import math

SHAFT_SCALE = 1

MOVE_DISTANCE = 60

def make_taper(r_work,h_work,s_work):
    shape=circle(r=r_work)
    taper=linear_extrude(height=h_work,center=True,scale=s_work)(shape)
    taper = translate((0,0,(h_work / 2)))(taper)
    return (taper)

# make bottom parts
thickness = 2
trash_can_outer_bottom_radius = 45
trash_can_inner_bottom_radius = trash_can_outer_bottom_radius - thickness
height = 100
top_scale = 1.22

trash_can_outer_parts1 = make_taper(trash_can_outer_bottom_radius,height,top_scale)

trash_can_inner_parts1 = make_taper(trash_can_inner_bottom_radius,height,top_scale)
trash_can_inner_parts1 = translate((0,0,thickness))(trash_can_inner_parts1)

trash_can_parts = (trash_can_outer_parts1 - trash_can_inner_parts1)

# make lid parts
margine = 0.4
inner_diameter_adjustment = 0.1
lid_inner_bottom_radius = ((trash_can_outer_bottom_radius * top_scale) + margine)
lid_outer_bottom_radius = (lid_inner_bottom_radius + thickness)
lid_top_scale = 0.33
lid_parts1_height = 8
lid_parts2_height = 15
lid_parts3_height = 8

lid_outer_parts1 = make_taper(lid_outer_bottom_radius, lid_parts1_height, SHAFT_SCALE)
lid_outer_parts2 = make_taper(lid_outer_bottom_radius, lid_parts2_height, lid_top_scale)
lid_outer_parts2 = translate((0,0,lid_parts1_height))(lid_outer_parts2)
lid_outer_parts3 = make_taper((lid_outer_bottom_radius*lid_top_scale), lid_parts3_height, SHAFT_SCALE)
lid_outer_parts3 = translate((0,0,(lid_parts1_height + lid_parts2_height)))(lid_outer_parts3)
lid_outer_parts = lid_outer_parts1 + lid_outer_parts2 + lid_outer_parts3

decoration_sphere_diameter= 6
for deg in range(0,360,30):
    decoration_sphere = sphere(d=decoration_sphere_diameter)
    radius = math.radians(deg)
    decoration_sphere = translate((lid_outer_bottom_radius * math.cos(radius),lid_outer_bottom_radius * math.sin(radius),lid_parts1_height / 2))(decoration_sphere)
    lid_outer_parts = lid_outer_parts + decoration_sphere

lid_inner_parts1 = make_taper(lid_inner_bottom_radius, (lid_parts1_height), SHAFT_SCALE)
lid_inner_parts2 = make_taper(lid_inner_bottom_radius, lid_parts2_height, lid_top_scale)
lid_inner_parts2 = translate((0,0,lid_parts1_height))(lid_inner_parts2)
lid_inner_parts3 = make_taper((lid_inner_bottom_radius*(lid_top_scale - inner_diameter_adjustment)), lid_parts3_height, SHAFT_SCALE)
lid_inner_parts3 = translate((0,0,(lid_parts1_height + lid_parts2_height)))(lid_inner_parts3)
lid_inner_parts = lid_inner_parts1 + lid_inner_parts2 + lid_inner_parts3
lid_inner_parts = translate((0,0,((-1)*(thickness + margine))))(lid_inner_parts)

lid_parts = lid_outer_parts - lid_inner_parts

trash_can_parts = right(MOVE_DISTANCE)(trash_can_parts)
lid_parts = left(MOVE_DISTANCE)(lid_parts)

print(scad_render(trash_can_parts))
print(scad_render(lid_parts))    
