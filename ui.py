import bpy

class particlesPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Particles"
    bl_idname = "SCENE_PT_layout_simple_tools"
    bl_category = "Particles1"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("particles.insert_particles")