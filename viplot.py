# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "opencv-python",
#     "plotly",
# ]
# ///


import time
import sys
import cv2 as cv
import plotly.graph_objs as go
from pathlib import Path
from time import strftime, gmtime

def process_video(filename: str | Path):
    """Process video to compute summed pixel values of each frame."""
    cap = cv.VideoCapture(filename)
    total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    print(f"Total Frame Count: {total_frames}")
    frame_count = 0
    intensities = []
    timestamps = []

    while cap.isOpened() and frame_count < total_frames:
        ret, frame = cap.read()
        if not ret:
            print("Couldn't read frame. (Exiting...)")
            sys.exit(71)
        timestamp = cap.get(cv.CAP_PROP_POS_MSEC) / 1000 # We need in seconds
        # Convert RGB to Grey Scale for the sake of easy computations
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Sum the pixel values of the frame
        n, m = frame.shape
        intensity = (frame.sum() // (n * m))
        intensities.append(intensity)
        frame_count += 1
        intensities.append(intensity)
        timestamps.append(timestamp)
    cap.release()
    return timestamps, intensities

def plot_graph(timestamps, intensities):
    # Convert timestamps to formatted strings
    hover_labels = [strftime("%H:%M:%S", gmtime(timestamp)) for timestamp in timestamps]
    
    # Create a plotly figure with custom hover template
    fig = go.Figure(data=go.Scatter(
        x=timestamps,
        y=intensities,
        fill="tozeroy",
        mode='lines',
        hovertemplate='<b>Time:</b> %{customdata}<br><b>Intensity:</b> %{y}<extra></extra>',
        customdata=hover_labels
    ))

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Intensity",
        title="Video Intensitiy graph"
    ) 
    fig.show()

def main():
    """Main entry point of the script."""
    if len(sys.argv) < 2:
        print("Argument filename is required.")
        sys.exit(69)

    filename = sys.argv[1]
    filename = Path(filename)

    if not filename.is_file():
        print("File doesn't exist.")
        sys.exit(70)

    stime = time.perf_counter()
    timestamps, intensities = process_video(filename)
    etime = time.perf_counter()
    print(f"Processing finished in {etime - stime:.3f} seconds.")
    plot_graph(timestamps, intensities)

if __name__ == "__main__":
    main()

