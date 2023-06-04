# VideoSmooth: Creating Visual Effects with AI

## Overview

This project demonstrates how artificial intelligence (AI), specifically using the ChatGPT model, can be used to create unique visual effects for videos.

The project includes a Python script, `videosmooth.py`, which uses AI to create a smoothing effect (or an ND filter effect) in a video. This script was automatically generated by the ChatGPT model and then edited for usability and readability.

We also provide `initial_code.py` as an example of the initial code that was generated by ChatGPT in the process of creating `videosmooth.py`.

## How to Use

1. Clone this repository (or just download videosmooth.py).
2. Install any necessary dependencies. (You'll need Python and OpenCV and numpy libraries)
3. Run `videosmooth.py` with your video as the input file.

## exaples
in command line:
python videosmooth.py IMG_2871.MOV output7.mp4 average7.jpg --start_time 5 --end_time 10 --smooth_window 10

Define start time and end time in seconds, smooth_window in frames
(default mooth window: --smooth_window 30)

You can skip --start_time, --end_time,  --smooth_window,
so you can use this command:
python videosmooth.py IMG_2871.MOV output7.mp4 average7.jpg


For more detailed information on how to use this project and how we created it, check out our YouTube video: [[Link to video](https://youtu.be/irbQvHwpYC0)](#)

## License

This project is provided under the MIT license, allowing free use, distribution, and modification of the code.

## Contact

If you have any questions or suggestions, please don't hesitate to get in touch.

Thank you for your interest in our project!
