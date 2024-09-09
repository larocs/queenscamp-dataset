<img src=./assets/sample-dataset.png width="75%" height="75%">

<p style="text-align: justify;">
The QueensCAMP dataset is a collection of RGB-D images of an indoor environment designed to evaluate VSLAM systems' robustness in real-world indoor environments with diverse challenges. The dataset contains dynamic objects, motion blur, lighting changes, and other challenges that are common in real-world indoor environments. Additionally, it includes sequences with emulated lens failures.

The images are captured using an Intel RealSense D435 camera mounted on an handheld aerial vehicle. The dataset includes ground truth poses for each frame captured by a Vicon motion capture system.

We captured 16 sequences, resulting in a total of 28,523 images at 15 frames per second. Additionally, for each sequence we generated 6 more sequences with induced failures, leading to a total of 112 sequences and 199,661 images with 13,861.12 seconds in total duration. The RGB and Depth images resolution are provided in a resolution of 640x480.
</p>



## Download
<p style="text-align: justify;">

You can download the sequences with the failures or only the raw bags (without emulated failures). The raw images are not aligned with the depth images. RGB images were captured at a resolution of 1920x1080, while depth images were captured at 640x480. 
</p>


- 01: [Full Sequence (6.0 GB)](https://drive.usercontent.google.com/download?id=1H6_Y_DupjIJNn4tnIFHsXhW0KqEeTJHm&export=download) |
               [Bag (0.5 MB)](https://drive.usercontent.google.com/download?id=1xjIQjClK1niVoXDSxSNxQe76FkAcNAff&export=download)

- 02:

- 03:

- 04:

- 05:

- 06:

- 07:

- 08:

- 09:

- 10:

- 11:

- 12:

- 13:

- 14:

- 15:

- 16:

## Dataset tools

The scripts used for post-processing of the bags and inserting failures are available in the [QueensCAMP Dataset Tools](https://github.com/larocs/queenscamp-dataset) repository.


## Citation

If you use this dataset in your research, please cite the following paper:

```
@inproceedings{queenscamp2024,
  title={QueensCAMP: an RGB-D dataset for robust Visual SLAM},
  author={Authors},
  booktitle={Conference},
  year={2024}
}
```