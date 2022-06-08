#read file
import csv
import bpy

bar_spacing = 1.5
bar_width = 75

with open ('/Users/vnair/Documents/Blender/LeasedHome_2022-6-6_0441.csv','r') as f1:
    with open ('/Users/vnair/Documents/Blender/LeasedHomeTest.csv','w') as f:
        next(f1)
        for line in f1:
            f.write(line)            
    
with open ('/Users/vnair/Documents/Blender/LeasedHomeTest.csv') as v:    
    readout = list(csv.reader(v))
    

#creating bars
for a in readout: 
    placement = readout.index(a)
    bpy.ops.mesh.primitive_plane_add(size=1)
    new_bar = bpy.context.object
    
    #setting x & y-axis
    for vert in new_bar.data.vertices:
        vert.co[1] += 0.5
        vert.co[0] += placement*bar_spacing + 0.5
    
    #bar width
    new_bar.scale = (bar_width,float(a[7]),1)
    
    #print (a[4])
