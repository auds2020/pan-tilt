# Pan tilt for Raspberry Pi with audio functionality. 

This project was originally created as a final project for my electronics II class, with the eventual hope it will be integrated into a life-size WALL-E prototype.

Hardware: 
We have a gimbal controlled by two servos, one controlling pan and one tilt. On top of the camera gimbal is a camera, which connects back to the Pi to the built-in camera port. 
We also have a series of maintained switches, which are wired to the Pi's GIPO pins. Finally, a USB microphone is connected for audio input, and audio output is given through the audio jack to a speaker. 

Function:
The Pi should record audio until the record button is released, and play audio until a given play button is released. If multiple play buttons are pressed at once, then the sounds should overlay one another.
