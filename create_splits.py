import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    Note: Since the Udacity workspace already contains files in the 'test' directory, we will only
    create two splits, namely train and val.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # Move files from the source directory to the train and val directories.
    # We will use a fairly standard 80/20 training:validation split.

    # Create a list of input files and randomly shuffle it
    input_files = glob.glob(os.path.join(source, "*.tfrecord"))
    random.shuffle(input_files)

    # Compute the index at which we should split train and val
    training_proportion = 0.8
    N = len(input_files)
    split_index = round(training_proportion * N)

    # Move training files
    for file in input_files[:split_index]:
        name = os.path.basename(file)
        os.rename(file, os.path.join(destination, "train", name))

    # Move validation files
    for file in input_files[split_index:]:
        name = os.path.basename(file)
        os.rename(file, os.path.join(destination, "val", name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
