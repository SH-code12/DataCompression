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


# Function to compress the image using the codebook (k-means) and return a matrix of codes
def compress(image, vectorSize, codebook):
    height, width = image.shape
    codes_matrix = np.zeros((height // vectorSize, width // vectorSize), dtype=int)

    # Divide image into blocks
    vectors = divideToVectors(image, vectorSize)

    # Find the nearest cluster for each vector
    labels = codebook.predict(vectors)

    vector_idx = 0
    for h in range(0, height, vectorSize):
        for w in range(0, width, vectorSize):
            if (h + vectorSize <= height) and (w + vectorSize <= width):
                codes_matrix[h // vectorSize, w // vectorSize] = labels[vector_idx]
                vector_idx += 1

    return codes_matrix


# Function to save compression data (labels and codebook) to text files
def save_compression_data(labels, codebook, compressed_file, codebook_file, height, width):
    with open(compressed_file, 'w') as f:
        f.write(f"{height} {width}\n")  # Save dimensions
        f.write(' '.join(map(str, labels)) + '\n')  # Save cluster indices

    # Save codebook
    with open(codebook_file, 'w') as f:
        for center in codebook:
            f.write(' '.join(map(str, center)) + '\n')  # Save each cluster center


# Function to load compression data (labels and codebook) from text files
def load_compression_data(compressed_file, codebook_file):
    with open(compressed_file, 'r') as f:
        height, width = map(int, f.readline().split())
        labels = list(map(int, f.readline().split()))

    codebook = []
    with open(codebook_file, 'r') as f:
        for line in f:
            codebook.append(list(map(float, line.split())))
    codebook = np.array(codebook)

    return labels, codebook, height, width


# Decompression function
def decompress(codes_matrix, codebook, vectorSize, height, width):
    image = np.zeros((height, width), dtype=np.uint8)
    idx = 0
    for h in range(0, height, vectorSize):
        for w in range(0, width, vectorSize):
            if (h + vectorSize <= height) and (w + vectorSize <= width):
                image[h:h + vectorSize, w:w + vectorSize] = codebook[
                    codes_matrix[h // vectorSize, w // vectorSize]].reshape(vectorSize, vectorSize)
                idx += 1
    return image


# File paths
input_image_path = "test2.jpg"
output_image_path = "output_image.jpg"

# Load and process the image
image = uploadImage(input_image_path)
print(f"Image loaded with Size: {image.shape}")

# Parameters
vectorSize = 4
numOfClusters = 16

# Divide image into blocks
vectors = divideToVectors(image, vectorSize)
print(f"Image divided into {len(vectors)} vectors of size {vectorSize}x{vectorSize}")

# Generate codebook
codebook_g = generateCodebook(vectors, numOfClusters)
print(f"Codebook generated with {numOfClusters} clusters.")

codes_matrix = compress(image, vectorSize, codebook_g)

save_compression_data(
    codes_matrix.flatten(),  # Flatten to save as a single list of labels
    codebook_g.cluster_centers_,
    "compressed_data.txt",
    "codebook_data.txt",
    image.shape[0],
    image.shape[1]
)

labels, codebook, height, width = load_compression_data("compressed_data.txt", "codebook_data.txt")

decompressed_image = decompress(codes_matrix, codebook, vectorSize, height, width)

saveImage(decompressed_image, "decompressed_image.jpg")
