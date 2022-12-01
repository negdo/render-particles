
import bpy
from bpy.utils import resource_path
from pathlib import Path

class insertParticles(bpy.types.Operator):
    bl_idname = "particles.insert_particles"
    bl_label = "Insert Particles"
    bl_description = "Insert particles"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # create new collection
        bpy.ops.collection.create(name="Render Particles")
        bpy.context.scene.collection.children.link(bpy.data.collections["Render Particles"])

        # select collection
        bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["Render Particles"]

        # append particles object from file
        self.append(context)

        # get camera position
        camera = bpy.context.scene.camera
        camera_location = camera.location
        camera_rotation = camera.rotation_euler
        camera_focus = camera.data.dof.focus_distance

        # get particles object
        selected_objs = bpy.context.selected_objects
        particles_obj = None

        # find particles object, it starts with Dust
        for obj in selected_objs:
            if obj.name.startswith("Dust"):
                particles_obj = obj
                break

        if particles_obj is None:
            self.report({'ERROR'}, "Can not find particles object")
            return {'CANCELLED'}
        
        # set particles object location to camera location
        particles_obj.location = camera.location
        
            

        return {'FINISHED'}


    def append(self, context):
        #append node group
        USER = Path(resource_path('USER'))
        src = USER / "scripts/addons/render-particles"

        file_path = src / "particles2.blend"
        inner_path = "Object"
        object_name = "Dust"

        bpy.ops.wm.append(
            filepath=str(file_path / inner_path / object_name),
            directory=str(file_path / inner_path),
            filename=object_name
        )


