from flask import Flask, render_template, Response
import cv2
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

model = load_model('projeto_finalAi\model\cariza_classifier_model2.h5')

def gen_frames():  # Generate frame by frame from camera
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Process the frame for model prediction
            img = cv2.resize(frame, (224, 224))
            img_array = np.expand_dims(img, axis=0) / 255.0
            prediction = model.predict(img_array)

            #binary classification: 0 for not Cariza, 1 for Cariza
            label = 'Your Cariza' if prediction[0] > 0.5 else 'Your not Cariza'
            color = (0, 255, 0) if label == 'Your Cariza' else (0, 0, 255)
            cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
