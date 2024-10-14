---
title: "Birdclef 2024"
author: Philipp
date: 2024-06-08T12:44:19+02:00
draft: false
socialShare: false
toc: true
tags: [project, birdclef, machine learning, ai, deep learning, transformer, cnn]
supressThumbnail: false
thumbnail: feature*
---

You can find the full paper to the project here: [Download the paper](./SS24_AAI_Lab_Report.pdf)

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

# ResNeXt-50: A Big Leap

Now we get a little more modern...

We then tried ResNeXt-50, which incorporates the concept of "cardinality" by performing multiple transformations in parallel.

### Training Setup:

- Hyperparameter Tuning: Performed using Optuna.
- Epochs: 5 (early stopping applied)
- Learning Rate: 0.0001
- Batch Size: 64

### Results:

- Training Loss: 0.2433
- Validation Loss: 1.3121
- Validation Accuracy: 75.11%
- Validation AUC: 0.9880

This model outperformed all previous approaches in both accuracy and AUC. The use of Optuna for hyperparameter tuning proved highly beneficial in optimizing the model’s performance.

# A Failed Attempt: Audio Spectrogram Transformer (AST)

As part of our exploration of cutting-edge models, we experimented with the **Audio Spectrogram Transformer (AST)**. This model processes raw audio directly, bypassing the need to convert audio into spectrogram images, theoretically allowing the model to learn features directly from the audio waveforms.

Our reasoning was that this approach could potentially outperform traditional CNN-based methods that rely on spectrogram images, especially when dealing with complex, noisy data like bird calls in natural environments. The AST, having been pre-trained on AudioSet, seemed like a promising candidate for transfer learning in this domain.

### The Setup

We initially faced issues with the .ogg file format and the 32 kHz sampling rate, as the AST model expects raw audio inputs in a different format (16 kHz). To resolve this, we employed SoX and PyDub to convert and resample the audio files. After several preprocessing attempts, we managed to create the appropriate inputs for the AST model.

However, that was just the beginning of the difficulties. Upon running the model, we encountered the following cryptic error:

```vbnet
AssertionError: choose a window size 400 that is [2, 1]
```

Despite consulting the model’s documentation and even reaching out to the author on GitHub, it took multiple iterations to identify the problem: we were using the wrong feature extractor. Initially, we were working with the AST feature extractor:

```python
feature_extractor = ASTFeatureExtractor.from_pretrained(model_name)
```

After trial and error, we switched to the Wav2Vec2FeatureExtractor, which was more appropriate for our audio input:

```python
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(model_name)
```

### The Outcome

Switching the feature extractor fixed the initial issue, but more errors followed. Each fix led to another hurdle, with error messages that were poorly documented and difficult to troubleshoot. These issues ranged from training crashes to input size mismatches. Given the tight competition deadlines and the lack of sufficient community support for AST, we reluctantly decided to abandon this approach.

While the AST model holds significant potential for audio classification tasks, the implementation difficulties in our case, combined with the limited time for the competition, made it infeasible. It was a stark reminder of how early-stage models, no matter how promising, can often pose significant risks in terms of implementation time and troubleshooting.

# Challenges and Lessons Learned

This project, like many in machine learning, presented several challenges that were both technical and strategic. One of the biggest hurdles was dealing with the sheer size and complexity of the dataset. Preprocessing 30 GB of audio files into spectrograms was computationally expensive, and our initial attempts took nearly 48 hours for a single attempt. Although we were able to reduce this to just over an hour through parallelization, it highlighted the importance of efficient data pipelines in large-scale machine learning projects. The lesson here is that investing time early in optimizing preprocessing steps can save significant time later on.

Another challenge was managing the models’ performance, particularly with older architectures like ResNet-18 and Inception v3. While these models provided moderate improvements, they were outclassed by newer architectures like ResNeXt-50. This drove home the importance of staying up to date with the latest model architectures in deep learning, as newer models often have built-in optimizations that improve performance with less tuning.

The failed attempt with AST also underscored the risk of diving into cutting-edge models without a deep understanding of their requirements. While AST promised better performance by working directly with raw audio, the technical issues and cryptic error messages made it clear that newer models often come with undocumented pitfalls, especially when the community support is limited.

Lastly, a key strategic challenge was managing our time and focus. Initially, we experimented widely with different architectures, which spread our efforts too thin. In hindsight, narrowing down our approach earlier and dedicating more time to fine-tuning a select few models (e.g., ResNeXt-50) could have yielded even better results. Balancing exploration with a focused strategy is a critical skill in research.

# Future Work

Moving forward, we see several opportunities to build on the progress made in this project. One clear direction is to further explore transformer-based models for audio processing. While our attempt with AST failed due to technical issues, transformers still hold significant promise. Their ability to process raw audio directly could lead to improvements in both training efficiency and classification accuracy, especially as these models evolve and more resources become available.

We also plan to incorporate more advanced validation techniques, such as k-fold cross-validation. Our current validation strategy, which involved splitting the data into training and validation sets, could be improved to give a more reliable measure of model performance. K-fold cross-validation would ensure that our models are tested on multiple subsets of the data, reducing the risk of overfitting and providing a more robust evaluation.

In addition, we’re interested in exploring ways to improve the preprocessing pipeline further. While our parallelized approach significantly reduced processing time, there may be room for additional optimizations, such as experimenting with different spectrogram generation techniques or leveraging GPU-based preprocessing. Faster, more efficient preprocessing will be essential as we scale to larger datasets.

Lastly, engaging more actively with the machine learning community, especially on platforms like Kaggle, could provide new insights and collaborations. Community engagement was an area where we missed out during this project, and it’s clear that tapping into collective knowledge early on could accelerate progress, particularly when dealing with new architectures or troubleshooting errors.
