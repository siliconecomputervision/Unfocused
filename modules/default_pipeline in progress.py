import modules.core as core
import os
import torch

from modules.path import modelfile_path, lorafile_path


@torch.no_grad()
def process(positive_prompt, negative_prompt, Base_Model, Refiner_Model, Lora_Model, vae, steps, switch, width, height, image_seed, latent):

    xl_base_filename = os.path.join(modelfile_path, 'nightvisionXLPhotorealisticPortrait_alpha0650Bakedvae.safetensors')
    xl_refiner_filename = os.path.join(modelfile_path, 'sd_xl_refiner_1.0.safetensors')
    xl_base_offset_lora_filename = os.path.join(lorafile_path, 'sd_xl_offset_example-lora_1.0.safetensors')
    xl_base = core.load_model(xl_base_filename)
    xl_base = core.load_lora(xl_base, xl_base_offset_lora_filename, strength_model=0.5, strength_clip=0.0)
    del xl_base.vae
    xl_refiner = core.load_model(xl_refiner_filename)
    positive_conditions = core.encode_prompt_condition(clip=xl_base.clip, prompt=positive_prompt)
    negative_conditions = core.encode_prompt_condition(clip=xl_base.clip, prompt=negative_prompt)

    positive_conditions_refiner = core.encode_prompt_condition(clip=xl_refiner.clip, prompt=positive_prompt)
    negative_conditions_refiner = core.encode_prompt_condition(clip=xl_refiner.clip, prompt=negative_prompt)

    empty_latent = latent

    sampled_latent = core.ksampler_with_refiner(
        model=xl_base.unet,
        positive=positive_conditions,
        negative=negative_conditions,
        refiner=xl_refiner.unet,
        refiner_positive=positive_conditions_refiner,
        refiner_negative=negative_conditions_refiner,
        refiner_switch_step=switch,
        latent=empty_latent,
        steps=steps, start_step=0, last_step=steps, disable_noise=False, force_full_denoise=True,
        seed=image_seed,
    )

    return sampled_latent