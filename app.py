from flask import Flask, render_template,request
from .cv2 import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convertimg', methods=['POST'])
def convertimg():
    try:
        if request.method == 'POST':
            filename = request.files['image']
            response = filename.read()
            frame = cv2.imdecode(np.fromstring(response, np.uint8), cv2.IMREAD_COLOR)
            detector = cv2.QRCodeDetector()
            data, vertices_array, binary_qrcode = detector.detectAndDecode(frame) 
            uuid=''            
            if vertices_array is not None:
                return data
            else:
                return "No data found"                
    except Exception as e:
        return ('error occured,' + str(e))
if __name__ == "__main__":
    app.run()