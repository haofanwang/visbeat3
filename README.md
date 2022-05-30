# visbeat3

This is a migration of [visbeat](http://abedavis.com/visualbeat/) from Python2 to Python3. Head over to an example notebook on [Colab](https://colab.research.google.com/drive/1rYyhNtIsICk1osGrHMPr2zISwSIysCpT?usp=sharing)!


## Install

```
$ pip3 install visbeat3
```

## Usage

```
import os
import time

import matplotlib
import matplotlib.pyplot as plt

import numpy as np
import visbeat3 as vb

source_video = vb.PullVideo(name='video', source_location='./data/01.mp4')
source_audio = vb.PullVideo(name='audio', source_location='./data/02.mp4')

synch_video_beat = 0
synch_audio_beat = 0
nbeats = 32

output_path = './result.mp4'

warped = vb.Dancify(source_video=source_video, 
                    target=source_audio.getAudio(), 
                    synch_video_beat=synch_video_beat,
                    synch_audio_beat=synch_audio_beat, 
                    force_recompute=True, 
                    warp_type='quad',
                    nbeats=nbeats, 
                    output_path=output_path)
```

## Used By
[video-bgm-generation](https://github.com/wzk1015/video-bgm-generation): video background music generation.


## Reference
```
@inproceedings{davis2018visual,
  title={Visual rhythm and beat},
  author={Davis, Abe and Agrawala, Maneesh},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops},
  pages={2532--2535},
  year={2018}
}
```
