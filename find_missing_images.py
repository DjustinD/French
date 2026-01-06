import json
import os
from pathlib import Path

# Define the folders to scan
json_folders = {
    'noms': [
        'animaux.json', 'corps.json', 'famille.json', 'lieux.json',
        'maison.json', 'metiers.json', 'nature.json', 'nourriture.json',
        'objets.json', 'plantes.json', 'transports.json', 'vetements.json'
    ]
}

# Collect all image references
referenced_images = set()

for folder, files in json_folders.items():
    folder_path = Path(folder)
    for json_file in files:
        file_path = folder_path / json_file
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    if 'image' in item:
                        # Extract just the filename from the path
                        img_path = item['image']
                        img_filename = img_path.replace('images/', '')
                        referenced_images.add(img_filename)

# Get existing images
images_folder = Path('images')
existing_images = set()
if images_folder.exists():
    for img_file in images_folder.glob('*.jpg'):
        existing_images.add(img_file.name)

# Find missing images
missing_images = referenced_images - existing_images

# Check existing prompts
prompts_folder = Path('images/prompts')
existing_prompts = set()
if prompts_folder.exists():
    for prompt_file in prompts_folder.glob('*.prompt'):
        existing_prompts.add(prompt_file.name)

# Filter out images that already have prompts
missing_without_prompts = []
for img in sorted(missing_images):
    prompt_name = img.replace('.jpg', '.prompt')
    if prompt_name not in existing_prompts:
        missing_without_prompts.append(img)

print(f"Total referenced images: {len(referenced_images)}")
print(f"Total existing images: {len(existing_images)}")
print(f"Total missing images: {len(missing_images)}")
print(f"Missing images without prompts: {len(missing_without_prompts)}")
print("\nMissing images needing prompts:")
for img in missing_without_prompts:  # All images
    print(img)

# Also save to a file for prompt generation
with open('missing_images_for_prompts.txt', 'w', encoding='utf-8') as f:
    for img in missing_without_prompts:
        f.write(img + '\n')
