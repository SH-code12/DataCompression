import numpy as np

from PIL import Image

from sklearn.cluster import KMeans  # Corrected typo


print("Shahd Elnassag ^_^")


# Function to upload image

def uploadImage(imagePath):

    image = Image.open(imagePath).convert("L")

    image = np.array(image)
    return image


# Function to save an image

def saveImage(image, output_image_path):

    image = Image.fromarray(image)

    image.save(output_image_path)

    print(f"Image saved to {output_image_path}")
    

# Function to divide Images to blocks

def divideToVectors(image, vectorSize):
    height , width = image.shape
    vectors = []
    for h in range(0, height, vectorSize):
        for w in range(0, width, vectorSize):
            vector = image[h : h + vectorSize, w : w + vectorSize]
            if vector.shape == (vectorSize , vectorSize):
                vectors.append(vector.flatten())
    return np.array(vectors)




# file paths

input_image_path = "test.jpg"  

output_image_path = "output_image.jpg"

# Load and process the image

image = uploadImage(input_image_path)

print(f"Image loaded with Size: {image.shape}") 


# Divide image into blocks

vectorSize = 4

vectors = divideToVectors(image, vectorSize)

print(f"Image divided into {len(vectors)} vectors of size {vectorSize}x{vectorSize}")

    # Save the image

saveImage(image, output_image_path)



