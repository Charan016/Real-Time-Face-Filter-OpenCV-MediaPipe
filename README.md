# 🎭 Real-Time Face Filter using OpenCV & MediaPipe

A fun and interactive **real-time face filter application** that uses your webcam to detect facial landmarks and overlay effects like a mustache and hat.

---

## 🚀 Features

* 🎥 Real-time webcam face detection
* 🧠 Facial landmark tracking using MediaPipe
* 🎭 Overlay filters (Mustache & Hat)
* 💾 Capture and save images
* ⚡ Lightweight and fast performance

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📂 Project Structure

```
Real-Time-Face-Filter-OpenCV-MediaPipe/
│
├── main.py              # Main application script
├── mustache.png         # Mustache filter image (RGBA)
├── hat.png              # Hat filter image (RGBA)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Real-Time-Face-Filter-OpenCV-MediaPipe.git
cd Real-Time-Face-Filter-OpenCV-MediaPipe
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 🎮 Controls

* **ESC** → Exit the application
* **S** → Save current frame as image

---

## 🧠 How It Works

* Uses **MediaPipe Face Mesh** to detect facial landmarks
* Converts landmark points into pixel coordinates
* Calculates face width and positions filters dynamically
* Applies PNG overlays using alpha blending (RGBA)

---

## 📸 Output

Real-time webcam feed with filters applied on detected face.

*(Tip: Add a screenshot here for better presentation)*

---

## 🔮 Future Improvements

* 😎 Add sunglasses / multiple filters
* 🔄 Face tilt detection (rotate filters)
* 👥 Multi-face support
* 📊 FPS counter for performance tracking
* 🎛️ Switch filters using keyboard

---

## 👨‍💻 Author

**Charan**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!





conda create -n FaceFiliter_Project python=3.10 -y

pip install mediapipe==0.10.8 opencv-python numpy

# use this in ternaml to activae the Environment

& "C:\Users\chara\anaconda3\shell\condabin\conda-hook.ps1"
conda activate FaceFiliter_Project

pip install opencv-python mediapipe==0.10.8 numpy

