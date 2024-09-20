# QueensCAMP Dataset Tools

This repository contains tools for the QueensCAMP dataset. The dataset is a collection of RGB-D images of an indoor environment designed to evaluate VSLAM systems' robustness in real-world indoor environments with diverse challenges.
Below are sample images illustrating various lens failures included in the dataset that can be emulated with the provided tools:

![sample-dataset](./assets/sample-dataset.png)

## Scripts Usage

### 1. Download the dataset

* RGB Camera info is available [here](https://drive.usercontent.google.com/uc?id=16JEOw3xNZu8f79BG29LN6BoParwQUhqU)

* Depth Camera info is available [here](https://drive.usercontent.google.com/uc?id=1IqAv9xRtl1qZ4iXHHOcg_rNLyAPKUIw1)

There are 16 sequences, you can download the sequences with the failures or only the raw bags (without emulated failures):

- 01: [Full Sequence (6.0 GB)](https://drive.usercontent.google.com/download?id=1H6_Y_DupjIJNn4tnIFHsXhW0KqEeTJHm&export=download) |
               [Bag (0.5 GB)](https://drive.usercontent.google.com/download?id=1xjIQjClK1niVoXDSxSNxQe76FkAcNAff&export=download)

- 02: [Full Sequence (8.1 GB)](https://drive.usercontent.google.com/download?id=19XVonI6U5cMy66qPH5YhF-IPB-cVH_JO&export=download) |
               [Bag (0.7 GB)](https://drive.usercontent.google.com/download?id=15fQOuLZwFsG5um1BvkKsW7BzuF-Uz_bn&export=download)

- 03: [Full Sequence (6.9 GB)](https://drive.usercontent.google.com/download?id=14XWFysXbD_W60ujBCDyY95F3d87vCtZO&export=download) |
                [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1fmWsYXq9EW7YzyX1CuKLe_LLKXuKcL1p&export=download)

- 04: [Full Sequence (6.9 GB)](https://drive.usercontent.google.com/download?id=1K4rlcI74OkwI9VLLBeY9FH-39VaC5fV4&export=download) |
        [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1jhRtQ_JpK9KXfJeLONSr0MGfzx0a1VLy&export=download)

- 05: [Full Sequence (9.2 GB)](https://drive.usercontent.google.com/download?id=1ERtGT_XPessxwUQ7dcyip1nSz4yAvE7P&export=download) |
        [Bag (0.7 GB)](https://drive.usercontent.google.com/download?id=1PexbcMAuAYAPID1NDunT5uqExfiDSxhF&export=download)

- 06: [Full Sequence (9.0 GB)](https://drive.usercontent.google.com/download?id=1cAnE0gxJPenBW_eK10atMoL5tCZWcvTx&export=download) |
        [Bag (0.7 GB)](https://drive.usercontent.google.com/download?id=1YSHISkkQpSvU5GGhAY6ZsPaD8WIbrv0x&export=download)

- 07: [Full Sequence (7.7 GB)](https://drive.usercontent.google.com/download?id=12OqTWhZbfFAoL-DuAbp77-SAZQBD2oXF&export=download) |
        [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1qXwq9cl_mcNPt2ANd8gg6Eqn6QjHwf9V&export=download)

- 08: [Full Sequence (5.2 GB)](https://drive.usercontent.google.com/download?id=1Q73NRw96wioWblvFmMgCB2E5EwfgRsq1&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1qF4QE2gLNhoUIO-KlBznHpQIck-p9g97&export=download)

- 09: [Full Sequence (4.2 GB)](https://drive.usercontent.google.com/download?id=1RTLnDZazFc2EKciGrayDelXRpT6WLEda&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1RgAflLe3xeAsIP-RgxrkaKOP7L_zEANw&export=download)

- 10: [Full Sequence (5.7 GB)](https://drive.usercontent.google.com/download?id=1cgPKmhMUwS5iszLFDjOVJ0-PKLg4Wysn&export=download) |
        [Bag (0.5 GB)](https://drive.usercontent.google.com/download?id=1TSWsITjPNu-nBko9QufAy7LLEdaOTTtu&export=download)

- 11: [Full Sequence (4.7 GB)](https://drive.usercontent.google.com/download?id=1MJIKAmhgvLfGV4RFH9UfEmhwX6lWuEgE&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1tOKUJKg8pC2e2RcZs5JQ_95SDt62Ps5j&export=download)

- 12: [Full Sequence (4.6 GB)](https://drive.usercontent.google.com/download?id=1adr-_G7FEwYVyKmNnbTKdEJaq48bKBM-&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1SlcGbPDHlwJ6RMTK_YckdmRoqBvEp5C6&export=download)

- 13: [Full Sequence (4.7 GB)](https://drive.usercontent.google.com/download?id=1hkKuaEauJMDE874IahYbSNlzAspFTcIR&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=13K2wL0HaefcJ6UMjC3W5YIOQGENhAEca&export=download)

- 14: [Full Sequence (3.4 GB)](https://drive.usercontent.google.com/download?id=15MQ8R4owPvb_g3eTKrm1JBXdj5MRSFWq&export=download) |
        [Bag (0.4 GB)](https://drive.usercontent.google.com/download?id=1lfcyFHUTmP4saGPSl5LaOgMF3zOYAocl&export=download)

- 15: [Full Sequence (6.4 GB)](https://drive.usercontent.google.com/download?id=13IrfPcwxmFRauRTLp8HbiDdebsVIgLtL&export=download) |
        [Bag (0.6 GB)](https://drive.usercontent.google.com/download?id=1K-0tqTxQlgvEluhMf_exRRYFQkKH5i8u&export=download)

- 16: [Full Sequence (4.2 GB)](https://drive.usercontent.google.com/download?id=1NgSeh7LJXVZG024mrV-l0pWlvphj4SST&export=download) |
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
