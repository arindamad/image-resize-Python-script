import os
from PIL import Image

# Define the input folder path containing the images
input_folder_path = r'C:\path\to\your\image_folder'

# Define the output folder path where padded images will be saved
output_folder_path = os.path.join(input_folder_path, 'padded_images')

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Define a function to resize and pad the image to 1:1 ratio with transparent padding for PNGs
def pad_image_to_square(image_path, save_path):
    img = Image.open(image_path)
    width, height = img.size

    # Determine the size of the square (max of width or height)
    max_side = max(width, height)

    # If PNG, create an RGBA image for transparency; for others, create an RGB image with white background
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        new_img = Image.new('RGBA', (max_side, max_side), (0, 0, 0, 0))  # Transparent background
    else:
        new_img = Image.new('RGB', (max_side, max_side), (255, 255, 255))  # White background for non-transparent images

    # Paste the original image into the center of the square
    paste_position = ((max_side - width) // 2, (max_side - height) // 2)
    new_img.paste(img, paste_position)

    # Save the padded image to the specified path
    new_img.save(save_path)

# Loop through all images in the folder and pad them
for filename in os.listdir(input_folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):  # Supported image formats
        image_path = os.path.join(input_folder_path, filename)
        save_path = os.path.join(output_folder_path, filename)  # Save inside 'padded_images' folder
        pad_image_to_square(image_path, save_path)
        print(f"Padded and saved: {save_path}")

print("Padding completed.")
