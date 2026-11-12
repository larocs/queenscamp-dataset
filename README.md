# QueensCAMP Dataset Tools

This repository contains tools for the QueensCAMP dataset. The dataset is a collection of RGB-D images of an indoor environment designed to evaluate VSLAM systems' robustness in real-world indoor environments with diverse challenges.
Below there is a video illustrating various lens failures included in the dataset that can be emulated with the provided tools:

[![Dataset Sample](assets/thumbnail.png)](https://www.youtube.com/watch?v=YoLkNhWoUXY)

## Scripts Usage

### 1. Download the dataset

* RGB Camera info is available [here](https://drive.usercontent.google.com/uc?id=16JEOw3xNZu8f79BG29LN6BoParwQUhqU)

* Depth Camera info is available [here](https://drive.usercontent.google.com/uc?id=1IqAv9xRtl1qZ4iXHHOcg_rNLyAPKUIw1)

There are 16 sequences, you can download the sequences with the failures or only the raw bags (without emulated failures):

- 01: [Full Sequence (6.0 GB)](https://zenodo.org/records/13754512/files/01.zip?download=1) |
               [Bag (0.5 GB)](https://zenodo.org/records/13754512/files/sequence1-dynamic.zip?download=1)

- 02: [Full Sequence (8.1 GB)](https://zenodo.org/records/13754512/files/02.zip?download=1) |
               [Bag (0.7 GB)](https://zenodo.org/records/13754512/files/sequence2-static.zip?download=1)

- 03: [Full Sequence (6.9 GB)](https://zenodo.org/records/13754512/files/03.zip?download=1) |
                [Bag (0.6 GB)](https://zenodo.org/records/13754512/files/sequence3-static.zip?download=1)

- 04: [Full Sequence (6.9 GB)](https://zenodo.org/records/13754512/files/04.zip?download=1) |
        [Bag (0.6 GB)](https://zenodo.org/records/13754512/files/sequence4-dynamic.zip?download=1)

- 05: [Full Sequence (9.2 GB)](https://zenodo.org/records/13754512/files/05.zip?download=1) |
        [Bag (0.7 GB)](https://zenodo.org/records/13754512/files/sequence5-dynamic.zip?download=1)

- 06: [Full Sequence (9.0 GB)](https://zenodo.org/records/13754512/files/06.zip?download=1) |
        [Bag (0.7 GB)](https://zenodo.org/records/13754512/files/sequence6-dynamic.zip?download=1)

- 07: [Full Sequence (7.7 GB)](https://zenodo.org/records/13754512/files/07.zip?download=1) |
        [Bag (0.6 GB)](https://zenodo.org/records/13754512/files/sequence7-dynamic.zip?download=1)

- 08: [Full Sequence (5.2 GB)](https://zenodo.org/records/13754512/files/08.zip?download=1) |
        [Bag (0.4 GB)](https://zenodo.org/records/13754512/files/sequence8-static.zip?download=1)

- 09: [Full Sequence (4.2 GB)](https://zenodo.org/records/13754512/files/09.zip?download=1) |
        [Bag (0.4 GB)](https://zenodo.org/records/13754512/files/sequence9-static.zip?download=1)

- 10: [Full Sequence (5.7 GB)](https://zenodo.org/records/13754512/files/10.zip?download=1) |
        [Bag (0.5 GB)](https://zenodo.org/records/13754512/files/sequence10-static.zip?download=1)

- 11: [Full Sequence (4.7 GB)](https://zenodo.org/records/13754512/files/11.zip?download=1) |
        [Bag (0.4 GB)](https://zenodo.org/records/13754512/files/sequence11-static.zip?download=1)

- 12: [Full Sequence (4.6 GB)](https://zenodo.org/records/13754512/files/12.zip?download=1) |
        [Bag (0.4 GB)](https://zenodo.org/records/13754512/files/sequence12-static.zip?download=1)

- 13: [Full Sequence (4.7 GB)](https://zenodo.org/records/13754512/files/13.zip?download=1) |
        [Bag (0.4 GB)](https://zenodo.org/records/13754512/files/sequence13-static.zip?download=1)

- 14: [Full Sequence (3.4 GB)](https://zenodo.org/records/13754512/files/14.zip?download=1) |
        [Bag (0.4 GB)](https://zenodo.org/records/13754512/files/sequence14-static.zip?download=1)

- 15: [Full Sequence (6.4 GB)](https://zenodo.org/records/13754512/files/15.zip?download=1) |
        [Bag (0.6 GB)](https://zenodo.org/records/13754512/files/sequence15-static.zip?download=1)

- 16: [Full Sequence (4.2 GB)](https://zenodo.org/records/13754512/files/16.zip?download=1) |
        [Bag (0.4 GB)](https://zenodo.org/records/13754512/files/sequence16-static.zip?download=1)

You can also download the dataset from [Zenodo](https://zenodo.org/records/13754512).

### 2. Rosbags Post-Processing
If you plan to download the rosbags, you can use the post-processing script to convert the rosbags to images and depth maps. The script will also generate the ground truth poses for each frame. Feel free to modify the script to suit your needs.

Usage:

```bash
python convert_bag_to_files.py <path_to_rosbag> --timestamps <path_to_save_timestamps> --trajectory_file <path_to_save_trajectory> --image_folder <path_to_save_images> --depth_folder <path_to_save_depths> --image_topic <image_topic> --depth_topic <depth_topic> --pose_topic <odom_topic>
```

For the dataset we also used the parameter `--skip 100` to skip the first 100 frames to reduce the size of static images.

### 3. Inserting Failures
The script `insert_failures.py` can be used to insert failures in the dataset images. Currently, the failures available are:
- 'underexposure'
- 'overexposure'
- 'blur'
- 'breakage'
- 'wet'
- 'condensation'
- 'dirt'

The templates for the failures are available in the `failures` folder.

Usage:

```bash
python insert_failures.py --sequence_path <path_to_sequence> --failure_type <failure_type> --output_path <path_to_save_sequence>
```

### 4. Evaluation
The script `evaluate.py` can be used to evaluate the performance of a VO/VSLAM system on the dataset. The script will compare the estimated trajectory with the ground truth trajectory and output the ATE error. The results can either be printed on the console or saved to a file.

Usage:

```bash
python evaluate.py <reference_file> <estimated_file> --output_path <path_to_save_results>
```

## Citation

If you use the dataset or tools in your research, please cite the following paper:

```
@INPROCEEDINGS{11338683,
  author={Bruno, Hudson M. S. and Colombini, Esther L. and Givigi, Sidney N.},
  booktitle={2025 IEEE International Conference on Advanced Robotics (ICAR)}, 
  title={QueensCAMP: an RGB-D dataset for robust Visual SLAM}, 
  year={2025},
  volume={},
  number={},
  pages={798-803},
  keywords={Degradation;Visualization;Simultaneous localization and mapping;Heuristic algorithms;Dynamics;Lighting;Cameras;Robustness;Lenses;Visual odometry},
  doi={10.1109/ICAR65334.2025.11338683}}
```
## Other publications
Check out our modular visual odometry framework, which is available [here](https://github.com/larocs/modvo).
