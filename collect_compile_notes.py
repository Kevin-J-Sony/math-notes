
import subprocess
import os
import glob
import shutil

src_dir_list = ["Z:/books-to-read/alg-top", "Z:/books-to-read/diff-geo"]
out_dir_list = ["./algebraic_topology", "./differential_geometry"]

assert(len(src_dir_list) == len(out_dir_list))

# first clear out the old directories
try:
    for i in range(len(out_dir_list)):
        # remove the directory and then create it again
        shutil.rmtree(out_dir_list[i])
        os.makedirs(out_dir_list[i])
except Exception as e:
    print(f'Error clearing directory: {e}')


for i in range(len(src_dir_list)):
    for file in glob.glob(os.path.join(src_dir_list[i], "*.tex")):
        shutil.copy(file, out_dir_list[i])
        filename = os.path.basename(file)
        subprocess.run(["pdflatex.exe", filename], cwd=out_dir_list[i])
        print(filename)
