import bpy


class ParticlesPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Render Particles"
    bl_idname = "SCENE_PT_layout_particles"
    bl_category = "Particles"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("particles.insert_particles")


class ParticlesManipulation(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Particles"
    bl_idname = "SCENE_PT_layout_particles2"
    bl_category = "Particles"
    bl_parent_id = "SCENE_PT_layout_particles"

    def draw(self, context):
        if bpy.data.objects["Dust"] is not None:
            layout = self.layout
            col = layout.column()
            properties = context.scene.particle_properties

            #col.prop(properties, "particle_collection")
            col.prop(properties, "particle_amount")
            col.prop(properties, "particle_scale")
            
        

class ParticlesMovement(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Movement"
    bl_idname = "SCENE_PT_layout_particles3"
    bl_category = "Particles"
    bl_parent_id = "SCENE_PT_layout_particles"

    def draw(self, context):
        if bpy.data.objects.get("Dust") != None:
            layout = self.layout
            col = layout.column()
            properties = context.scene.particle_properties

            col.label(text="Local Movement")
            col.prop(properties, "local_movement")
            col.prop(properties, "randomness")
            col.prop(properties, "velocity")

            col.prop(properties, "wind_direction")





    

        