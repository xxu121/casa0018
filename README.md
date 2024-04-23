# Audio-based Chinese-English differentiation using deep learning

Xincen Xu, 


link to github rep:  


link to Edge Impulse projects: [https://studio.edgeimpulse.com/studio/362922](https://studio.edgeimpulse.com/studio/362922) 


## Introduction

The project employs the convenience of audio recognition to simplify the language selection process, especially for "deep learning" in English and "deep learning” (深度学习) in Chinese. Its originality lies in the ease of switching between languages using audio input, eliminating the tedious step of manually selecting the preferred language in the user's voice-activated system. By focusing on these specific phrases, the project directly solves the annoyance users face when interacting with multilingual applications, making the experience more seamless and intuitive.


Neural Machine Translation (NMT) is a more advanced type of automatic language translation that solves many of the problems found in older systems. Unlike older methods that translated sentence fragments separately, NMT looks at the entire sentence at once, resulting in better translation results. Compared to Google's old system, NMT has a 60 per cent lower error rate, showing that it is a big step forward in improving the accuracy and comprehensibility of translations(Sakti and Utiyama, 2017).


The project's LED indicator lights up in a specific colour to show whether the language spoken is English or Chinese. This quick visual feedback makes it easy for the user to see what language is being detected, providing a simple and efficient way to enhance the user experience for voice-controlled systems.


## Research Question


Can the system recognise whether a phrase is Chinese or English using only a specific simple expression?


Furthermore, can it recognise other words in the same language without explicit training?

## Application Overview


The project began by creating an audio dataset that included English labels for recording different people saying "deep learning" and Chinese labels for recording "deep learning" (in Chinese, "深度学习"). It also includes importing and recording various noises from the lab and natural environments to enrich the dataset.


To identify the most effective model for distinguishing between languages, the project experiments with various Digital Signal Processing (DSP) blocks, learning blocks, parameter settings, and model architectures. The results of these experiments are systematically organised and presented in a table for comparison.


The best performing model is built onto the Arduino Nano board, which monitors the sound. Built-in LEDs (red, green, and blue) on the board indicate the language being spoken. (Situnayake, 2020)


![image](https://github.com/xxu121/casa0018/assets/146341729/d27e5b69-9358-49c0-8d6f-ac01566c50b6)


Figure 1: The components of language classification application

## Data


In Edge Impulse, the dataset consists of recordings from various individuals saying "deep learning" in both English and Chinese. Each recording is 30 seconds long, and every phrase within these recordings has been segmented into 1-second slices, with low-quality segments removed. Noise samples were recorded in a classroom setting, while additional natural noises were sourced from Edge Impulse’s (Impulse, 2024) resources. 


<img width="607" alt="image" src="https://github.com/xxu121/casa0018/assets/146341729/311154ec-ac1f-46c0-986d-0bc50b9a9147">


Table 1: amount of training and testing data



## Dataset preparing


The dataset consists of a 15-second audio clip labelled English with the phrase ‘deep learning’ repeated throughout the clip, with pauses between each phrase.


The 15-second audio was divided into several shorter clips, each containing a complete utterance of 'deep learning'. Samples that are unclear due to background noise or incomplete phrases were identified and removed from the dataset. 


![image](https://github.com/xxu121/casa0018/assets/146341729/72a73b7a-afbd-42f9-8ca4-20855f6d7dc9)


Figure 2: example of speaking deep learning


![image](https://github.com/xxu121/casa0018/assets/146341729/adac1818-e8d2-44a2-9dce-2d6a009b8a36)


Figure 3: 1s sample of English



The lengths of the dataset's audio clips range from 1 second to 2 seconds, reflecting the varying speeds at which different people speak. These differences in length are taken into account without making any modifications to the clips.



The machine learning model has been trained to recognise and learn the distinct characteristics of Chinese and English from this large dataset, which includes diverse manners of speech. Due to the significant differences between Chinese and English, the model can accurately differentiate between these two languages.

![image](https://github.com/xxu121/casa0018/assets/146341729/393b6d42-f9ab-4a73-b77e-5fe203590201)


Figure 4: samples with different speaking speed


## Model
In Edge Impulse, the main processing modules used to train the audio data include spectrograms, MFCC, and MFE. MFE and spectrograms are great for non-speech audio analysis, while MFCC is the primary processing module because it effectively captures the nuances of human speech. MFE and spectrograms are used to show how their training results differ from those of MFCC, thus highlighting the advantages of MFCC in speech audio processing. Also, two main types of learning are used: classification, which splits the audio into languages, and transfer learning, which improves the results by using models trained on similar tasks.

| Experiment no | Processing block | Learning Block | Processed features | Learning rate | Number of training cycles | Data augmentation | Neural network architecture | Coefficient | Neurons | Dropout rate | Training ACCURACY (%) | Model Testing accuracy (%) | Loss |
|---------------|------------------|----------------|--------------------|---------------|--------------------------|-------------------|-----------------------------|-------------|---------|--------------|------------------------|-----------------------------|------|
| 1             | MFE              | Transfer Learning | 3960               | 0.01          | 100                      | No                | MobileNetV1 0.1             | 0.98        | 128     | 0.1          | 94.2                   | 95.06                       | 0.36 |
| 2             | MFCC             | Transfer Learning | 650                | 0.01          | 100                      | No                | MobileNetV1 0.1             | 0.98        | 128     | 0.1          | Failed                 | Failed                      | Failed |
| 3             | Spectrogram      | Transfer Learning | 6435               | 0.01          | 100                      | No                | MobileNetV1 0.1             | 0.98        | 128     | 0.1          | Failed                 | Failed                      | Failed |
| 4             | MFE              | Classification   | 3960               | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer | 0.98        | 8, 16   | 0.25         | Failed                 | Failed                      | Failed |
| 5             | MFCC             | Classification   | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer | 0.98        | 8, 16   | 0.25         | 88.5                   | 90.74                       | 0.45 |
| 6             | Spectrogram      | Classification   | 6435               | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer | 0.98        | 8, 16   | 0.25         | 59.5                   | 3.70                        | 0.88 |


Table 2: Result under different learning block

## Experiments


During the course of the experiments, various parameters were tuned to see how they affected the model. These adaptations included learning rate, number of training cycles, remodelling layer structure, number of neurons and dropout rate. The aim was to compare the training accuracy, testing accuracy and loss under each set of parameters to find the best combination.
Experiments 7 to 11 indicate that increasing the number of training cycles does not have a significant impact on the results of the project.
Experiments 10 and 11 indicate that a 13-column remodelling layer works better than a 65-column remodelling layer.
Experiments 10 to 16 explored various neuron configurations and showed that a setup with 256 neurons in each of the two layers performed best.
Experiments that removed the flat layer failed to produce satisfactory results.
Experiment 17 improved the learning rate from 0.005 to 0.05, but the accuracy was significantly lower.
Experiment 18 demonstrate the result under 2D conv.


## Results and Observations

Experiment 15 is the best choice. It had the highest model test accuracy of 91.98%, which is essential to ensure good model performance. The training accuracy was also 96.9% with a low loss rate of 0.32, showing good predictive performance. The bilayer structure with 256 neurons seems to provide the right amount of complexity to capture audio without overfitting, making Experiment 15 the best model for the audio language classification task.

| Experiment no | Processing block | Learning Block         | Processed features | Learning rate | Number of training cycles | Data augmentation | Neural network architecture                                    | Coefficient | Neurons     | Dropout rate | Training ACCURACY (%) | Model Testing accuracy (%) | Loss |
|---------------|------------------|------------------------|--------------------|---------------|--------------------------|-------------------|-----------------------------------------------------------------|-------------|-------------|--------------|------------------------|-----------------------------|------|
| 7             | MFCC             | Classification & k-means | 650                | 0.005         | 100                      | No                | Reshape layer (65 columns), 1D conv, Flatten layer              | 0.98        | 8, 16       | 0.25         | 95.4                   | 90.74                       | 0.16 |
| 8             | MFCC             | Classification         | 650                | 0.005         | 200                      | No                | Reshape layer (65 columns), 1D conv, Flatten layer              | 0.98        | 8, 16       | 0.25         | 88.5                   | 90.74                       | 0.45 |
| 9             | MFCC             | Classification         | 650                | 0.005         | 500                      | No                | Reshape layer (65 columns), 1D conv, Flatten layer              | 0.98        | 8, 16       | 0.25         | 88.5                   | 90.74                       | 0.45 |
| 10            | MFCC             | Classification         | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer              | 0.98        | 8, 16       | 0.25         | 95.4                   | 90.74                       | 0.12 |
| 11            | MFCC             | Classification         | 650                | 0.005         | 200                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer              | 0.98        | 8, 16       | 0.25         | 95.4                   | 90.74                       | 0.12 |
| 12            | MFCC             | Classification         | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer              | 0.98        | 8, 256      | 0.25         | 96.9                   | 90.74                       | 0.58 |
| 13            | MFCC             | Classification         | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer              | 0.98        | 8, 256      | 0.05         | 92.4                   | 90.74                       | 0.47 |
| 14            | MFCC             | Classification         | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer              | 0.98        | 8           | 0.05         | 85.5                   | 75.31                       | 0.83 |
| 15            | MFCC             | Classification         | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer              | 0.98        | 256, 256    | 0.25         | 96.9                   | 91.98                       | 0.32 |
| 16            | MFCC             | Classification         | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 1D conv                            | 0.98        | 256, 256    | 0.25         | Failed                 | Failed                      | Failed |
| 17            | MFCC             | Classification         | 650                | 0.05          | 100                      | No                | Reshape layer (13 columns), 1D conv, Flatten layer              | 0.98        | 256, 256    | 0.25         | 45.8                   | 0                           | 0.47 |
| 18            | MFCC             | Classification         | 650                | 0.005         | 100                      | No                | Reshape layer (13 columns), 2D conv, Flatten layer              | 0.98        | 256, 256    | 0.25         | 94.7                   | 87.04                       | 0.19 |

Table 3: Result under different parameters

The best model used a learning rate of 0.005 and a simple network design with a reshape layer, a convolutional layer, and a flatten layer. It had two sets of 256 neurons each and used a dropout rate of 0.25.


![image](https://github.com/xxu121/casa0018/assets/146341729/7a04896b-e29f-4a37-b046-ddd50dc6772c)


Figure 5: Accuracy and loss of the best training model


The model is about 88% sure when it identifies English speech and similarly confident when it hears noise. The inaccuracies in distinguishing English speech from noise suggest that the model sometimes confuses the two. 


![image](https://github.com/xxu121/casa0018/assets/146341729/ce1d7021-6707-4ef9-8907-b13c411635d3)


Figure 6: Accuracy of the best model testing result


## Observations

In this case, training the model more than 100 times didn't make it any better at recognising sounds. It seems that after 100 training sessions, the model has learnt everything it can.


The 13-column reshaping layer may provide a more optimised configuration than the 15-column reshaping layer, allowing the model to understand and differentiate between audio signals effectively. So 13-column reshaping layer provide more accuracy result.

 
The 256,256 neuron configuration performs best in terms of model complexity and learning capacity, and therefore excels in audio classification.


Improvements to the model included removing uncertain audio samples to clean up the dataset, and adjusting the model's settings during testing to identify configurations that would improve accuracy.


When deploying the model to a physical device, the achieved accuracy often falls short of the theoretical values. This discrepancy becomes more evident when distinguishing between Chinese and English, leading to confusion. Furthermore, without specific training, the model struggles to recognize words beyond the ones it has been trained on, both in Chinese and English.


## Future improvement 


Expanding the dataset to cover more Chinese and English words helps the model to better recognise any word in both languages.


Adjust the settings while training the model.


Link the language recognition output to a translation app, enabling the app to identify the heard language and translate it into the user's preferred language.


## Bibliography

1. IMPULSE, E. 2024. Responding to your voice - TI LaunchXL [Online]. Available: https://docs.edgeimpulse.com/docs/run-inference/hardware-specific-tutorials/responding-to-your-voice-ti#id-3.-building-your-dataset [Accessed].
2. SAKTI, S. & UTIYAMA, M. 2017. International Workshop on Spoken Language Translation.
SITUNAYAKE, P. W. A. D. 2020. TinyML.

