# Unfocused
This is a port of Fooocus by illyasviel intended to allow the user to take advantage of his developments directly in the ComfyUI.
For this current version you are required to MANUALLY change the base checkpoint name that you are connecting to the FocusRefinerSwitcher node.
You MUST change the SDXL checkpoint name to the checkpoint you are using on line 11 of default_pipeline.py
I am currently using NightVisionXL so that is what it is set to currently:     

xl_base_filename = os.path.join(modelfile_path, 'nightvisionXLPhotorealisticPortrait_alpha0650Bakedvae.safetensors')

You may adjust the sampler, scheduler and config inside of the ksampler function in Core.py on line 72.

def ksampler(model, positive, negative, latent, seed=None, steps=30, cfg=12.0, sampler_name='dpmpp_2m_sde_gpu',
             scheduler='karras', denoise=1.0, disable_noise=False, start_step=None, last_step=None,
             force_full_denoise=False):
