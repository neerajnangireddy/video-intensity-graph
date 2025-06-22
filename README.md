# Video Intensity Plot (viplot)
This tools plot the intensity of the pxiels over the timeline of a video.

## How does it work?
1) Takes a video and extact frames from it.
2) Transform each frame to grey scale.
3) sum up all the pixels and divide by the number of pixels.
4) plot the resulting value againt the coresponding frame timestamp.


## Installation and running
### Method 1(using uv)
The easy and recommended way of installing and running.
If you don't have uv already install it from [here](https://docs.astral.sh/uv/getting-started/installation/):
```
git clone https://github.com/neerajnangireddy/video-intensity-graph
cd video-intensity-graph
uv run viplot video.mkv
```

### Method 2(using venv and pip)
```
git clone https://github.com/neerajnangireddy/video-intensity-graph
cd video-intensity-graph
python3 -m venv .venv
source .venv/bin/activate
pip3 install opencv-python plotly
python3 viplot.py video.mkv
```



