# fire_detection_webcam
detect the fire by opencv using webcam
# Fire Detection Program

This is a program developed by Osama Alkhalid for detecting fire in a video stream using computer vision techniques. The program uses the OpenCV library for image processing and the Pygame library for audio playback.

## Requirements

To run this program, you need to have the following:

- Python 3.x
- OpenCV library (`opencv-python`)
- Pygame library (`pygame`)

You can install the required libraries using `pip`:<br>
<h3>pip install opencv-python</h3><br>

<h3>pip install pygame</h3><br>


## Usage

1. Clone the repository or download the source code files to your local machine.
2. Make sure you have the `fire_detection.xml` file, which is the cascade classifier for detecting fire. Place it in the same directory as the program files.
3. Prepare the audio file you want to play when fire is detected. Make sure it is in a compatible audio format (e.g., WAV).
4. Replace `'audio.mp3'` in the code with the path to your audio file.
5. Open a terminal or command prompt and navigate to the directory where the program files are located.
6. Run the program using the following command:


7. The program will open a video stream from the default camera. It will continuously analyze the frames and detect fire using the cascade classifier.
8. When fire is detected, it will print a message "Fire is detected" and play the audio file you specified.
9. To exit the program, press the 'q' key.

Note: The program assumes that your default camera is accessible with index 0. If you have multiple cameras or a different camera index, you can modify the code to use the appropriate camera index.

Feel free to customize and adapt the code to suit your specific requirements.
python main.py


## License

This program is released under the MIT License.

Please acknowledge the author, Osama Alkhalid, if you use or modify this program.

And here's the code for main.py:



