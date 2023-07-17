```python
from diffusers import DiffusionPipeline
import torch

#login huggingface
# from huggingface_hub import login
# login()

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-0.9", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead", fullgraph=True)
pipe.to("cuda")

# if using torch < 2.0s
# pipe.enable_xformers_memory_efficient_attention()


# Save model parameters
# checkpoint_path = "/home/tltydl2/generative-models/checkpoints/sd_xl_base_0.9.safetensors"
# pipe.save_pretrained(checkpoint_path)


prompt = "An astronaut riding a rainbow horse"

image = pipe(prompt=prompt, output_type="latent").images
    

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-refiner-0.9", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

# checkpoint_path = "/home/tltydl2/generative-models/checkpoints/sd_xl_refiner_0.9.safetensors"
# pipe.save_pretrained(checkpoint_path)


# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()
images = pipe(prompt=prompt, image=image).images


output_dir = "/home/tltydl2/generative-models/save_images/"

# Save the PIL Image to a file 
for i, image in enumerate(images):
    output_path = f"{output_dir}image_{i}.png"
    image.save(output_path)
```
