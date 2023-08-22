MAX_RESOLUTION = 4096

class FocusRefinerSwitcher:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"image_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                             "steps": ("INT", {"default": 60, "min": 1, "max": 10000}),
                             "switch": ("INT", {"default": 40, "min": 1, "max": 10000}),
                             "width": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
                             "height": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
                             "p_txt": ("STRING", {"multiline": True, "default": "CLIP_G+CLIP_L"}),
                             "n_txt": ("STRING", {"multiline": True}),
                             "base_model": ("MODEL",),
                             "refiner_model": ("MODEL",),
                             "lora_model": ("MODEL",),
                             "latent": ("LATENT", ),
                             "vae": ("VAE",),
                             }}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "process"
    
    CATEGORY = "Silicone Nodes"
    
    from modules.default_pipeline import process as dp_process


    def process(self, p_txt, n_txt, base_model, refiner_model, lora_model, vae, steps, switch, width, height, image_seed, latent):
        result_latent_image = FocusRefinerSwitcher.dp_process(p_txt, n_txt, base_model, refiner_model, lora_model, vae, steps, switch, width, height, image_seed, latent)
        
        return result_latent_image
