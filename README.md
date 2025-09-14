# Object Detection with YOLOv5

## Project Overview
This project focuses on detecting **four object classes** using a custom dataset:
  - `remote`
  - `tv`
  - `chair`
  - `table`
The trained model uses **YOLOv5** for object detection.

As instructed, i curated this dataset by taking photos of household items, which i annotated on makesense.ai(https://www.makesense.ai).
I proceeded to organing the data in YOLOv5 structure as follows:
  dataset/
    images/train/
    images/val/
    labels/train/
    labels/val/
ensuring all images have their corresponding annotations in the label folder.

I created a dataset config file with the directory to the traina and validation images along with the corresponding labels for each class, which has the following:

  train: assessment/images/train
  val: assessment/images/val

  nc: 4
  names: ['chair', 'remote', 'table', 'tv']

Back to the dataset, i parsed the annotations, extracting the class labels and bounding box details and formatting as a list, with the bounding box details in a list within this list. This is so i can examine and confirm the labels correpond to each image.

After the review and confirmation of the correspondence images and annotations, the next before training was the application of overfitting techniques. For the size of this dataset (234 images for both train and validation), overfitting is not far away. So i opted for three techniques to comabat it; Early Stopping, Data Augumentation and lowering Learning Rate. Ultralytics built the `Patience` command for early stopping. For the learning rate, i added it as part of the augmentations. Turned out if i had to tweak the hyper parameters, i had to tweak them all, which was now;

# Hyperparameters
lr0: 0.01
lrf: 0.01
momentum: 0.937
weight_decay: 0.0005
warmup_epochs: 3.0
warmup_momentum: 0.8
warmup_bias_lr: 0.1

# Augmentations
box: 0.05
cls: 0.5
cls_pw: 1.0
obj: 1.0
obj_pw: 1.0
iou_t: 0.20
anchor_t: 4.0
fl_gamma: 0.0
hsv_h: 0.015
hsv_s: 0.7
hsv_v: 0.4
degrees: 0.0
translate: 0.1
scale: 0.1
shear: 0.0
perspective: 0.0
flipud: 0.0
fliplr: 0.5
mosaic: 1.0
mixup: 0.2
copy_paste: 0.0

A brief description of each:
lr0: starting learning rate.
lrf: final learning rate (end of training).
momentum: helps smooth updates, keeps training stable.
weight_decay: small penalty to avoid overfitting.
warmup_epochs: how many epochs to slowly ramp up learning.
warmup_momentum: starting momentum during warmup.
warmup_bias_lr: starting bias learning rate during warmup.

Augmentations:
box: box loss gain (affects how much bbox error matters).
cls: class loss gain (importance of classification error).
cls_pw: class loss positive weight.
obj: objectness loss gain (confidence about object presence).
obj_pw: objectness positive weight.
iou_t: IoU threshold for assigning anchors to targets.
anchor_t: anchor matching threshold.
fl_gamma: focal loss gamma (handles class imbalance, 0 = off).
hsv_h: hue shift.
hsv_s: saturation shift.
hsv_v: value/brightness shift.
degrees: random rotation.
translate: random image shift.
scale: random zoom.
shear: random shear transform.
perspective: random perspective warp.
flipud: vertical flip probability.
fliplr: horizontal flip probability.
mosaic: probability of combining 4 images into 1 (for variety).
mixup: probability of blending 2 images.
copy_paste: probability of pasting objects from other images.

