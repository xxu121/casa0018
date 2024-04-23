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


![image](https://github.com/xxu121/casa0018/assets/146341729/ac9e2c0f-e0eb-4f60-b9b1-45d719010f4c)


Figure 1: The components of language classification application

## Data


In Edge Impulse, the dataset consists of recordings from various individuals saying "deep learning" in both English and Chinese. Each recording is 30 seconds long, and every phrase within these recordings has been segmented into 1-second slices, with low-quality segments removed. Noise samples were recorded in a classroom setting, while additional natural noises were sourced from Edge Impulse’s (Impulse, 2024) resources. 

	Training	Testing	Total
Chinese	238	55	293
English 	289	66	355
Noise	93	24	117
%	80	20	<img width="485" alt="image" src="https://github.com/xxu121/casa0018/assets/146341729/b7c72031-527a-4dcd-b1ee-652ffb00d67a">

## Dataset preparing


The dataset consists of a 15-second audio clip labelled English with the phrase ‘deep learning’ repeated throughout the clip, with pauses between each phrase.


The 15-second audio was divided into several shorter clips, each containing a complete utterance of 'deep learning'. Samples that are unclear due to background noise or incomplete phrases were identified and removed from the dataset. 


![image](https://github.com/xxu121/casa0018/assets/146341729/40850fcb-e683-47bd-8e65-3c883861bcdd)

Figure 2: example of speaking deep learning


![image](https://github.com/xxu121/casa0018/assets/146341729/d7f87181-14f6-493a-9b75-2fd8b9430610)

Figure 3: 1s sample of English
