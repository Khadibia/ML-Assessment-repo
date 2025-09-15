# Object Detection with YOLOv5

## Project Overview
This project focuses on detecting **four object classes** using a custom dataset:
  - `remote`
  - `tv`
  - `chair`
  - `table`
The trained model uses **YOLOv5** for object detection.

As instructed, i curated this dataset by taking photos of household items, which i annotated on makesense.ai(https://www.makesense.ai).

The link to my train and val images; https://drive.google.com/drive/folders/1s7FreXGXTYwi6rfqFfmVlQl64BaP-szg?usp=sharing

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

The final folder sructure was;
├── dataset/
│ ├── images/
│ │ ├── train/
│ │ └── val/
│ ├── labels/
│ │ ├── train/
│ │ └── val/
├── data.yaml -> config file
├── best.pt -> final weights
└── README.md -> project documentation

After the review and confirmation of the correspondence images and annotations, the next before training was the application of overfitting techniques. For the size of this dataset (234 images for both train and validation), overfitting is not far away. So i opted for three techniques to comabat it; Early Stopping, Data Augumentation and lowering Learning Rate. Ultralytics built the `Patience` command for early stopping. For the learning rate, i added it as part of the augmentations. Turned out if i had to tweak the hyper parameters, i had to tweak them all, which was now;

# Hyperparameters
* lr0: 0.01
* lrf: 0.01
* momentum: 0.937
* weight\_decay: 0.0005
* warmup\_epochs: 3.0
* warmup\_momentum: 0.8
* warmup\_bias\_lr: 0.1

# Augmentations
* box: 0.05
* cls: 0.5
* cls\_pw: 1.0
* obj: 1.0
* obj\_pw: 1.0
* iou\_t: 0.20
* anchor\_t: 4.0
* fl\_gamma: 0.0
* hsv\_h: 0.015
* hsv\_s: 0.7
* hsv\_v: 0.4
* degrees: 0.0
* translate: 0.1
* scale: 0.1
* shear: 0.0
* perspective: 0.0
* flipud: 0.0
* fliplr: 0.5
* mosaic: 1.0
* mixup: 0.2
* copy\_paste: 0.0

A brief description of each:
* lr0: starting learning rate
* lrf: final learning rate (end of training)
* momentum: helps smooth updates, keeps training stable
* weight\_decay: small penalty to avoid overfitting
* warmup\_epochs: how many epochs to slowly ramp up learning
* warmup\_momentum: starting momentum during warmup
* warmup\_bias\_lr: starting bias learning rate during warmup

Augmentations:
* box: box loss gain (affects how much bbox error matters)
* cls: class loss gain (importance of classification error)
* cls\_pw: class loss positive weight
* obj: objectness loss gain (confidence about object presence)
* obj\_pw: objectness positive weight
* iou\_t: IoU threshold for assigning anchors to targets
* anchor\_t: anchor matching threshold
* fl\_gamma: focal loss gamma (handles class imbalance, 0 = off)
* hsv\_h: hue shift
* hsv\_s: saturation shift
* hsv\_v: value/brightness shift
* degrees: random rotation
* translate: random image shift
* scale: random zoom
* shear: random shear transform
* perspective: random perspective warp
* flipud: vertical flip probability
* fliplr: horizontal flip probability
* mosaic: probability of combining 4 images into 1 (for variety)
* mixup: probability of blending 2 images
* copy\_paste: probability of pasting objects from other images

# Instructions on how to setup and run the model
1. pip install -r requirements.txt
2. Prepare test image and place model in same folder as pred script. The script will load the model, run inference on the specified image, and print the results.
3. run predictions using pred script.py
4. Check results. Annotated images show detected objects with class IDs, confidence scores, and bounding box coordinates.

# Final Model Performance Metrics
| Class  | Images | Instances | P     | R     | mAP50 | mAP50-95 |
| ------ | ------ | --------- | ----- | ----- | ----- | -------- |
| all    | 31     | 31        | 0.788 | 0.846 | 0.879 | 0.682    |
| chair  | 31     | 12        | 0.841 | 0.883 | 0.945 | 0.801    |
| remote | 31     | 7         | 0.910 | 1.000 | 0.995 | 0.788    |
| table  | 31     | 6         | 0.504 | 0.500 | 0.580 | 0.438    |
| tv     | 31     | 6         | 0.899 | 1.000 | 0.995 | 0.699    |

