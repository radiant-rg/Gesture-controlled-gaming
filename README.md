
# 🚗 Gesture Drive: AI Hand Control for Racing Games

A Computer Vision project that allows you to play racing games (like Hill Climb Racing) using hand gestures via your webcam.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)

## 🎮 How It Works

The program uses **MediaPipe** to detect hand landmarks and counts the number of fingers extended to trigger keyboard inputs.

| Gesture | Fingers Detected | Action | Key Press |
| :--- | :---: | :--- | :--- |
| **Index Finger Up** | 1 | **GAS** | `RIGHT ARROW` |
| **Fist (Closed)** | 0 | **BRAKE** | `LEFT ARROW` |
| **Open Hand** | 5 | **NEUTRAL** | None |
---
## 🛠️ Installation

1.  **Clone the repository** (or download the files):
    \`\`\`bash
    git clone https://github.com/radiant-rg/gesture-drive.git
    cd gesture-drive
    \`\`\`

2.  **Install dependencies**:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`
---
## 🚀 Usage

1.  Start your racing game (e.g., Hill Climb Racing in a browser).
2.  Run the script:
    \`\`\`bash
    python main.py
    \`\`\`
3.  Position your hand in front of the webcam:
    * **Raise 1 Finger** to accelerate.
    * **Close your fist** to brake/reverse.
    * **Open your hand** to coast.
4.  Press \`ESC\` to quit the controller.
---
## ⚠️ Troubleshooting

* **Permissions:** Ensure your terminal/IDE has permission to access the Webcam and control the Keyboard (Input Monitoring).
* **Lighting:** Ensure your hand is well-lit for accurate detection.
* **Failsafe:** If the mouse/keyboard gets stuck, drag your mouse to any corner of the screen to trigger the PyAutoGUI failsafe.
---
## 📄 License

This project is open-source and available under the MIT License.
EOF
echo "📝 Created file: README.md"

echo "✅ Setup complete! Type 'cd gesture-drive-controller' to start."