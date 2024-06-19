---
title: "Birdclef 2024"
author: Philipp
date: 2024-06-08T12:44:19+02:00
draft: true
socialShare: false
toc: true
tags: [project, birdclef, machine learning, ai, deep learning, transformer, cnn]
supressThumbnail: false
thumbnail: feature*
---

# The Challenge

Kaggle's BirdCLEF2024 competition challenges participants to identify bird species from audio recordings collected globally. Utilizing extensive datasets and advanced machine learning techniques, the goal is to enhance automated bird sound recognition. This competition not only aids in biodiversity monitoring but also supports conservation efforts by improving tools for ecologists and ornithologists.

For more detailed information, check out the [BirdCLEF 2024 competition page](https://www.kaggle.com/competitions/birdclef-2024).

# Background

This project is conducted as part of the Applied Artificial Intelligence Lab seminar at the University of Passau.

Focusing on the development of a robust AI model for bird classification, the project includes regular progress presentations, team discussions, and collaborative work on a shared repository.

The team comprises [Spencer Apeadjei-Duodu](https://www.linkedin.com/in/adkspence/) and myself. Our aim is to advance AI capabilities in ornithology, contributing to broader ecological studies and conservation initiatives. Regular updates and team interactions ensure consistent progress and innovation throughout the project duration.

# The Start

First, we examined the data.
30 GB of audio files labeled and sorted into their respective folders.
Our initial idea was to use a custom CNN. For this, we wanted to convert the audio files into spectrogram images and train our CNN on them.

Good preprocessing was essential for this. We divided the audio files into 5-second chunks and applied various audio filters to them. Spectrogram images were then created from the audio chunks and saved as PNG files in the same labeled folder structure.

```python
{{% include "preprocess.py" %}}
```

The first pipeline consisted of:

- High pass filter
- Noise reduction
- Normalization
- Segmentation
- Spectrogram images

This took an extremely long time. Approximately 48 hours for the entire dataset. And if something didn't work or if we wanted to fine-tune something, we would have to do it all over again. We then searched for better filtering methods and used better libraries.

The second pipeline was more refined:

- We removed the high pass filter and instead cut the spectrogram image below 2kHz.
- We used the library [noisereduce](https://pypi.org/project/noisereduce/) as the noise filter.
- Then we directly segmented and generated spectrogram images. The images were exported as squares and monochrome color. This ensures better compatibility with our models.

As a cherry on top, the pipeline was parallelized.
All of this reduced the preprocessing time from 48 hours to 1 hour and 10 minutes.

This is what I would consider as the first success.

# The first model

We tried to implement it in [tensorflow](https://www.tensorflow.org/).
Unfortunately, we encountered errors on the AI server provided to us.
That's why we switched to [PyTorch](https://pytorch.org/).
This was much easier to handle.

The model itself was nothing special.
Just a few convolutional, pooling and linear layers.

```python
class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(128 * 16 * 16, 256)
        self.fc2 = nn.Linear(256, num_classes)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 16 * 16)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
```

We just reached 48% accuracy with that.
So we tried something else.

# ResNet18

Was one of the less good decisions and the time would probably have been better invested elsewhere. But we see our project as a process in which you simply try out freely in all directions and see what comes out of it.

[ResNet18](https://pytorch.org/vision/master/models/generated/torchvision.models.resnet18.html) is unfortunately a somewhat older model that has now been replaced by faster and better models. It is a pretraind CNN model.

It has severall advantages:

- Can directly be applied to the Spectrogram images
- Fast training time
- Good at extracting features

The initialization of the model is super easy for that:

```python
def create_spectrogram_model(num_classes):
    model = models.resnet18(pretrained=True)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, num_classes)
    model = model.to(device)
    return model
```

### The Hyperparameters:

- Batch size = 64
- Epochs = 5
- Learning rate = 0.0001

### The Performance:

- TrainLoss: 1.42
- ValLoss: 1.58
- ValAcc: 63.40%

# Inception_v3

Next, we tried [Inception_v3](https://pytorch.org/hub/pytorch_vision_inception_v3/).
Also a pretrained CNN model with all it's advantages and disadvantages.
Inception_v3 is also an older model, which you can see in the results.

The initialization is also as easy as it gets:

```python
inception = models.inception_v3(pretrained=True)
```

This model gave us a slightly better performance:

### Hyperparameters:

- Learning Rate: 0.001
- Batch Size: 32
- Optimizer: Adam
- Loss Function: Cross-Entropy Loss
- Epochs: 20

### Performance:

- Training Loss: 0.2660
- Validation Loss: 1.5370
- Validation Accuracy: 73.84%

# Now we get a little more modern
