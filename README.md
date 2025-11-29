# Python Screen Recorder

This project is a basic Python screen recorder that captures the entire desktop screen and saves it as an MP4 video. It continuously takes screenshots of the screen, converts them into video frames, and writes them into a video file.

## Features

* Records full screen
* Automatically detects screen resolution
* Stores the output as an MP4 video
* Press the "s" key anytime to stop recording

## Libraries Used

### 1. **OpenCV (cv2)**

Used for creating the video writer and saving frames into a video file.

### 2. **PyAutoGUI**

Used to capture screenshots of the screen at each frame.

### 3. **NumPy**

Converts screenshots (images) into arrays that OpenCV can process.

### 4. **Keyboard**

Used to detect keyboard key presses, specifically to stop recording.

### 5. **pywin32 (win32api)**

Used to get the system screen width and height so the video matches the actual resolution.

## How It Works

1. The program asks for a filename.
2. It detects screen size using GetSystemMetrics.
3. It sets up OpenCV’s VideoWriter with the correct resolution and frame rate.
4. In a loop:

   * Takes a screenshot using PyAutoGUI
   * Converts it to a NumPy array
   * Converts the color format to OpenCV format
   * Writes the frame to the video
5. When the user presses the "s" key, the loop breaks and the video file is saved.
