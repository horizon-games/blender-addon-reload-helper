bl_info = {
    "name": "Addon Reload Helper",
    "author": "Tomasz Dysinski",
    "version": (1, 0, 1),
    "blender": (2, 91, 0),
    "location": "Properties > Scene > Addon Reload Helper",
    "description": "Help reload addons with an operator, some UI, and a hotkey (OSKey + Shift + R)",
    "warning": "",
    "doc_url": "",
    "category": "System",
}


import bpy
from bpy.types import Operator


class AddonReloadHelperUI(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Addon Reload Helper"
    bl_idname = "horizon.addon_reload_helper"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        row = layout.row()
        row.scale_y = 2.0
        row.operator("addon_reload_helper.reload")



class ReloadAddons(Operator):
    """Reload Addons"""
    bl_idname = "addon_reload_helper.reload"
    bl_label = "Reload Addons"
    bl_options = {'REGISTER'}

    def execute(self, context):
        result = bpy.ops.script.reload()
        return {'FINISHED'}

# store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_class(AddonReloadHelperUI)
    bpy.utils.register_class(ReloadAddons)

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

    kmi = km.keymap_items.new(ReloadAddons.bl_idname, 'R', 'PRESS', oskey=True, shift=True)
    # kmi.properties.total = 4

    addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(AddonReloadHelperUI)
    bpy.utils.unregister_class(ReloadAddons)

    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
