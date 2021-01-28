import fire
from pathlib import Path
import random
import os
import shutil


def folder_subsampler(input_path, output_path, percentage):
    output_p = Path(output_path)
    output_p.mkdir(parents=True, exist_ok=True)

    f = [(dirpath, dirnames, filenames) for dirpath, dirnames, filenames in os.walk(input_path)]
    dir_files_dict = {tup[0]: [i for i in tup[2] if i[0] != '.'] for tup in f if len(tup[1]) == 0}

    # create the folder structure
    # select and copy the files
    for in_folder, file_list in dir_files_dict.items():
        out_folder = in_folder.replace(input_path, output_path)
        Path(out_folder).mkdir(parents=True, exist_ok=True)
        samples_files = random.sample(file_list, max(1, int(percentage * len(file_list))))
        for file in samples_files:
            shutil.copy2(os.path.join(in_folder, file), os.path.join(out_folder, file))


if __name__ == '__main__':
    fire.Fire(folder_subsampler)
