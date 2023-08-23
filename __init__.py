from .focus_refiner_switcher import FocusRefinerSwitcher
from modules.core import StableDiffusionModel
from modules.samplers_advanced import KSamplerWithRefiner

__all__ = ['FocusRefinerSwitcher']


NODE_CLASS_MAPPINGS = {
    "FocusRefinerSwitcher": FocusRefinerSwitcher,
    "StableDiffusionModel": StableDiffusionModel,
    "KSamplerWithRefiner": KSamplerWithRefiner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FocusRefinerSwitcher": "Focus Refiner Switcher",
}
