import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

print("Shahd Elnassag ^_^")
def uploadImage(imagePath):
    image = Image.open(imagePath).convert("L")
    image = np.array(image)
    return image

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

# Function to save compression data (labels and codebook) to files
def save_compression_data(labels, codebook, compressed_file, codebook_file, height, width):
    with open(compressed_file, 'w') as f:
        f.write(f"{height} {width}\n")  # Save dimensions
        f.write(' '.join(map(str, labels)) + '\n')  # Save cluster indices

    # Save codebook
    with open(codebook_file, 'w') as f:
        for center in codebook:
            f.write(' '.join(map(str, center)) + '\n')  # Save each cluster center

# File paths
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

# Save compression data and codebook
labels = codebook_g.predict(divideToVectors(image, vectorSize))  # Cluster indices
save_compression_data(
    labels,
    codebook_g.cluster_centers_,
    "compressed_data.txt",
    "codebook_data.txt",
    image.shape[0],
    image.shape[1]
)

# Decompression function
def decompress(compressed_file, codebook_file, vectorSize):
    with open(compressed_file, 'r') as f:
        height, width = map(int, f.readline().split())
        labels = list(map(int, f.readline().split()))
    with open(codebook_file, 'r') as f:
        cluster_centers = []
        for line in f:
            cluster_centers.append(list(map(float, line.split())))
    cluster_centers = np.array(cluster_centers)
    cluster_centers = np.clip(cluster_centers, 0, 255).astype(np.uint8)
    decompressed_image = np.zeros((height, width), dtype=np.uint8)
    vector_idx = 0
    for h in range(0, height, vectorSize):
        for w in range(0, width, vectorSize):
            if (h + vectorSize <= height) and (w + vectorSize <= width):
                decompressed_image[h:h + vectorSize, w:w + vectorSize] = cluster_centers[labels[vector_idx]].reshape(vectorSize, vectorSize)
                vector_idx += 1
    return decompressed_image

# Call the decompress function
decompressed_image = decompress("compressed_data.txt", "codebook_data.txt", vectorSize)

# Save the decompressed image
decompressed_image_path = "decompressed_image.jpg"
saveImage(decompressed_image, decompressed_image_path)
