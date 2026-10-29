import os, shutil

path = r"C:\Users\shree\Desktop\basic programs"
for file in os.listdir(path):
    src = os.path.join(path, file)
    if os.path.isfile(src):
        ext = file.split(".")[-1].upper() if "." in file else "Others"
        folder = os.path.join(path, ext)
        os.makedirs(folder, exist_ok=True)
        shutil.move(src, os.path.join(folder, file))

print("Files organized successfully!")