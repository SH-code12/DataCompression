import heapq
from collections import defaultdict


# Calculate the frequency of characters in the data
def calc_freq(data):
    fr = defaultdict(int)
    for c in data:
        fr[c] += 1
    return fr


class HufNode:
    def __init__(self, fr, char=None, left=None, right=None):
        self.fr = fr
        self.char = char
        self.l = left
        self.r = right

    def __lt__(self, other):
        return self.fr < other.fr


# Build the Huffman tree using a priority queue (min-heap)
def buildHuffman(fr):
    pq = []
    for char, freq in fr.items():
        heapq.heappush(pq, HufNode(freq, char))

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = HufNode(left.fr + right.fr, None, left, right)
        heapq.heappush(pq, merged)

    return pq[0] if pq else None


# Recursively generate Huffman codes from the Huffman tree
def get_codes(node, currcode="", codes=None):
    if codes is None:
        codes = {}

    if node is None:
        return

    if node.char is not None:
        codes[node.char] = currcode
    else:
        get_codes(node.l, currcode + '0', codes)
        get_codes(node.r, currcode + '1', codes)

    return codes


# Reverse the codes map so it can be used by Decompress function
def reverseMap(codes):
    reversed_map = {}
    for c, code in codes.items():
        reversed_map[code] = c

    return reversed_map


# Compress function after building the Huffman tree
def Compress(data, codes):
    ret = ""
    for c in data:
        ret += codes[c]
    return ret


# Decompress function using the Huffman codes
def Decompress(binary_data, codes):
    reverse_codes = {v: k for k, v in codes.items()}  # Reverse mapping
    current_bits = ""
    decompressed_text = ""

    for bit in binary_data:
        current_bits += bit
        if current_bits in reverse_codes:
            decompressed_text += reverse_codes[current_bits]
            current_bits = ""

    return decompressed_text


# Convert binary to bytes 

def binary_to_bytes(binary_string):
    # Calculate padding
    padding_length = (8 - len(binary_string) % 8) % 8
    binary_string += '0' * padding_length

    # Convert to bytes
    byte_list = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_list.append(int(byte, 2))

    # Append the padding length as the last byte
    byte_list.append(padding_length)
    return bytes(byte_list)



# Convert bytes back to a binary string
def bytes_to_binary(byte_data):
    # Extract padding length from the last byte
    padding_length = byte_data[-1]
    binary_string = ''.join(f"{byte:08b}" for byte in byte_data[:-1])

    # Remove padding
    return binary_string[:-padding_length] if padding_length > 0 else binary_string



def compress_file(input_file, compressed_file, codes_file):
    with open(input_file, 'r') as infile:
        data = infile.read()

    freq = calc_freq(data)
    huffman_root = buildHuffman(freq)
    huffman_codes = get_codes(huffman_root)
    compressed_data = Compress(data, huffman_codes)

    # Save compressed data with padding
    with open(compressed_file, 'wb') as bin_file:
        bin_file.write(binary_to_bytes(compressed_data))

    # Save Huffman codes
    with open(codes_file, 'w') as codes_outfile:
        for char, code in huffman_codes.items():
            char_representation = 'SPACE' if char == ' ' else char
            codes_outfile.write(f"{char_representation}:{code}\n")

# Decompress function for files
def decompress_file(compressed_file, codes_file, output_file):
    # Read compressed binary data and remove padding
    with open(compressed_file, 'rb') as bin_file:
        compressed_data = bytes_to_binary(bin_file.read())

    # Read Huffman codes
    codes = {}
    with open(codes_file, 'r') as codes_infile:
        for line in codes_infile:
            char, code = line.strip().split(':', 1)
            char = ' ' if char == 'SPACE' else char
            codes[char] = code

    # Decompress data
    decompressed_data = Decompress(compressed_data, codes)

    # Write decompressed data to file
    with open(output_file, 'w') as outfile:
        outfile.write(decompressed_data)

    print(f"Decompressed data saved to '{output_file}'")


# Test for file operations
def file_operations():
    input_filename = 'test_input.txt'
    compressed_filename = 'test_compressed.bin'  
    codes_filename = 'test_codes.txt'
    decompressed_filename = 'test_decompressed.txt'
    test_data = input("Enter Data: ")

    # Write test data to the input file
    with open(input_filename, 'w') as infile:
        infile.write(test_data)

    print("\nTesting file compression...")
    compress_file(input_filename, compressed_filename, codes_filename)

    # Display compressed binary data
    with open(compressed_filename, 'rb') as compressed_file:
        compressed_data = compressed_file.read()
    print("Compressed Data (binary):", compressed_data)

    # Display Huffman codes
    print("Huffman Codes:")
    with open(codes_filename, 'r') as codes_file:
        codes_data = codes_file.readlines()
    for line in codes_data:
        print(line.strip())

    print("\nTesting file decompression...")
    decompress_file(compressed_filename, codes_filename, decompressed_filename)

    # Read and display decompressed data
    with open(decompressed_filename, 'r') as decompressed_file:
        decompressed_data = decompressed_file.read()
    print("Decompressed Data:", decompressed_data)

# Test for in-memory operations
def logic():
    test_data = input("Please the text ypu want : ")
    freq = calc_freq(test_data)
    huffman_root = buildHuffman(freq)
    huffman_codes = get_codes(huffman_root)
    compressed_data = Compress(test_data, huffman_codes)

    print("\nLogic Test Results:")
    print("Huffman Codes:", huffman_codes)
    print("Compressed Data:", compressed_data)

    decompressed_data = Decompress(compressed_data, huffman_codes)
    print("Decompressed Data:", decompressed_data)


# Run tests
# logic()
file_operations()
