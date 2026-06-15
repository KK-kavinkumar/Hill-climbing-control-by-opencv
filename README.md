# Hill Climb Racing Control Using Hand Gesture Recognition

## Overview

This project enables users to play Hill Climb Racing using hand gestures instead of a keyboard. The system uses a webcam and MediaPipe Hand Tracking to detect finger positions in real time and converts gestures into game controls such as acceleration, braking, cursor movement, and menu selection.

The project demonstrates the application of Computer Vision and Human-Computer Interaction (HCI) for touchless gaming experiences.

---

## Features

* Real-time hand gesture detection
* Touchless game control
* Accelerate using hand gestures
* Brake using hand gestures
* Cursor control using finger tracking
* Menu navigation using gesture-based Enter key
* Webcam-based interaction
* Low-latency gesture recognition

---

## Technologies Used

### Programming Language

* Python

### Computer Vision

* OpenCV
* MediaPipe

### Automation

* PyAutoGUI

### Input Device

* Webcam

---

## Gesture Mapping

| Gesture                     | Action          |
| --------------------------- | --------------- |
| Open Palm (5 Fingers)       | Accelerate      |
| Index Finger Only           | Brake           |
| Index + Middle Finger       | Cursor Movement |
| Closed Hand / Single Finger | Press Enter     |

---

## Working Principle

1. Webcam captures live video.
2. OpenCV processes each frame.
3. MediaPipe detects hand landmarks.
4. Finger positions are analyzed.
5. Specific finger combinations are mapped to actions.
6. PyAutoGUI simulates keyboard and mouse events.
7. Hill Climb Racing responds as if controlled by a physical keyboard.

---

## Project Architecture

```text
Webcam
   ↓
OpenCV Video Capture
   ↓
MediaPipe Hand Detection
   ↓
Gesture Recognition Logic
   ↓
PyAutoGUI Keyboard/Mouse Events
   ↓
Hill Climb Racing Game
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/hill-climb-gesture-control.git
cd hill-climb-gesture-control
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Requirements

### Hardware

* Webcam
* Windows PC/Laptop

### Software

* Python 3.9+
* Hill Climb Racing (PC Version)
* OpenCV
* MediaPipe
* PyAutoGUI

---

## requirements.txt

```text
opencv-python
mediapipe
pyautogui
```

---

## Controls

### Accelerate

Show all five fingers.

```text
Gesture: Open Palm
Action : Right Arrow Key
```

### Brake

Show only the index finger.

```text
Gesture: Index Finger
Action : Left Arrow Key
```

### Cursor Control

Show index and middle fingers.

```text
Gesture: Two Fingers
Action : Mouse Movement
```

### Menu Selection

Close hand or show minimal finger gesture.

```text
Gesture: Closed Hand
Action : Enter Key
```

---

## Applications

* Gesture Controlled Gaming
* Human Computer Interaction
* Computer Vision Learning
* Touchless User Interfaces
* Accessibility Solutions
* AI-Based Control Systems

---

## Future Enhancements

* Multiplayer gesture gaming
* Voice and gesture hybrid control
* Custom gesture training
* Deep learning gesture classification
* Support for multiple games
* Hand tracking analytics dashboard

---

## Results

The system successfully controls Hill Climb Racing using hand gestures with real-time response, eliminating the need for keyboard interaction and providing an immersive touchless gaming experience.

---

## Author

Kavin Kumar S

B.Tech Artificial Intelligence and Data Science

Skills: Computer Vision, Artificial Intelligence, Python, OpenCV, MediaPipe, IoT, Automation, and Machine Learning.

---

## License

This project is developed for educational and research purposes.
