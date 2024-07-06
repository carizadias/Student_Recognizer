# AI_Student_Recognizer
This is a seminar final project baking..
# Real-Time Student Classification System with Transfer Learning

## Project Description

This project was developed as part of the Artificial Intelligence Seminar at the University of Mindelo. The objective is to create a facial recognition system that identifies whether an image contains the student Cariza or not, using Transfer Learning with the EfficientNetB0 model. The project includes an interactive website developed with Flask, allowing real-time detection using OpenCV.

## Project Structure

- `dataset/`: Contains the training and validation images.
  - `train/`
  - `validation/`
- `model/`: Contains the trained model.
- `app/`: Contains the Flask application code.
  - `templates/`: Contains HTML templates.
  - `static/`: Contains static files like CSS and JS.
  - `app.py`: Main script of the Flask application.
- `notebooks/`: Contains Jupyter notebooks used for model development and training.
- `README.md`: Project description.

## Prerequisites

- Python 3.9+
- TensorFlow
- Keras
- Flask
- OpenCV
- Google Colab (optional for model training)
- Google Drive (for data and model storage)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/carizadias/AI_Student_Recognizer.git
   cd AI_Student_Recognizer
   ```
2. Create a virtual environment and install dependencies:

   ```bash
    python3 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
   ```

3. Start the Flask application:
   ```bash
     venv\Scripts\activate
     python app.py
   ```
5. Access the website in your browser at http://127.0.0.1:5000(apear's on the terminal).
   
7. Model training was performed on Google Colab. Follow the steps below to retrain the model:
   - Access the Jupyter notebook on Google Colab.
   - Configure the training and validation directories on Google Drive.
   - Run the notebook cells to import libraries, prepare data, create, and train the model.
   - The trained model will be saved to Google Drive.

8. Features:
   - Home Page: Project description with training and validation graphs.
   - Student Profile: Page dedicated to the profile of student Cariza.
   - Real-Time Detection: Capture and processing of real-time video using OpenCV, applying the trained model to identify the student's face.
  
9. Results:
   - Validation Loss: 0.5270
   - Validation Accuracy: 0.8021
