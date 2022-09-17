# import required module
from PIL import Image
import os

images_dir='../images'

for filename in os.listdir(images_dir):
    path = os.path.join(images_dir, filename)
    if filename.startswith('.'):
        print(f"[ⓧ] Ignoring: {filename} at {path}")
        continue
    if not filename.startswith('`'):
        print(f"[*] Calculating image size for {filename.split('.')[0]} at {path[2:]}")
        img = Image.open(path)
        width = img.width
        height = img.height
        print(f'\t[-] Width = {width}')
        print(f'\t[-] Height = {height}')
        new_name = images_dir + f"/`{filename.split('.')[0]} - {width}x{height}.{filename.split('.')[1]}"
        os.rename(path, new_name)
        print(f"[✅] Renamed {filename.split('.')[0]} successfully")
    else:
        print(f"[ⓧ] Ignoring already processed file: {filename} at {path}")