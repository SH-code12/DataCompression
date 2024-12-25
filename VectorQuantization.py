import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


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

# Function to divide Images into blocks
def divideToVectors(image, vectorSize):
    height, width = image.shape
    vectors = []
    for h in range(0, height, vectorSize):
        for w in range(0, width, vectorSize):
            vector = image[h: h + vectorSize, w: w + vectorSize]
            if vector.shape == (vectorSize, vectorSize):
                vectors.append(vector.flatten())
    return np.array(vectors)

# Function to generate Codebook
def generateCodebook(vectors, numOfClusters):
    codebook = KMeans(n_clusters=numOfClusters, random_state=0)
    codebook.fit(vectors)
    return codebook

# Function to compress the image using the codebook (k-means)
def compress(image, vectorSize, codebook):
    height, width = image.shape
    compressed_image = np.zeros_like(image)

    # Divide image into blocks
    vectors = divideToVectors(image, vectorSize)

    # Find the nearest cluster for each vector
    cluster_centers = codebook.cluster_centers_
    labels = codebook.predict(vectors)

    vector_idx = 0
    for h in range(0, height, vectorSize):
        for w in range(0, width, vectorSize):
            if (h + vectorSize <= height) and (w + vectorSize <= width):
                # Get the closest codebook vector and assign it to the block
                compressed_image[h:h + vectorSize, w:w + vectorSize] = cluster_centers[labels[vector_idx]].reshape(vectorSize, vectorSize)
                vector_idx += 1

    return compressed_image


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

# Generate codebook
numOfClusters = 16  
codebook_g = generateCodebook(vectors, numOfClusters)
print(f"Codebook generated with {numOfClusters} clusters.")

# Compress the image
compressed_image = compress(image, vectorSize, codebook_g)

# Save the compressed image
saveImage(compressed_image, output_image_path)
