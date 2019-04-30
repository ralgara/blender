# Blender 2.7 only

import bpy
import math
import random

def clear_scene():
    for item in bpy.context.scene.objects:
        if item.type == 'MESH':
            bpy.context.scene.objects.unlink(item)

    for item in bpy.data.objects:
        if item.type == 'MESH':
            bpy.data.objects.remove(item)

    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

    for item in bpy.data.materials:
        bpy.data.materials.remove(item)

def euler(u, v, s, scale):
    return  scale*1/math.sqrt(2*math.pi*s*s)*math.exp(-(u*u+v*v)/(2*s*s))


def fill_vertices(numX, numY, f):
    verts = []
    for i in range (0, numX):
        for j in range(0,numY):
            # nomalize range
            u = 2*(i/numX-1/2)
            v = 2*(j/numY-1/2)
            s = variance
            x = scale*u
            y = scale*v
            #z = scale*1/math.sqrt(2*math.pi*s*s)*math.exp(-(u*u+v*v)/(2*s*s))
            z = f(u, v, s, scale)
            z = z + random.random()
            vert = (x,y,z)
            verts.append(vert)
    return verts


def fill_faces(numX, numY):
    count = 0
    faces = []
    for i in range (0, numY *(numX-1)):
        if count < numY-1:
            A = i
            B = i+1
            C = (i+numY)+1
            D = (i+numY)
            face = (A,B,C,D)
            faces.append(face)
            count = count + 1
        else:
            count = 0
    return faces

# mesh variables
numX = 100
numY = 100

# variance and sale variables
variance = .35
scale = 4
clear_scene()
verts = fill_vertices(numX, numY, euler)
faces = fill_faces(numX, numY)

# create mesh and object
mesh = bpy.data.meshes.new("wave")
object = bpy.data.objects.new("wave",mesh)

# set mesh location
object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(object)

# create mesh from python data
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)
