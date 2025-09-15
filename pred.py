from yolov5 import YOLOv5
from pathlib import Path
from PIL import Image
from IPython.display import display

# Path to test img
img_path = Path("/content/yolov5/new_images/test.jpg")

# Load YOLOv5 with trained weights
yolov5 = YOLOv5('best.pt', device="cuda")

# Run inference
results = yolov5.predict(img_path)

# Print results
print(results)

# Display image in notebook
img = Image.open(results.files[0])
display(img)