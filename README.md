# QueensCAMP

This repository contains tools for the QueensCAMP dataset. The dataset is a collection of RGB-D images of an indoor environment designed to evaluate VSLAM systems' robustness in real-world indoor environments with diverse challenges.
Below are sample images illustrating various lens failures included in the dataset that can be emulated with the provided tools:

<div style="display: flex; justify-content: center; gap: 20px;">
  <figure style="text-align: center;">
    <img src="./assets/sample-image.png" width="200" />
    <figcaption>Sample Image</figcaption>
  </figure>
</div>

<div style="display: flex; justify-content: center; gap: 20px;">
  <figure style="text-align: center;">
    <img src="./assets/sample-underexposure.png" width="200" />
    <figcaption>Underexposure</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="./assets/sample-overexposure.png" width="200" />
    <figcaption>Overexposure</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="./assets/sample-breakage.png" width="200" />
    <figcaption>Lens Breakage</figcaption>
  </figure>
</div>

<div style="display: flex; justify-content: center; gap: 20px;">
  <figure style="text-align: center;">
    <img src="./assets/sample-wet.png" width="200" />
    <figcaption>Wet Lens</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="./assets/sample-condensation.png" width="200" />
    <figcaption>Condensation</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="./assets/sample-dirt.png" width="200" />
    <figcaption>Dirty Lens</figcaption>
  </figure>
</div>

## Scripts Usage

### 1. Download the dataset

### 2. Rosbags Post-Processing
If you plan to download the rosbags, you can use the post-processing script to convert the rosbags to images and depth maps. The script will also generate the ground truth poses for each frame. Feel free to modify the script to suit your needs.

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
- 'rain'
- 'condensation'
- 'dirt'

```bash
python insert_failures.py --sequence_path <path_to_sequence> --failure_type <failure_type> --output_path <path_to_save_sequence>
```

### 4. Evaluation
The script `evaluate.py` can be used to evaluate the performance of a VO/VSLAM system on the dataset. The script will compare the estimated trajectory with the ground truth trajectory and output the ATE error. The results can either be printed on the console or saved to a file.

```bash
python evaluate.py <reference_file> <estimated_file> --output_path <path_to_save_results>
```
