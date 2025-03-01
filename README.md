# Vision-AI-Toolkit-Web

## Description

**Vision-AI-Toolkit-Web** is the web interface for the **Vision-AI-Toolkit**, enabling real-time **object detection**, **face matching**, and **text recognition** from images and videos. It provides a seamless and intuitive browser-based experience for visual data analysis, making it easier for users to interact with AI-powered tools through a simple web application.

### Key Features:

- **Object Detection**: Uses the YOLOv8 model for real-time object detection via webcam or video input.
- **Face Matching**: Compares two images to identify matching faces using a face embedding model.
- **Text Recognition**: Extracts and recognizes text from images using EasyOCR.
- **Browser-based GUI**: A user-friendly web interface built with HTML, CSS, and JavaScript.

## Requirements

### Backend Dependencies

Ensure you have the following Python dependencies installed to run the backend:

```bash
pip install opencv-python numpy torch easyocr ultralytics Flask
```

- **opencv-python**: For image and video processing (including face matching and object detection).
- **numpy**: For numerical operations in image processing.
- **torch**: Required for running YOLOv8.
- **easyocr**: For optical character recognition (OCR) to extract text from images.
- **ultralytics**: Contains the YOLOv8 model for object detection.
- **Flask**: A lightweight framework to run the web application.

### Frontend Technologies

The frontend uses standard **HTML**, **CSS**, and **JavaScript**. You can utilize libraries such as **Bootstrap** or **Tailwind CSS** for styling, based on your design preferences.

## How to Use

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/DavidGeorgeAnuj/vision-ai-toolkit-web.git
cd vision-ai-toolkit-web
```

### 2. Install Backend Dependencies

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Web Application

Start the Flask web server:

```bash
python app.py
```

The web application will be available at `http://127.0.0.1:5000/` in your browser.

### 4. Web Interface Functionality

- **Real-time Object Detection**: Upload a **video file** or use the **webcam** for live object detection.
- **Face Matching**: Upload **two images** to compare faces.
- **Text Recognition**: Upload an **image** to extract text using EasyOCR.

### 5. Viewing Results

- **Object Detection**: Detected objects will be highlighted in the video or webcam feed.
- **Face Matching**: The system will indicate if the uploaded faces match.
- **Text Recognition**: Extracted text will be displayed in the interface.

## Future Enhancements

- **Advanced Object Detection**: Support for detecting additional object categories or training YOLOv8 on custom datasets.
- **Real-Time Face Matching**: Implement live face matching using webcam feeds.
- **Multi-Language OCR**: Enhance text recognition to support multiple languages via EasyOCR.
- **User Authentication**: Add authentication and data storage for personalized experiences.

## Contributing

Contributions are welcome! If you'd like to contribute, feel free to open issues or submit pull requests. Please follow the existing code style and add tests for any new features.

## License

This project is licensed under the **MIT License**.

