# Imports
try:
    from g4f.client import Client
except ImportError:
    input("Install g4f you goofy")
    import sys
    sys.exit()

import base64
from datetime import datetime


# Json to Image Conversion
def save_png(data, output_path):
    # Save binary data to a PNG file
    with open(output_path, "wb") as f:
        f.write(data)
    print(f"Image saved at {output_path}")


# Image Generation
def image_from_prompt(prompt):
    client = Client()
    response = client.images.generate(
        model="flux-pro",
        prompt=prompt,
        response_format="b64_json"
    )
    data = response.data[0].b64_json
    return base64.b64decode(data)


def image_from_prompt(prompt, model):
    client = Client()
    response = client.images.generate(
        model=model,
        prompt=prompt,
        response_format="b64_json"
    )
    data = response.data[0].b64_json
    return base64.b64decode(data)


def image_from_reference(reference_path):
    client = Client()
    response = client.images.create_variation(
        image=open(reference_path, "rb"),
        model="flux",
        response_format="b64_json"
    )
    data = response.data[0].b64_json
    return base64.b64decode(data)


# Main
def main():
    prompt = input("Provide a prompt: ")

    current_folder = ""
    current_time = datetime.now().strftime("%d-%m-%y_%H-%M-%S")

    # All available models: sdxl-turbo, flux, flux-pro, flux-dev, flux-shcnell, dall-e-3, midjourney
    models = ["sdxl-turbo", "flux", "flux-pro", "flux-dev", "flux-shcnell", "dall-e-3", "midjourney"]

    for model in models:
        print(f"Generating image with {model}...")
        prompt_name = "-".join(prompt.split()[:3]) if len(prompt.split()) > 2 else prompt.strip().replace(" ", "-")
        file_name = f"{prompt_name}_{model}_{current_time}"

        json_image = image_from_prompt(prompt, model)

        save_png(json_image, f"{current_folder}/{file_name}.png")
    input("\nGeneration complete. Press any key to exit.")


if __name__ == "__main__":
    main()
