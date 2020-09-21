# fast-video-segmentation


## Installation

This projects depends following main packages

1. tensorflow==1.14
2. tensorflow-gpu==1.14 (if gpu is available)

There are three different ways to setup the environment. **Choose one**. Ideally first and second are recommended. 
All the setups are tested on mac os.

1. poetry

Install poetry by following the [installation link][]

[installation link]: https://python-poetry.org/docs/#installation

After installation. 

	$ poetry update

This will install required dependencies by following the dependency list from [pyproject.toml](pyproject.toml)

run the following command to load the environment.

	$ poetry shell

if gpu is available on the machine then install the following

	$ pip install tensorflow-gpu==1.14


2. Conda

Install [miniconda][] by following the [conda installation link][]

[conda installation link]: https://docs.conda.io/en/latest/miniconda.html
[miniconda]: https://docs.conda.io/en/latest/miniconda.html

After conda installation, Create conda environment

	$ conda env create -f environment.yml

This will install required dependencies by following the dependency list from [environment.yml](environment.yml)

run the following command to load the environment.

	$ conda activate video-semantic-segmentation-network

if gpu is available on the machine then install the following

	$ pip install tensorflow-gpu==1.14


3. setup.py

This method can be used if this projects is run on google colab kind of environments where poetry and conda virtual environments are unavailable.

	$ python setup.py install

This will install required dependencies. If gpu is available on the machine then install the following

	$ pip install tensorflow-gpu==1.14


## Jupyter setup

Jupyter needs to be installed and to list this projects settings in kernel spec do the following

	$ python -m ipykernel install --user --name=video-semantic-segmentation-network


## Download models and dataset.

#### Models and checkpoints
There are three models that are required to run the inference and all are tensorflow compatable models. The models from the best settings are uploaded on google drive and needs to be downloaded. Following are the download links

1. **resnet50_segnet_model** : [resnet50_segnet_model][] 
2. **dvs_net_flownets_checkpoints** : [dvs_net_flownets_checkpoints][]
3. **decision_network_checkpoints** : [decision_network_checkpoints][]


[resnet50_segnet_model]: https://drive.google.com/file/d/19yNs8osr9x1jTQWhy0MFkLIjQjkyEgeN/view?usp=sharing
[dvs_net_flownets_checkpoints]: https://drive.google.com/file/d/1HkuF0LB105EdprTY-JDpJ7ott4OH-zSt/view?usp=sharing
[decision_network_checkpoints]: https://drive.google.com/file/d/12wzNEj8cS3tWEO-RhsMCs55_RePiyA6S/view?usp=sharing

After downloading the compressed files, unzip them and copy them in to corresponding folders as following.

	$ unzip resnet50_segnet_model.zip -d resnet50_segnet_model_temp
	$ cp -r resnet50_segnet_model_temp/* resnet50_segment_model
	$ rm -rf resnet50_segnet_model_temp
	$ rm resnet50_segnet_model.zip

similarly, for dvs_net_flownets_checkpoints: This is originally from [DVSNet][] (heading: Checkpoint)

	$ unzip dvs_net_flownets_checkpoints.zip -d dvs_net_flownets_checkpoints_temp
	$ cp -r dvs_net_flownets_checkpoints_temp/* dvs_net_flownets_checkpoints
	$ rm -rf dvs_net_flownets_checkpoints_temp
	$ rm dvs_net_flownets_checkpoints.zip

[DVSNet]: https://github.com/XUSean0118/DVSNet/blob/master/README.md

and for decision_network_checkpoints,

	$ unzip decision_network_checkpoints.zip -d decision_network_checkpoints_temp
	$ cp -r decision_network_checkpoints_temp/* decision_network_checkpoints
	$ rm -rf decision_network_checkpoints_temp
	$ rm decision_network_checkpoints.zip


#### datasets

1. Data for training the baseline segmentation network that is resnet50_segnet model. 

Download the dataset from [alexgkendell][]'s  gitbub tutorial. This dataset contains 701 annotated images (367: train, 101: val, 233: test). These images are single frame images and they are used to train segmentation network. More information is provided in the __Training__ section 

[alexgkendell]: https://github.com/alexgkendall/SegNet-Tutorial/tree/master/CamVid


2. Data for training the full network explained in two different steps in __training section__ required following dataset.

The dataset required for this is the same dataset as above but sampled at 30 frames per second. 30th frame is considered as current frame and 1st - 29th frame is considered as key frames. Annotation is provided for the current frame that is the 30th frame.

This dataset can be downloaded from here: [camvid_30_fps][]

[camvid_30_fps]: https://drive.google.com/file/d/12wzNEj8cS3tWEO-RhsMCs55_RePiyA6S/view?usp=sharing

3. Data for evaluation or running the inference

If the dataset from 2. is download then this step is not required. However, for running inference only and getting the **evaluation results** test set needs to be downloaded and this is packaged seperately for convinience and can be downloade from here: [camvid_30_fps_test_only][]

[camvid_30_fps_test_only]: https://drive.google.com/file/d/12wzNEj8cS3tWEO-RhsMCs55_RePiyA6S/view?usp=sharing

4. video input

videos from camvid dataset can be downloaded from. These can be used as input to the inference. More on how to process video inputs in the following sections
1. [seq01TP][] 
2. [seq06R0][]

[seq01TP]: ftp://svr-ftp.eng.cam.ac.uk/pub/eccv/01TP_extract.avi
[seq06R0]: ftp://svr-ftp.eng.cam.ac.uk/pub/eccv/0006R0.MXF



## Running inference


#### How to get evaluation results
#### How to process a video


## Training

There are 2 parts for the training. 
1. Baseline segmentation network
2. Fill training of video-semantic-segmentation-network

### Baseline segmentation network: resnet50_segnet

**Prerequisites**
1. 	CamVid dataset as mentioned in [datasets](#datasets) section bullet point number 1.

Baseline model used in experiments is an encoder-decoder network with resnet50 (pretrained with imagenet) as encoder and segnet as decoder. [resnet50](model/resnet50.py) and [segnet](model/segnet.py) are the encoder and decoder network. These files are written in keras and are place holders here. They are used to load the pretrained resnet50_segnet combined model and to convert keras model from hd5 format to tensorflow protobuf pb format. [convert_keras_to_tensorflow_pb.py](convert_keras_to_tensorflow_pb.py)

Training is ideal if performed on machines with GPU support and following jupyter notebook can be used to train a new model. This notebook is used to generate a baseline model in our experiments and is run on google colab with GPU support.
[resnet50_segnet_training]()

[resnet50_segnet_training]:https://colab.research.google.com/drive/1Rpkg_cBLc0VdIGvUZdWo3FsMHgXlVPdH?usp=sharing

#### what to do with the baseline segmentation network model.

After training a new model with the above jupyter notebook on google colab, the trained model is a keras supported model saved typically 'resnet50_segnet.h5'. This model file is in hd5 format and needs to be converted to protobuf format 'resnet50_segnet.pb'
Do the following

	$ cp resnet50_segnet.h5 ./resnet50_segnet_model/resnet50_segnet.h5
	$ python convert_keras_to_tensorflow_pb.py

This should convert the keras model and saved the protobuf format file as './resnet50_segnet_model/resnet50_segnet.pb'












