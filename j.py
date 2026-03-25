import os
import shutil

source = "hard"     
destination = "sql/hard"   

os.makedirs(destination, exist_ok=True)

for file in os.listdir(source):
    if file.endswith(".sql"):
        src_path = os.path.join(source, file)
        dst_path = os.path.join(destination, file)

        shutil.move(src_path, dst_path)
        print(f"Moved: {file}")
print("All .sql files have been moved successfully hurrah.")
