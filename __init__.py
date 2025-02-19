from .util_nodes import LoadVideo,PreViewVideo
from .studio_nodes import DiffTextNode,DiffutoonNode,SDPathLoader,ControlNetPathLoader,ExVideoNode
WEB_DIRECTORY = "./web"
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "LoadVideo": LoadVideo,
    "PreViewVideo": PreViewVideo,
    "SDPathLoader": SDPathLoader,
    "DiffTextNode": DiffTextNode,
    "DiffutoonNode": DiffutoonNode,
    "ControlNetPathLoader": ControlNetPathLoader,
    "ExVideoNode": ExVideoNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadVideo": "LoadVideo",
    "PreViewVideo": "PreViewVideo",
    "SDPathLoader": "SDPathLoader",
    "DiffTextNode": "DiffTextNode",
    "DiffutoonNode": "DiffutoonNode",
    "ControlNetPathLoader": "ControlNetPathLoader",
    "ExVideoNode": "ExVideoNode"
}