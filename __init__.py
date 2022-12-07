'''
Copyright (C) 2022 Miha Marinko
miha.marinko20@gmail.com

Created by Miha Marinko

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Render Particles",
    "description": "Customizable particle presets to achieve better renders",
    "author": "Miha Marinko",
    "version": (0, 1, 0),
    "blender": (3, 3, 0),
    "location": "View3D",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
    "bl_options": {"REGISTER", "UNDO"} }

import importlib
import sys
from .particles import *
from .ui import *
from .properties import *

import bpy


classes = [ParticleProperties, ParticlesPanel, ParticlesManipulation, InsertParticles, ParticlesMovement]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.particle_properties = bpy.props.PointerProperty(type=ParticleProperties)

    print("Render Particles registered")

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    print("Render Particles unregistered")