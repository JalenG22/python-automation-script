#cleanup_files.py#

import os 
import shutil

folder_path = "files"

for file in os.listdir(folder_path):
  if os.path.isfile(os.path.join(folder_path, file)):
    ext = file.split('.')[-1]
    ext_folder = os.path.join(folder_path, ext)

    if not os.path.exists(ext_folder): os.makedirs(ext_folder)
      os.makedirs(ext_folder)

      shutil.move(
              os.path.join(folder_path, file),
              os.path.join(ext_folder, file)
      )

print("Files organized by extension.")

