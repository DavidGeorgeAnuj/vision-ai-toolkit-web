vision-ai-toolkit-web
=====================

Description
-----------

**vision-ai-toolkit-web** is the web interface for the **Vision-AI-Toolkit**, enabling real-time **object detection**, **face matching**, and **text recognition** from images and videos. It provides a seamless and intuitive browser-based experience for visual data analysis, making it easier for users to interact with AI-powered tools through a simple web application.

This toolkit integrates several AI components:

-   **Object Detection**: Using the YOLOv8 model to detect objects in real-time through webcam or video input.
-   **Face Matching**: Comparing two images to detect matching faces using a face embedding model.
-   **Text Recognition**: Extracting and recognizing text from images using EasyOCR.

The web-based interface allows users to perform these tasks in a user-friendly environment, offering a convenient and accessible solution for image and video analysis.

Features
--------

-   **Real-time Object Detection**: Use your webcam or upload a video file for real-time object detection powered by YOLOv8.
-   **Face Matching**: Upload two images to compare faces and check for matches.
-   **Text Recognition**: Extract text from uploaded images using EasyOCR.
-   **Browser-based GUI**: A user-friendly web interface built with HTML, CSS, and JavaScript.

Requirements
------------

### Backend

Make sure you have the following Python dependencies installed to run the backend of the application:

bash

Copy

`pip install opencv-python numpy torch easyocr ultralytics Flask`

-   **opencv-python**: For image and video processing (including face matching and object detection).
-   **numpy**: For numerical operations in image processing.
-   **torch**: PyTorch framework required for running YOLOv8.
-   **easyocr**: For optical character recognition (OCR) to extract text from images.
-   **ultralytics**: Contains the YOLOv8 model used for object detection.
-   **Flask**: Lightweight framework to run the web application.

### Frontend

The frontend uses standard **HTML**, **CSS**, and **JavaScript**. You can use libraries such as **Bootstrap** or **Tailwind CSS** to style the interface, depending on your design preferences.

How to Use
----------

### 1\. Clone the Repository

Clone the repository to your local machine:

bash

Copy

`git clone https://github.com/DavidGeorgeAnuj/vision-ai-toolkit-web.git
cd vision-ai-toolkit-web`

### 2\. Install Backend Dependencies

Install the necessary Python dependencies:

bash

Copy

`pip install -r requirements.txt`

### 3\. Run the Web Application

Start the Flask web server:

bash

Copy

`python app.py`

The web application will be available at `http://127.0.0.1:5000/` in your browser.

### 4\. Web Interface

The web interface allows users to:

-   Upload a **video file** or use the **webcam** for real-time object detection.
-   Upload **two images** for face matching and comparison.
-   Upload an **image** to extract text using EasyOCR.

### 5\. View Results

-   For **object detection**, the detected objects will be displayed on the video or webcam feed.
-   For **face matching**, the result will indicate if the faces in the two uploaded images match.
-   For **text recognition**, the recognized text will be extracted and displayed.

Future Work / Enhancements
--------------------------

-   **Advanced Object Detection**: Extend support to detect more object categories or train YOLOv8 on custom datasets.
-   **Real-Time Face Matching**: Implement face matching functionality with live webcam feeds.
-   **Multi-Language OCR**: Enhance text recognition capabilities to support additional languages using EasyOCR's multilingual features.
-   **User Authentication**: Implement user authentication and save data for more personalized experiences.

Contributing
------------

Contributions to **vision-ai-toolkit-web** are welcome! If you'd like to contribute, feel free to open issues or submit pull requests. Please ensure that you follow the existing code style and add tests for any new features.

License
-------

This project is licensed under the MIT License.
