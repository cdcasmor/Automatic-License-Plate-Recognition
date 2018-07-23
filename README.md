![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)
![built Using TensorFlow](https://img.shields.io/badge/built%20using-TensorFlow-blue.svg)
![built Using OpenCV](https://img.shields.io/badge/built%20using-OpenCV-brightgreen.svg)


<h1 align="center"> Automatic Number Plate Recognition </h1>

<p align="center"> Using neural networks to build an automatic number plate recognition system. </p>



<div align="center">

:taxi:

</div>



<p align="center"> <img src="https://github.com/yycyjqc/Automatic_Number_Plate_Recognition/blob/master/Image/vehicle-license-plates.png"> </p>


<p align="center">
  <a href="#members">Members</a> •
  <a href="#background">Background</a> •
  <a href="#proposal">Proposal</a> •
  <a href="#data-source">Data Source</a> •
  <a href="#process">Process</a> •
  <a href="#findings">Findings</a> •
  <a href="#limitations">Limitations</a> •
  <a href="#technology-stack-used">Technology Stack Used</a> •
<a href="#other">Other</a>
</p>

## Members
Welcome to the Automatic number-plate recognition project! We are team **Innovators**.

Reach us through LinkedIn:

-   [Cesar Castrejon](https://www.linkedin.com/in/cesar-castrejon-927164118/)
-   [Clifford Ferraren](https://www.linkedin.com/in/clifford-ferraren/)
-   [Sean Yu](https://www.linkedin.com/in/sean-yu-733205a6/)
-   [Tsering Sherpa](https://www.linkedin.com/in/tsering-sherpa-1171a7b4/)

## Background
**Automatic number-plate recognition** (ANPR) is a technology that uses optical character recognition on images to read vehicle registration plates to create vehicle location data. It can use existing closed-circuit television, road-rule enforcement cameras, or cameras specifically designed for the task. 

## Proposal

## Data Source

1. **```SUN397.tar.gz```**

   > 3GB of background images from the [SUN database](http://groups.csail.mit.edu/vision/SUN/). The tar file (36GB) can be [downloaded here](http://vision.princeton.edu/projects/2010/SUN/SUN397.tar.gz).   This step may take a while as it consists of 131,067 images.

2. **```UK Number Plate```**

   > Probably the UK's most popular number plate font. As used by the DVLA (gov.uk), HPI, Aviva, EuroCarParts and many more. It can be [download here]("https://www.dafont.com/uk-number-plate.font").

## Process 

#### Method

Neurons are kinda similar to logistic regression.

<img src="https://github.com/yycyjqc/Automatic_Number_Plate_Recognition/blob/master/Image/logistic_regression.png"> 

#### Synthesizing images

To train any neural net a set of training data along with correct outputs must be provided. In this case this will be a set of 128x64 images along with the expected output. Here’s an illustrative sample of training data generated for this project:

<img src="https://github.com/yycyjqc/Automatic_Number_Plate_Recognition/blob/master/Image/00000000_PV07NEU_1.png">

<img src="https://github.com/yycyjqc/Automatic_Number_Plate_Recognition/blob/master/Image/00000001_KM05MUP_1.png">

<img src="https://github.com/yycyjqc/Automatic_Number_Plate_Recognition/blob/master/Image/00000003_LK39UGD_1.png">



However, the system does not always work well. Here is the failed example:

<img src="https://github.com/yycyjqc/Automatic_Number_Plate_Recognition/blob/master/Image/00000002_HY03KBG_0.png">



Click [here](https://www.dropbox.com/s/nwfk2mvf6d8fqvm/weights.npz?dl=0) to download the pretrained model ```weights.npz```.

<img src="https://github.com/yycyjqc/Automatic_Number_Plate_Recognition/blob/master/Image/extractbgs.gif">

## Findings 

## Limitations 

## Technology Stack Used
- scikit-learn

  > **Scikit-learn** is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
- TensorFlow

  >**TensorFlow** is an open-source software library for dataflow programming across a range of tasks. It is a symbolic math library, and is also used for machine learning applications such as neural networks.

- OpenCV

  > **OpenCV** (Open Source Computer Vision Library) is released under a BSD license and hence it’s free for both academic and commercial use. OpenCV was designed for computational efficiency and with a strong focus on real-time applications.

- NumPy

  >**NumPy** is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

## Other

