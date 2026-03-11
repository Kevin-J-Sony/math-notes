
import subprocess
import os
import glob
import shutil

src_dir_list = ["Z:/books-to-read/alg-top", "Z:/books-to-read/diff-geo"]
out_dir_list = ["./algebraic_topology", "./differential_geometry"]

assert(len(src_dir_list) == len(out_dir_list))

for i in range(len(src_dir_list)):
    for file in glob.glob(os.path.join(src_dir_list[i], "*.tex")):
        shutil.copy(file, out_dir_list[i])
        print(type(file))