import bpy
import bmesh

myvertexlist = [[2,2,2],[4,4,4],[6,6,6],[8,8,8]]

# Get the active mesh
me = bpy.context.object.data

# Get a BMesh representation
bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(me)   # fill it in from a Mesh

# Modify the BMesh, can do anything here...
for newvert in myvertexlist:
    bm.verts.new(newvert)

# also add bm.edges and bm.faces

# Finish up, write the bmesh back to the mesh
#bm.to_mesh(me)
bm.free()  # free and prevent further access
# This example assumes we have a mesh object in edit-mode
bmesh.update_edit_mesh(me, True)
