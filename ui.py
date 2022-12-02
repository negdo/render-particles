import bpy
from bpy.props import FloatProperty, BoolProperty
from bpy.types import PropertyGroup

class particlesPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Insert Particles"
    bl_idname = "SCENE_PT_layout_particles1"
    bl_category = "Particles"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("particles.insert_particles")


class particlesManipulation(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Manipulate Particles"
    bl_idname = "SCENE_PT_layout_particles2"
    bl_category = "Particles"

    def draw(self, context):
        if bpy.data.objects["Dust"] is not None:
            layout = self.layout
            col = layout.column()
            col.operator("particles.insert_particles")

            properties = context.scene.particle_properties
            col.prop(properties, "particle_size")
            #col.prop(bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_12"], "my_enum_prop")
        

class ParticleProperties(PropertyGroup):

    particle_scale: FloatProperty(
        name="Particle Size",
        description="Scale of particles in geo nodes",
        default = 0.1,
        min = 0.0,
        max = 100.0,
        )



    

        