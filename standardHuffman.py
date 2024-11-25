# 1. Calculate probabilities
def calculate_probabilities(data):
    frequencies = {}
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    total_length = len(data)
    probabilities = {}
    for char, freq in frequencies.items():
        probabilities[char] = freq / total_length
    return probabilities


# Node class for Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


# Build Huffman tree
def sum_Probabilities(probabilities):
    nodes = []

    for char, freq in probabilities.items():
        nodes.append(Node(char, freq))

    while len(nodes) > 1:
        # Sort the nodes by frequency
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if nodes[i].freq > nodes[j].freq:
                    nodes[i], nodes[j] = nodes[j], nodes[i]

        left = nodes.pop(0)
        right = nodes.pop(0)

        # Create a new node
        newNode = Node(None, left.freq + right.freq)
        newNode.left = left
        newNode.right = right

        nodes.append(newNode)

    return nodes[0]  


# Generate Huffman codes
def create_codes(node, current_code="", codes={}):
    if node is None:
        return codes

    if node.char is not None:  
        codes[node.char] = current_code
    else:
        create_codes(node.left, current_code + "0", codes)
        create_codes(node.right, current_code + "1", codes)

    return codes


# Compress the data
def compress(data, codes):
    compressed_data = ""
    for char in data:
        compressed_data += codes[char]
    return compressed_data


# Decompress the data
def decompress(compressed_text, codes):
    reverse_codes = {}
    for key, value in codes.items():
        reverse_codes[value] = key

    pointer = 0
    current_code = ""
    original_text = ""

    while pointer < len(compressed_text):
        current_code += compressed_text[pointer]
        if reverse_codes.get(current_code) is not None:
            original_text += reverse_codes[current_code]
            current_code = ""
        pointer += 1

    return original_text


data = "bbbacacbcd"

probabilities = calculate_probabilities(data)
print("Character Probabilities:")
for char, prob in probabilities.items():
    print(f"'{char}': {prob:.4f}")

root = sum_Probabilities(probabilities)

huffman_codes = create_codes(root)
print("\nHuffman Codes:")
for char, code in huffman_codes.items():
    print(f"'{char}': {code}")

compressed_data = compress(data, huffman_codes)
print(f"\nCompressed Data: {compressed_data}")

decompressed_data = decompress(compressed_data, huffman_codes)
print(f"Decompressed Data: {decompressed_data}")
