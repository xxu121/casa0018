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

Experiment no	Processing block	Learning Block	Processed features	Learning rate	Number of training cycles	Data augmentation 	Neural network architecture	Coefficient 	neurons	Dropout rate	Training ACCURACY (%)	Model Testing accuracy (%)	Loss
1	MFE	Transfer Learning	3960	0.01	100	No	MobileNetV1 0.1	0.98	128	0.1	94.2	95.06	0.36
2	MFCC	Transfer Learning	650	0.01	100	No	MobileNetV1 0.1	0.98	128	0.1	Failed	Failed 	Failed
3	Spectrogram	Transfer Learning	6435	0.01	100	No	MobileNetV1 0.1	0.98	128	0.1	Failed 	Failed 	Failed 
4	MFE	Classification	3960	0.005	100	No	Reshape layer (13 columns), 1D conv, Flatten layer	0.98	8,16	0.25	Failed	Failed 	Failed
5	MFCC	Classification	650	0.005	100	No	Reshape layer (13 columns), 1D conv, Flatten layer	0.98	8, 16	0.25	88.5	90.74	0.45
6	Spectrogram	Classification	6435	0.005	100	No	Reshape layer (13 columns), 1D conv, Flatten layer	0.98	8, 16	0.25	59.5	3.70	0.88<img width="1376" alt="image" src="https://github.com/xxu121/casa0018/assets/146341729/f15c8afb-caff-4d02-aea1-2a345e16f0ff">

