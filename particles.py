
import bpy
from bpy.utils import resource_path
from pathlib import Path
from mathutils import Vector

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

        # set location between camera and focus point
        self.set_location(context, particles_obj)
        return {'FINISHED'}

    def set_location(self, context, particles_obj):
        try:
            # get camera
            camera = context.scene.camera

            # get focus distance
            focus_distance = context.scene.camera.data.dof.focus_distance
            if camera.data.dof.focus_object != None:
                focus_distance = (camera.data.dof.focus_object.location - camera.location).length

            # calculate camera focus point location
            focus_point = camera.location + focus_distance * camera.rotation_euler.to_matrix().to_4x4() @ Vector((0, 0, -1))
            
            # set particles object location middle between camera and focus point
            particles_obj.location = (camera.location + focus_point) / 2

            # calculate width at focus point at fov
            width = focus_distance * camera.data.sensor_width / camera.data.lens * 0.5
            length = focus_distance * 0.5

            # set particles object scale
            particles_obj.scale = (width * 1.3, width * 1.3, length)
            # apply scale
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

            # set particles object rotation
            particles_obj.rotation_euler = camera.rotation_euler
        except:
            self.report({'ERROR'}, "Can not set particles object location")

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


