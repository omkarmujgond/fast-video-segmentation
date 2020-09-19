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


## Download models and dataset.





