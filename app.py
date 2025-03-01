from flask import Flask, request, render_template, redirect, jsonify
import numpy as np
import cv2
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import os
import joblib

# Tạo ứng dụng Flask
app = Flask(__name__)

# model = LogisticRegression()
model = SVC()
# Load model Logistic Regression đã được huấn luyện
model = joblib.load('SVC_model.pkl')

# Giả sử bạn có các classes đã được huấn luyện
classes = ['NORMAL', 'PNEUMONIA']
label_encoder = LabelEncoder()
label_encoder.fit(classes)

IMG_SIZE = 227

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Kiểm tra nếu có file được tải lên
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:

            nparr = np.fromstring(file.read(), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img_resized = img_resized.astype('float32') / 255.0
            img_resized = img_resized.flatten().reshape(1, -1)
            
            # Dự đoán lớp của ảnh
            prediction = model.predict(img_resized)
            predicted_class = label_encoder.inverse_transform(prediction)[0]
            
            return jsonify({'prediction': predicted_class})
    return render_template('index.html', prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
