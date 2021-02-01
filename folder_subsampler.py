import fire
from pathlib import Path
import os
import shutil


def folder_subsampler(input_path, output_path, nb_classes):
    input_paths = input_path.split(',')
    for in_path in input_paths:
        out_path = os.path.join(output_path, os.path.basename(in_path))
        output_p = Path(out_path)
        output_p.mkdir(parents=True, exist_ok=True)

        f = [(dirpath, dirnames, filenames) for dirpath, dirnames, filenames in os.walk(in_path)]
        to_copy = sorted(f[0][1])[:nb_classes]

        # create the folder structure
        for subfolder in to_copy:
            shutil.copytree(os.path.join(in_path, subfolder), os.path.join(out_path, subfolder))


if __name__ == '__main__':
    fire.Fire(folder_subsampler)
