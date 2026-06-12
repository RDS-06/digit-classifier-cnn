🧠 Handwritten Digit Classifier (0–9) using CNN

A deep learning project that classifies handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset.

It also includes an interactive GUI where users can draw digits and get real-time predictions.

🚀 Features
CNN model trained on the MNIST dataset
High accuracy on test data
Predicts handwritten digits from images
Interactive Tkinter GUI for drawing digits
Model saving and loading using Keras
🛠️ Tech Stack
Python
TensorFlow / Keras
NumPy
Matplotlib
Pillow (PIL)
Tkinter (GUI)
📊 Dataset
Dataset: MNIST
Classes: 10 (digits 0–9)
Image size: 28×28 grayscale
Training samples: 60,000
Test samples: 10,000
🧠 Model Architecture
Conv2D (32 filters, 3×3) + ReLU
MaxPooling2D (2×2)
Conv2D (64 filters, 3×3) + ReLU
MaxPooling2D (2×2)
Flatten
Dense (64 units) + ReLU
Dense (10 units) + Softmax
📁 Project Structure
digit-classifier-cnn/
│
├── train.py              # Train CNN model
├── predict.py            # Test model on MNIST sample
├── draw_predict.py       # Tkinter GUI for drawing digits
├── model.keras           # Saved trained model
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/digit-classifier-cnn.git
cd digit-classifier-cnn
2. Install dependencies
pip install -r requirements.txt
🏃 How to Run
🔹 Train the model
python train.py
🔹 Test prediction (MNIST image)
python predict.py
🔹 Run GUI app
python draw_predict.py
🎨 GUI Features
Draw digits using mouse
Click “Predict” to classify digit
Clear canvas option
Shows prediction + confidence score
📈 Output Example
Prediction: 7 (98.45%)
Actual: 7
🔥 Future Improvements
Add Streamlit web app version
Improve accuracy with data augmentation
Add confusion matrix visualization
Deploy as web app
Real-time webcam digit detection
👨‍💻 Author

Built as a deep learning project to understand CNNs and image classification.

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub and feel free to improve it!

📦 requirements.txt
tensorflow
numpy
matplotlib
pillow
