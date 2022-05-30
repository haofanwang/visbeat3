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