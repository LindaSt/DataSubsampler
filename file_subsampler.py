import fire
from pathlib import Path
import random
import os
import shutil


def _get_samples_files(file_list, file_percentage, random_file_sample):
    if random_file_sample:
        samples_files = random.sample(file_list, max(1, int(file_percentage * len(file_list))))
    else:
        samples_files = file_list[:max(1, int(file_percentage * len(file_list)))]
    return samples_files


def file_subsampler(input_path, output_path, file_percentage, file_ending=".gxl", random_file_sample=False,
                    symlink=False, train_only=False):
    output_p = Path(output_path)
    output_p.mkdir(parents=True, exist_ok=True)

    f = [(dirpath, dirnames, filenames) for dirpath, dirnames, filenames in os.walk(input_path) if len(filenames) > 0 and file_ending in filenames[0]]
    dir_files_dict = {tup[0]: sorted([i for i in tup[2] if i[0] != '.']) for tup in f if len(tup[1]) == 0}

    # create the folder structure
    # select and copy the files
    for in_folder, file_list in dir_files_dict.items():
        if input_path[-1] == '/':
            input_path = input_path[:-1]
        if output_path[-1] == '/':
            output_path = output_path[:-1]

        out_folder = in_folder.replace(input_path, output_path)
        Path(out_folder).mkdir(parents=True, exist_ok=True)
        # reduce file list
        if train_only:
            if 'train' in in_folder:
                samples_files = _get_samples_files(file_list, file_percentage, random_file_sample)
            else:
                samples_files = file_list
        else:
            samples_files = _get_samples_files(file_list, file_percentage, random_file_sample)

        for file in samples_files:
            if symlink:
                print(f'Creating symlink for {os.path.join(in_folder, file)}')
                os.symlink(os.path.join(in_folder, file), os.path.join(out_folder, file))
            else:
                print(f'Copying file {os.path.join(in_folder, file)}')
                shutil.copy2(os.path.join(in_folder, file), os.path.join(out_folder, file))


if __name__ == '__main__':
    fire.Fire(file_subsampler)
