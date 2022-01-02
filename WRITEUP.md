# Submission - Object Detection in an Urban Environment

## Project overview

The goal of this project is to create a framework that can detect and classify pedestrians, cyclists, and vehicles in visual imagery of real-life on-road scenarios. The visual images come from vehicle-mounted cameras on self driving cars.

The primary use case for this system is autonomous (self driving) cars. These vehicles need to have an accurate understanding of their environment in order to operate safely and avoid collisions. In urban environments, cyclists, pedestrians, and other vehicles are among the most common objects encountered on roads, so it is clearly important to be able to detect them. Additionally, it is important to _classify_ each of these objects, since they move and behave in very different ways.

Besides autonomous driving, one can also imagine other applications where this framework might be useful either by itself or as part of a more complex system:

- As a tool to supplement human drivers in avoiding collisions (e.g. as part of an Advanced Driver-Assistance System)
- Data collection for urban planning. For example, how many cyclists pass through a given intersection over the course of a typical week?
- Any other use case where an understanding of road users is important.

## Setup

### Retrieve the data

Note: These steps should be performed on the host machine (i.e. not in a Docker container)

Rather than using `download_process.py` to download the raw tfrecords and isolate the camera data (which will take a very long time), we'll instead just download the pre-processed data directly from the Udacity Project Workspace for this project. Open the project workspace in a browser and navigate to `/home/workspace` in the left window (should already be there). Right click on `data` and click `Download`. This will download a file called `data.tar.gz` to your `~/Downloads` folder.

Then, on your local machine: From the root of this repo, run `tar -xvf ~/Downloads/data.tar.gz` to extract the data into the workspace. The data will be extracted with the same directory structure as in the project workspace.
