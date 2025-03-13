# QueensCAMP Dataset Tools

This repository contains tools for the QueensCAMP dataset. The dataset is a collection of RGB-D images of an indoor environment designed to evaluate VSLAM systems' robustness in real-world indoor environments with diverse challenges.
Below there is a video illustrating various lens failures included in the dataset that can be emulated with the provided tools:

[![Dataset Sample](assets/thumbnail.png)](https://www.youtube.com/watch?v=YoLkNhWoUXY)

## Scripts Usage

### 1. Download the dataset

* RGB Camera info is available [here](https://drive.usercontent.google.com/uc?id=16JEOw3xNZu8f79BG29LN6BoParwQUhqU)

* Depth Camera info is available [here](https://drive.usercontent.google.com/uc?id=1IqAv9xRtl1qZ4iXHHOcg_rNLyAPKUIw1)

There are 16 sequences, you can download the sequences with the failures or only the raw bags (without emulated failures):

- 01: [Full Sequence (6.0 GB)](https://drive.usercontent.google.com/download?id=1nqa7ft5MKF0wcJd9GyHwLBtAL7D1OV47&export=download) |
               [Bag (0.5 GB)](https://drive.usercontent.google.com/download?id=1xjIQjClK1niVoXDSxSNxQe76FkAcNAff&export=download)

- 02: [Full Sequence (8.1 GB)](https://drive.usercontent.google.com/download?id=1D1wiifPuNYeotUNdMXFZDKXJJ_X_aiuF&export=download) |
               [Bag (0.7 GB)](https://drive.usercontent.google.com/download?id=15fQOuLZwFsG5um1BvkKsW7BzuF-Uz_bn&export=download)

- 03: [Full Sequence (6.9 GB)](https://drive.usercontent.google.com/download?id=16zeLzSl9FB-43kvDg77Xiva5teQYdw3r&export=download) |
                [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1fmWsYXq9EW7YzyX1CuKLe_LLKXuKcL1p&export=download)

- 04: [Full Sequence (6.9 GB)](https://drive.usercontent.google.com/download?id=1baHAq8XdyKSh1rX_6fpZ7zJKM29UW1wZ&export=download) |
        [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1jhRtQ_JpK9KXfJeLONSr0MGfzx0a1VLy&export=download)

- 05: [Full Sequence (9.2 GB)](https://drive.usercontent.google.com/download?id=1WmULSIyx9UtDKhr1H_0DOEazRkbOMIm3&export=download) |
        [Bag (0.7 GB)](https://drive.usercontent.google.com/download?id=1PexbcMAuAYAPID1NDunT5uqExfiDSxhF&export=download)

- 06: [Full Sequence (9.0 GB)](https://drive.usercontent.google.com/download?id=1h_c-l19GEGLTc-gLBfEbZCbZOK-KFRDt&export=download) |
        [Bag (0.7 GB)](https://drive.usercontent.google.com/download?id=1YSHISkkQpSvU5GGhAY6ZsPaD8WIbrv0x&export=download)

- 07: [Full Sequence (7.7 GB)](https://drive.usercontent.google.com/download?id=1GJM3pz_BnLuGTq4CytuYEAZqraqH_ck3&export=download) |
        [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1qXwq9cl_mcNPt2ANd8gg6Eqn6QjHwf9V&export=download)

- 08: [Full Sequence (5.2 GB)](https://drive.usercontent.google.com/download?id=1jKQo7DGmUXfP35yZ70NiBR6hqwSSa84e&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1qF4QE2gLNhoUIO-KlBznHpQIck-p9g97&export=download)

- 09: [Full Sequence (4.2 GB)](https://drive.usercontent.google.com/download?id=1ja_qvTYSmGJPxoVAm89Ay2pIiDLXjvw4&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1RgAflLe3xeAsIP-RgxrkaKOP7L_zEANw&export=download)

- 10: [Full Sequence (5.7 GB)](https://drive.usercontent.google.com/download?id=1RBpzd42HbjEOmdjLONgsXi3GgDy_AyUF&export=download) |
        [Bag (0.5 GB)](https://drive.usercontent.google.com/download?id=1TSWsITjPNu-nBko9QufAy7LLEdaOTTtu&export=download)

- 11: [Full Sequence (4.7 GB)](https://drive.usercontent.google.com/download?id=1XmyRndO7CKdTVmeuZfYUzd5okKbgVeZM&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1tOKUJKg8pC2e2RcZs5JQ_95SDt62Ps5j&export=download)

- 12: [Full Sequence (4.6 GB)](https://drive.usercontent.google.com/download?id=13966F62XT715PDz5STvwla8EAftOyzKJ&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1reJzXP6iS9ij_LSm4sJ6MqVEtvRJHCdB&export=download)

- 13: [Full Sequence (4.7 GB)](https://drive.usercontent.google.com/download?id=1MVWvxYA8ZWXM5yB0ZtEqjHl3AGdPwrKz&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=13K2wL0HaefcJ6UMjC3W5YIOQGENhAEca&export=download)

- 14: [Full Sequence (3.4 GB)](https://drive.usercontent.google.com/download?id=1EuQpPZC4vqVSyoHel3GADSzbrdPbZswv&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1lfcyFHUTmP4saGPSl5LaOgMF3zOYAocl&export=download)

- 15: [Full Sequence (6.4 GB)](https://drive.usercontent.google.com/download?id=1FsjWzlUupiUxAfD6hBum70dqTznlTzQQ&export=download) |
        [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1K-0tqTxQlgvEluhMf_exRRYFQkKH5i8u&export=download)

- 16: [Full Sequence (4.2 GB)](https://drive.usercontent.google.com/download?id=1MCcSApcisMupuyX0K09A8kjQl7aIG7M4&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1kUfufHLgd9Q9Z3Eb1gAdgDXD3rPxdA6P&export=download)

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
@misc{bruno2024queenscamprgbddatasetrobust,
      title={QueensCAMP: an RGB-D dataset for robust Visual SLAM}, 
      author={Hudson M. S. Bruno and Esther L. Colombini and Sidney N. Givigi Jr au2},
      year={2024},
      eprint={2410.12520},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2410.12520}, 
}
```
## Other publications
Check out our modular visual odometry framework, which is available [here](https://github.com/larocs/modvo).
