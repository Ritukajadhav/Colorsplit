
# ColorSplit

ColorSplit is a web-based application that focuses on color-based image processing and visualization. The project is built using Flask for the backend and standard web technologies for the frontend.

---

## Project Overview

ColorSplit allows users to interact with images and perform color-related operations through a browser-based interface. The application follows a simple client–server architecture where the frontend communicates with the Flask backend.

---

## Tech Stack

- Backend: Flask (Python)
- Image Processing: OpenCV, NumPy
- Frontend: HTML, CSS, JavaScript
- Styling: Custom CSS

---

## Project Structure

```text
ColorSplit/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       ├── bg2.jpg
│       ├── colorsplitlogo.png
│       ├── loginimg.png
│       ├── smallcircleimg.jpg
│       ├── member1.jpg
│       ├── member2.jpg
│       ├── member3.jpg
│       └── member4.jpg
│
└── templates/
    ├── index.html
    ├── login.html
    └── dashboard.html
````

---

## Installation and Setup

### Prerequisites

* Python 3.x
* pip (Python package manager)

---

### Steps to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Janhavi47/Colorsplit.git
   ```

2. Navigate into the project directory:

   ```bash
   cd Colorsplit
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate       # On Windows
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask application:

   ```bash
   python app.py
   ```

6. Open your browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

---

## Dependencies

The following Python libraries are used in this project:

```text
Flask
opencv-python
numpy
```

---

## Notes

* Static assets such as images and stylesheets are stored in the `static/` directory.
* HTML templates are stored in the `templates/` directory.
* The project has been developed and tested in a local development environment.

---

