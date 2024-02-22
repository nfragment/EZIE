import json
import os
from collections import defaultdict
from zipfile import ZipFile, ZIP_STORED

RAW_DIR = './raw' # use this for linux
# RAW_DIR = '.\\raw' # use this for windows
packages = defaultdict(list)

print ("starting stage")

for board_dir, _, files in os.walk(RAW_DIR):
    print ("entered for loop")
    if files := [f for f in files if not f.startswith('.')]:
        print ("executing if block")
        a, _, arch, board = board_dir.split('/') # use this for linux
        # a, _, arch, board = board_dir.split('\\') # use this for windows
        os.makedirs(arch, exist_ok=True)
        print(f"Compressing {board} for {arch}")

        zipfile_name = os.path.join(arch, f"{board}.autoconf")
        with ZipFile(zipfile_name, mode="w", compression=ZIP_STORED, allowZip64=False, compresslevel=None,
                     strict_timestamps=True) as myzip:
            for file in files:
                filepath = os.path.join(board_dir, file)
                myzip.write(filepath, file)
        packages[arch].append(board)

print ("intermediate stage")
for arch, packages_list in packages.items():
    with open(f"{arch}_manifest.json", "w") as manifest:
        json.dump({"files": sorted(packages_list, key=str.casefold)}, manifest, indent=None, separators=(",", ":"))

print ("final stage")