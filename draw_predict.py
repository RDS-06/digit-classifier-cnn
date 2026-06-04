import tkinter as tk
from PIL import Image, ImageDraw
import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("model.keras")

# Create window
root = tk.Tk()
root.title("Digit Classifier")

# Drawing canvas
canvas_width = 280
canvas_height = 280

canvas = tk.Canvas(
    root,
    width=canvas_width,
    height=canvas_height,
    bg="black"
)
canvas.pack()

# PIL image for processing
image = Image.new("L", (canvas_width, canvas_height), 0)
draw = ImageDraw.Draw(image)

# Label for prediction
result_label = tk.Label(root, text="Draw a digit", font=("Arial", 16))
result_label.pack()


def paint(event):
    x, y = event.x, event.y

    # Draw on tkinter canvas
    canvas.create_oval(
        x - 8, y - 8,
        x + 8, y + 8,
        fill="white",
        outline="white"
    )

    # Draw on PIL image
    draw.ellipse(
        (x - 8, y - 8, x + 8, y + 8),
        fill=255
    )


def clear_canvas():
    canvas.delete("all")
    draw.rectangle(
        (0, 0, canvas_width, canvas_height),
        fill=0
    )
    result_label.config(text="Draw a digit")


def predict_digit():
    # Resize to MNIST size
    img = image.resize((28, 28))

    # Convert to numpy array
    img_array = np.array(img)

    # Normalize
    img_array = img_array / 255.0

    # Reshape for CNN
    img_array = img_array.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img_array, verbose=0)

    digit = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    result_label.config(
        text=f"Prediction: {digit} ({confidence:.2f}%)"
    )


# Mouse drawing
canvas.bind("<B1-Motion>", paint)

# Buttons
predict_btn = tk.Button(
    root,
    text="Predict",
    command=predict_digit
)
predict_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear",
    command=clear_canvas
)
clear_btn.pack(pady=5)

root.mainloop()