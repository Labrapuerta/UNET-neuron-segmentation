# Structure of the scripts

This directory contains the scripts used to generate the data and figures in the paper. The scripts are organized in the following way:

- `data/`: Scripts for generating and preproces the data used in the model.
- `models/`: Scripts for training and evaluating the models.
- `visualization/`: Scripts for visualizing the results and generating figures.
- `utils/`: Utility functions used across the scripts.


# UNET architecture

The UNET architecture is a popular deep learning model for image segmentation tasks. It consists of an encoder-decoder network with skip connections that help preserve spatial information during the upsampling process. The model is composed of two main parts: the encoder, which downsamples the input image to extract features, and the decoder, which upsamples the features to generate the segmentation mask. The skip connections connect corresponding layers in the encoder and decoder, allowing the model to combine low-level and high-level features for accurate segmentation.
