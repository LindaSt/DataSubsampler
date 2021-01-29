# FolderSubsampler

This little tools allows you to subsample data from a larger dataset. It recreates the folder structure and samples at the lowes level of files.

Commandline arguments:
`--input_path`: Path to the parent folder, which should be

`--output_path`: Path where the files should be copied to. Folder is created if it does not exist.

`--file_percentage`: Percentage to be sampled (between 0 and 1)

`--random_file_sample`: Optional (default False). If set to true, random files are sampled instead of taking the first X% (after sorting).

Example command:
`python folder_subsampler.py --input-path /path/to/my_dataset --output-path /path/to/my_small_dataset -file_percentage 0.01 --random-file-sample`


The necessary conda environment can be installed form the environment.yaml file.

Tested for such a folder structure:
```
dataset
└───train
│   └───0
│   │   │   file000.txt
│   │   │   ...
│   │
│   └───1
│   │   │   file100.txt
│   │   │   ...
│   │
│   └───...
│ 
└───val
│   └───0
│   │   │   file000.txt
│   │   │   ...
│   │
│   └───1
│   │   │   file100.txt
│   │   │   ...
│   │
│   └───...
│ 
└───test
    └───0
    │   │   file000.txt
    │   │   ...
    │
    └───1
    │   │   file100.txt
    │   │   ...
    │
    └───...
```
