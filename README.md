# MovieMania - a Movie Recommender System using the Google Cloud Platform 
### Welcome to an intelligent, knowledge-based System to recommend movies! 
#### Anusha Balaji, Pallav Jhaveri, Darshan Shah, Kush Shah 


Please check out the [readme](https://github.com/shahkush18/knowledge-based-systems/blob/master/info/readme.md) in **`info/`** folder to access a more comprehensive report on our system! 

# How MovieMania Works 

## Collaborative Filtering in TensorFlow using WALS

This code implements a collaborative filtering recommendation model using the WALS
(weighted least alternating squares) algorithm provided in TensorFlow, and applies
it to the MovieLens data set.

## Installation & Setup 

This code assumes python 2.

* Install miniconda2:

https://conda.io/docs/user-guide/install/index.html


* Create environment and install packages:

Assuming you are in the repo directory:

```
$ conda create -n tfrec
$ conda install -n tfrec --file requirements.txt
```

* Install TensorFlow.

CPU:
```
$ pip install tensorflow
```

Or GPU, if one is available in your environment:

```
$ pip install tensorflow-gpu
```


## Download Movielens Data

```
$ curl -O 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
$ unzip ml-100k.zip
$ mkdir data
$ cp ml-100k/u.data data/
```

## Run

*   Train the model locally
```
$ ./mltrain.sh local data/u.data
```

*   Train the model on ML Engine:
```
$ gsutil cp data/u.data gs://mybucket/data/u.data
$ ./mltrain.sh train gs://mybucket/data/u.data

```

*   Hyperparameter tuning on ML Engine:
```
$ ./mltrain.sh tune gs://mybucket/data/u.data

```
