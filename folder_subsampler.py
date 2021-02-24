import fire
from pathlib import Path
import os
import shutil


def folder_subsampler(input_path, output_path, nb_classes, symlink=False):
    input_paths = input_path.split(',')
    for in_path in input_paths:
        out_path = os.path.join(output_path, os.path.basename(in_path))
        output_p = Path(out_path)
        output_p.mkdir(parents=True, exist_ok=True)

        f = [(dirpath, dirnames, filenames) for dirpath, dirnames, filenames in os.walk(in_path)][0][1]
        # check if folder names are ints, because then the sorting is not numerical (0,1,2) but '1','10', etc
        if f[0].isdigit():
            f = [int(i) for i in f]

        to_copy = sorted(f)[:nb_classes]

        # create the folder structure
        for subfolder in to_copy:
            if symlink:
                print(f'Creating symlink for folder {os.path.join(in_path, str(subfolder))}')
                os.symlink(os.path.join(in_path, str(subfolder)), os.path.join(out_path, str(subfolder)))
            else:
                print(f'Copying folder {os.path.join(in_path, str(subfolder))}')
                shutil.copytree(os.path.join(in_path, str(subfolder)), os.path.join(out_path, str(subfolder)))


if __name__ == '__main__':
    fire.Fire(folder_subsampler)
