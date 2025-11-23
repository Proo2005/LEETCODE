import os
import shutil

source = "hard"      # source folder
destination = "sql/hard"    # destination folder

# create destination folder if it does not exist
os.makedirs(destination, exist_ok=True)

# loop through all files in source
for file in os.listdir(source):
    if file.endswith(".sql"):
        src_path = os.path.join(source, file)
        dst_path = os.path.join(destination, file)
        
        # move the file
        shutil.move(src_path, dst_path)
        print(f"Moved: {file}")

print("Transfer complete!")
