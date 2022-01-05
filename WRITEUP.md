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

### Running the submitted code

The notebooks and other code in this submission can be run inside the supplied Docker container. Follow provided instructions in the `build` directory to build and run the Docker container.

Note that when trying to run the "Exploratory Data Analysis" notebook in the Docker container, I encountered an error `AttributeError: module 'pyparsing' has no attribute 'downcaseTokens'`. It appears that the latest pyparsing module is too new (`downcaseTokens` was changed to `downcase_tokens` in version 3.0.0). To remedy this, simply install an older version by running `pip install pyparsing==2.4.2`.

## Dataset

### Dataset analysis

The dataset contains camera images from urban scenes, taken with on-vehicle cameras. There are ~100 tfrecord files, each containing many images.

#### Sample image

A sample image from the dataset (with ground truth labels) is shown below. To see more sample images, run the `Exploratory Data Analysis.ipynb` notebook.

![Sample image from dataset](img/sample_image.png)

#### Observations about the images

It appears that the images are all looking forward, so perhaps they all use the front camera on the vehicle.

Also, some images appear to be very blurry / contain odd artifacts. An example is given below. This image did not contain any labels.

![Image with no labels and artifacts](img/blurry_image.png)

#### Distribution of labels

There are 3 label types, namely vehicles, pedestrians, and cyclists. These labels are not evenly distributed throughout the dataset. In fact, there are many more vehicles in the dataset than pedestrians, and many more pedestrians than cyclists. The following pie chart shows the distribution of labels for 1000 images randomly drawn from the dataset:

![Label distribution pie chart](img/label_dist_pie_chart.png)

The fact that there are very few cyclists, for example, may cause us to have less confidence in our model's ability to detect cyclists.

Another useful data metric is the number of each label type present in images. The following histograms show the number of instances of each label per image for 1000 randomly chosen images in the dataset.

![Histogram of number of vehicle labels per image](img/label_dist_vehicle_hist.png)

![Histogram of number of pedestrian labels per image](img/label_dist_pedestrian_hist.png)

![Histogram of number of cyclist labels per image](img/label_dist_cyclist_hist.png)

From the histograms, it is clear to see that most images contain vehicles, and in fact multiple vehicles. However, most images do not contain pedestrians or cyclists. Very few images contain large numbers of pedestrians, and only a handful of images contain multiple cyclists. It may prove useful to keep this in mind as we continue with training our model.
