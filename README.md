This little tools allows you to subsample data from a larger dataset. 

The necessary conda environment can be installed form the environment.yaml file.

Tested for such a folder structure (0, 1, ... are the classes in your dataset):
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


# Folder Subsampler
This script allow you cut down the number of classes to the first `nb_classes` classes.

Commandline arguments:
`--input_path`: Path to the folder(s) that contains the class folders (train/val/test in the folder tree above)

`--output_path`: Path to the parent folder, where the folder(s) in the input path should be copied to. Folder is created if it does not exist.

`--nb_classes`: Number of classes that should be copied to the new dataset

Example command:
`python folder_subsampler.py --input-path /path/to/my_dataset/train,/path/to/my_dataset/val --output-path /path/to/my_small_dataset/ --nb_classes 100`


# File Subsampler
This script recreates the folder structure and samples at the lowes level of files.

Commandline arguments:
`--input_path`: Path to the parent folder (dataset in the folder tree above)

`--output_path`: Path where the files should be copied to. Folder is created if it does not exist.

`--file_percentage`: Percentage to be sampled (between 0 and 1)

`--random_file_sample`: Optional (default False). If set to true, random files are sampled instead of taking the first X% (after sorting).

Example command:
`python file_subsampler.py --input-path /path/to/my_dataset --output-path /path/to/my_small_dataset --file_percentage 0.01 --random-file-sample`