from PIL import Image
import os

def scale_and_overlay_images(input_folder, ramka_folk_folder, ramka_volk_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    input_images = sorted(os.listdir(input_folder))
    ramka_folk_images = sorted(os.listdir(ramka_folk_folder))[:3]
    ramka_volk_images = sorted(os.listdir(ramka_volk_folder))[:3]

    def resize_and_crop(image, size):
        image_width, image_height = image.size
        target_width, target_height = size

        scale = max(target_width / image_width, target_height / image_height)
        new_width = int(image_width * scale)
        new_height = int(image_height * scale)

        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        return image.crop((left, top, right, bottom))

    for i in range(3):
        input_image_file = input_images[i]
        input_image = Image.open(os.path.join(input_folder, input_image_file)).convert('RGB')
        input_image = resize_and_crop(input_image, (1000, 1000))

        ramka_folk_image_file = ramka_folk_images[i]
        ramka_folk_image = Image.open(os.path.join(ramka_folk_folder, ramka_folk_image_file)).convert('RGBA')
        ramka_folk_image = ramka_folk_image.resize((1000, 1000), Image.Resampling.LANCZOS)
        combined_image = Image.alpha_composite(input_image.convert('RGBA'), ramka_folk_image)
        combined_image = combined_image.convert('RGB')
        combined_image.save(os.path.join(output_folder, f'{i+1}_folk.jpg'))

        ramka_volk_image_file = ramka_volk_images[i]
        ramka_volk_image = Image.open(os.path.join(ramka_volk_folder, ramka_volk_image_file)).convert('RGBA')
        ramka_volk_image = ramka_volk_image.resize((1000, 1000), Image.Resampling.LANCZOS)
        combined_image = Image.alpha_composite(input_image.convert('RGBA'), ramka_volk_image)
        combined_image = combined_image.convert('RGB')
        combined_image.save(os.path.join(output_folder, f'{i+4}_volk.jpg'))


