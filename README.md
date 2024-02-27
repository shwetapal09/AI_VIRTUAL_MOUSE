# AI VIRTUAL MOUSE
# Virtual Mouse with Hand Gestures 
This repository contains code for a virtual mouse system that allows users to control the mouse cursor and perform click operations using hand gestures captured through a webcam.

# Features:
1.Hand Detection: Utilizes the MediaPipe library to detect hand landmarks in real-time webcam feed.

2.Finger Tracking: Tracks the positions of the index finger and the thumb finger to control the mouse cursor.

3.Click Operations: Performs mouse click operations based on the distance between the index finger and the thumb finger.

4.Visual Feedback: Provides visual feedback by displaying a trail of cursor movement on the screen.

5.Customizable Parameters: Users can adjust parameters such as cursor speed and click sensitivity.

# Dependencies:
1.Python 3.x

2.OpenCV (cv2)

3.MediaPipe

4.PyAutoGUI

5.NumPy

# Usage:
1.Clone the repository to your local machine.

2.Install the required dependencies using pip install -r requirements.txt.

3.Run the virtual_mouse.py script.

4.Use your hand gestures to control the mouse cursor and perform clicks.

# Notes:
1.Ensure that your webcam is properly connected and accessible by the script.

2.Adjust parameters such as hand detection confidence, cursor speed, and click sensitivity as needed for optimal performance.

3.Contributions and feedback are welcome! Feel free to submit issues or pull requests.
