# Experiments with random geometry
# Blender 2.8 only

import bpy
import random

#Define vertices and faces
verts = [ (x,y,z)
    for x in range(-10,10)
    for y in range(-10,10)
    for z in range(0,5)]
faces = [ tuple(random.choices(range(len(verts)), k=3))
    for s in range(0,10)]
# Define mesh and object variables
mymesh = bpy.data.meshes.new("Blob")
myobject = bpy.data.objects.new("Blob", mymesh)

#Set location and scene of object
myobject.location = bpy.context.scene.cursor.location
bpy.context.collection.objects.link(myobject)

#Create mesh
mymesh.from_pydata(verts,[],faces)
mymesh.update(calc_edges=True)
