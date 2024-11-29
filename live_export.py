import bpy
import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

bl_info = {
    "name": "Live Export for Browser with Environment Texture and Applied Modifiers",
    "blender": (3, 0, 0),
    "category": "Import-Export",
    "description": "Live export Blender scene to browser on Ctrl+S with environment texture and applied modifiers.",
}

EXPORT_FILE_NAME = "blender_live_scene.glb"
EXPORT_FILE_PATH = os.path.join(os.getcwd(), EXPORT_FILE_NAME)  # Ensure export path is in the current working directory
ENV_TEXTURE_PATH = os.path.join(os.getcwd(), "environment_texture.jpg")
HTTP_SERVER_PORT = 8000


class LiveExportOperator(bpy.types.Operator):
    """Toggle live export for browser"""
    bl_idname = "wm.live_export_toggle"
    bl_label = "Toggle Live Export"

    # Static class variables to store server and thread
    is_running = False
    server_thread = None
    server_instance = None

    def execute(self, context):
        if not LiveExportOperator.is_running:
            self.start_live_export()
            self.report({'INFO'}, "Live export enabled. Exporting on Ctrl+S.")
        else:
            self.stop_live_export()
            self.report({'INFO'}, "Live export disabled.")
        return {'FINISHED'}

    def start_live_export(self):
        bpy.app.handlers.save_post.append(self.save_handler)
        self.start_server()
        LiveExportOperator.is_running = True

    def stop_live_export(self):
        if self.save_handler in bpy.app.handlers.save_post:
            bpy.app.handlers.save_post.remove(self.save_handler)
        self.stop_server()
        LiveExportOperator.is_running = False

    @staticmethod
    def save_handler(scene):
        try:
            # Export environment texture
            export_environment_texture()

            # Export GLTF file with modifiers applied
            bpy.ops.export_scene.gltf(
                filepath=EXPORT_FILE_PATH,
                export_format='GLB',
                export_apply=True  # Apply all modifiers during export
            )
            print(f"Scene exported to {EXPORT_FILE_PATH}")
        except Exception as e:
            print(f"Failed to export scene: {e}")

    @classmethod
    def start_server(cls):
        def serve():
            with HTTPServer(("", HTTP_SERVER_PORT), SimpleHTTPRequestHandler) as httpd:
                cls.server_instance = httpd
                print(f"Serving at http://localhost:{HTTP_SERVER_PORT}")
                httpd.serve_forever()

        cls.server_thread = threading.Thread(target=serve, daemon=True)
        cls.server_thread.start()

    @classmethod
    def stop_server(cls):
        if cls.server_instance:
            cls.server_instance.shutdown()
            cls.server_instance.server_close()
            cls.server_instance = None
            print("HTTP server stopped.")
        cls.server_thread = None


class LiveExportPanel(bpy.types.Panel):
    """Creates a panel in the scene context of the properties editor"""
    bl_label = "Live Export to Browser"
    bl_idname = "SCENE_PT_live_export"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.live_export_toggle", text="Toggle Live Export")


def export_environment_texture():
    """Export the environment texture as a separate file."""
    world = bpy.context.scene.world
    if world and world.node_tree:
        nodes = world.node_tree.nodes
        env_node = nodes.get("Environment Texture")
        if env_node and env_node.image:
            try:
                env_node.image.save_render(filepath=ENV_TEXTURE_PATH)
                print(f"Environment texture exported to {ENV_TEXTURE_PATH}")
            except Exception as e:
                print(f"Failed to export environment texture: {e}")


def register():
    bpy.utils.register_class(LiveExportOperator)
    bpy.utils.register_class(LiveExportPanel)


def unregister():
    bpy.utils.unregister_class(LiveExportOperator)
    bpy.utils.unregister_class(LiveExportPanel)


if __name__ == "__main__":
    register()
