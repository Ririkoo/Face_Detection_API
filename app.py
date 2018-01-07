import cv2
import numpy as np
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
app.config.from_object(__name__)


def detect_faces(image):
    faceCascade = cv2.CascadeClassifier("/root/face_detect_api/haarcascade_frontalface_default.xml")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    coordinates = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in faces]
    try:
        return coordinates
    except:
        return []


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/prediction", methods=["POST"])
def prediction():
    if request.method == "POST":
        stream = request.files["file"]
        data = stream.read()
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        face_coordinates = detect_faces(image)
        if (len(face_coordinates) < 1):
            return jsonify({"status": "failed"})
        else:
            return jsonify({"status": "success",
                            "face_num": len(face_coordinates),
                            "faces": face_coordinates})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
