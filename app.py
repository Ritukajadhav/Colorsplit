from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np

app = Flask(__name__)

# Updated color ranges in HSV
color_ranges = {
    "Red": (np.array([0, 150, 70]), np.array([10, 255, 255])),
    "Red2": (np.array([170, 150, 70]), np.array([180, 255, 255])),
    "Pink": (np.array([145, 100, 150]), np.array([170, 255, 255])),
    "Orange": (np.array([11, 150, 150]), np.array([25, 255, 255])),
    "Skin Tone": (np.array([0, 20, 70]), np.array([20, 150, 255])),
    "Brown": (np.array([10, 100, 200]), np.array([20, 255, 200])),
    "Dark Brown": (np.array([10, 100, 50]), np.array([20, 255, 150])),
    "Blue": (np.array([100, 150, 70]), np.array([128, 255, 255])),
    "Yellow": (np.array([20, 100, 100]), np.array([30, 255, 255])),
    "White": (np.array([0, 0, 200]), np.array([180, 20, 255])),
    "Gray": (np.array([0, 0, 40]), np.array([180, 18, 230])),
    "Green": (np.array([36, 120, 100]), np.array([70, 255, 255])),
    "Light Green": (np.array([36, 80, 120]), np.array([70, 150, 255])),
    "Light Blue": (np.array([90, 100, 100]), np.array([110, 255, 255])),
    "Purple": (np.array([129, 100, 100]), np.array([158, 255, 255])),
    "Black": (np.array([0, 0, 0]), np.array([180, 255, 40])),
}

# Open a connection to the camera
camera = cv2.VideoCapture(0)

# Function to detect color at the given point in HSV frame
def detect_color_at_point(hsv_frame, x, y, color_ranges):
    if x < 0 or y < 0 or x >= hsv_frame.shape[1] or y >= hsv_frame.shape[0]:
        return "Out of bounds"
    
    pixel = hsv_frame[y, x]  # Get the HSV value of the pixel under the pointer
    
    for color_name, (lower, upper) in color_ranges.items():
        # Create a mask for the color range
        mask = cv2.inRange(hsv_frame, lower, upper)
        # Check if the pixel is within the color range
        if mask[y, x] > 0:
            return color_name
    
    return "No Color Detected"

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/color_detection')
def color_detection():
    return render_template('color_detection.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Route to handle video streaming
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Convert frame to JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Yield frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to handle color detection based on mouse coordinates
@app.route('/detect_color', methods=['POST'])
def detect_color():
    data = request.get_json()
    x = int(data['x'])
    y = int(data['y'])

    # Capture frame from the video feed
    success, frame = camera.read()
    if not success:
        return jsonify({'color': 'No frame available'})

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    detected_color = detect_color_at_point(hsv_frame, x, y, color_ranges)

    return jsonify({'color': detected_color})

if __name__ == "__main__":
    app.run(debug=True)
