import numpy as np
from PIL import Image

print("Shahd Elnassag ^_^")

# Function to upload image
def uploadImage(image_path):
    image = Image.open(image_path).convert("L")
    image = np.array(image)
    return image

# Function to save an image
def saveImage(image, output_image_path):
    image = Image.fromarray(image)
    image.save(output_image_path)
    print(f"Image saved to {output_image_path}")


# file paths
input_image_path = "test.jpg"  
output_image_path = "output_image.jpg" 

image = uploadImage(input_image_path)
print(f"Image loaded with Size: {image.shape}")

    # Save the image
saveImage(image, output_image_path)




