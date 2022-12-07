from bpy.props import FloatProperty, BoolProperty, FloatVectorProperty, IntProperty, PointerProperty, CollectionProperty, EnumProperty
from bpy.types import PropertyGroup
import bpy


def update_particle_collection(self, context):
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_11"] = self.particle_collection
    bpy.data.objects["Dust"].update_tag()

def update_particle_amount(self, context):
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_2"] = self.particle_amount
    bpy.data.objects["Dust"].update_tag()

def update_particle_scale(self, context):
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_12"] = self.particle_scale
    bpy.data.objects["Dust"].update_tag()

def update_wind_direction(self, context):
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_8"][0] = self.wind_direction[0]
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_8"][1] = self.wind_direction[1]
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_8"][2] = self.wind_direction[2]
    bpy.data.objects["Dust"].update_tag()

def update_particle_randomness(self, context):
    print("update_particle_randomness")
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_7"] = self.randomness
    bpy.data.objects["Dust"].update_tag()

def update_particle_velocity(self, context):
    print("update_particle_velocity")
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_5"] = self.velocity
    bpy.data.objects["Dust"].update_tag()

def update_particle_local_movement(self, context):
    print("update_particle_local_movement")
    bpy.data.objects["Dust"].modifiers["Render Particles"]["Input_6"] = self.local_movement
    bpy.data.objects["Dust"].update_tag()



class ParticleProperties(PropertyGroup):

    particle_amount: bpy.props.IntProperty(
        name="Particle Amount",
        description="Number of particles to instance",
        default=1000,
        min=0,
        update=update_particle_amount
    )

    particle_scale: FloatProperty(
        name="Particle Size",
        description="Scale of particles in geo nodes",
        default = 0.1,
        min = 0.0,
        max = 100.0,
        update = update_particle_scale
        )

    randomness: FloatProperty(
        name="Randomness",
        description="Randomness of local particle movement",
        default = 5.0,
        min = 0.0,
        max = 1000.0,
        update = update_particle_randomness
        )

    velocity: FloatProperty(
        name="Velocity",
        description="Velocity of local movement of particles",
        default = 1.0,
        min = 0.0,
        max = 1000.0,
        update = update_particle_velocity
        )

    local_movement: FloatProperty(
        name="Distance",
        description="Distance of local movement of particles",
        default = 1.0,
        min = 0.0,
        max = 1000.0,
        update = update_particle_local_movement
        )
    
    wind_direction: FloatVectorProperty(
        name="Wind Direction",
        description="Direction of wind",
        default = (0.0, 0.0, 0.0),
        update = update_wind_direction
        )

    

    

    #particle_collection: CollectionProperty(
    #    name="Particle Collection",
    #    description="Collection of particles to instance",
    #    update = update_particle_collection,
    #    type = bpy.types.Collection
    #)