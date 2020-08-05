from __future__ import print_function

import argparse
import os
import sys
import importlib

import tensorflow as tf
import numpy as np


# Root directory of the project
ROOT_DIR = os.path.abspath("../")
sys.path.append(ROOT_DIR)  # To find local version of the library

from model import FlowNets
from tools.img_utils import preprocess
from tools.flow_utils import warp
from tools import inputs

DATA_DIRECTORY = '/data/cityscapes_dataset/cityscape/'
DATA_LIST_PATH = '../list/imagestrain_13_list.txt'
RESTORE_FROM = '../checkpoint/'
SAVE_DIR = './train/'
NUM_CLASSES = 19
NUM_STEPS = 38675 # Number of images in the dataset.
input_size = [1024,2048]
IMG_MEAN = np.array((104.00698793,116.66876762,122.67891434), dtype=np.float32)


def get_arguments():
    """Parse all the arguments provided from the CLI.

    Returns:
      A list of parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Generate Testcases")
    parser.add_argument("--data_dir", type=str, default=DATA_DIRECTORY,
                        help="Path to the directory containing the dataset.")
    parser.add_argument("--data_list", type=str, default=DATA_LIST_PATH,
                        help="Path to the file listing the images in the dataset.")
    parser.add_argument("--restore_from", type=str, default=RESTORE_FROM,
                        help="Where restore model parameters from.")
    parser.add_argument("--save_dir", type=str, default=SAVE_DIR,
                        help="Where to save segmented output.")
    parser.add_argument("--num_steps", type=int, default=NUM_STEPS,
                        help="Number of images in the video.")
    parser.add_argument("--clip", type=float, default=0.0,
                        help="trim extreme confidence score")
    return parser.parse_args()


def main():
    """Create the model and start the evaluation process."""
    args = get_arguments()
    print(args)

    tf.reset_default_graph()
    # Set placeholder
    image1_filename = tf.placeholder(dtype=tf.string)
    image2_filename = tf.placeholder(dtype=tf.string)

    current_output = tf.placeholder(tf.int64, [4, 224, 224])



