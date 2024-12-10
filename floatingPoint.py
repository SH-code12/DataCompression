import struct

print("Shahd Elnassag ^_^")

def getProbabilities(data):
    
    uniqueSymbol = sorted(set(data))
    
    total_prob = 0.0
    
    probabilities = {}
    
    for symbol in uniqueSymbol:
        while True:
            probability = float(input("Enter the probability for symbol: " + symbol + ": ").strip())
            
            if probability < 0 or probability > 1:
                print("probability must be betwwen 0 and 1, try again\n")
                continue
            probabilities[symbol] = probability
            total_prob += probability
            break
            
    if total_prob != 1.0:
        print("Error! , Sum of Probabilities must be 1. Now Sum of probabilities = " + total_prob 
            + "\nTry again and Enter correct Probabilities")
    return probabilities


def calculateRange(probabilities):
                    
    Ranges = {}
    
    newProb = 0.0
    # claculate ranges for each symbol
    for symbol, prob in probabilities.items():
        lowRange = newProb 
        highRange = newProb + prob
        # store Ranges
        Ranges[symbol] = (lowRange , highRange)
        
        # Update probability for the next symbol
        newProb = highRange
        
    return Ranges

def compressFloatingPoint(data , probabilities):
    
    # calculate ranges 
    ranges = calculateRange(probabilities)
    
    lower = 0.0
    upper = 1.0
    
    for symbol in data:
        # Initialize Ranges 
        lowRange, highRange = ranges[symbol]
        # for check the range calculated correct
        print(f"Symbol: {symbol}, lowRange: {lowRange:.4f}, highRange: {highRange:.4f} ")

        # new Ranges
        rangeWidth = upper - lower
        upper = lower + rangeWidth * highRange
        lower = lower + rangeWidth * lowRange
        # for check the range calculated correct
        print(f"Symbol: {symbol}, Lower: {lower:.4f}, Upper: {upper:.4f} ")
    
    # chooce value from final range
    compressedData = (upper + lower) / 2
    
    return compressedData

def decompressFloatingPoint(Code,probabilities,length):
    ranges = calculateRange(probabilities)

    lower = 0.0
    upper = 1.0
    decompressedData=""
    for _ in range(length):
        rangeW = upper - lower
        #scale the target value based on the current range
        target = (Code - lower) / rangeW
        #check target value

        for symbol, (low, high) in ranges.items():
            if low <= target < high:
                # check target value in the correct range
                print(f"target: {target}, Lower: {low:.4f}, Upper: {high:.4f} , symbol: {symbol}")
                decompressedData += symbol
               #update
                upper = lower + rangeW * high
                lower = lower + rangeW * low
                break

    return decompressedData



# Testing Function

def runAlgorithm():
    
    inputData = input("Enter Data to Compressed it: ").strip()
    
    probabilities = getProbabilities(inputData)
    

    compressedData = compressFloatingPoint(inputData , probabilities)

    print("Compressed Data:", compressedData)

    decompressedData = decompressFloatingPoint(compressedData, probabilities, len(inputData))

    print("Decompressed Data", decompressedData)

def runOnfiles():
    input_filename = 'Floatinput.txt'
    compressed_filename = 'Floatinput.bin'

    file1 = open(input_filename,"r+")
    data = file1.read().strip()
    print("orignal data: ",data)
    probablity = getProbabilities(data)
    compressedData =  compressFloatingPoint(data, probablity)
    print("compressed Data: ",compressedData)

    unique_elements = len(probablity)
    with open(compressed_filename, "wb") as writeTofile:
        # store the length and the unique data
        writeTofile.write(struct.pack('I', len(data)))
        writeTofile.write(struct.pack('I', unique_elements))
        # store the probabilities
        for symbol, prob in probablity.items():
            writeTofile.write(struct.pack('c', symbol.encode('utf-8')))
            writeTofile.write(struct.pack('d', prob))

        # store the compressed floating-point data
        writeTofile.write(struct.pack('d', compressedData))

    print("Data successfully written to:", compressed_filename)
    # successful writing to binary

# decompress from a file
    with open(compressed_filename, "rb") as readfromBinary:
        # Read the length of the data
        data_length = struct.unpack('I', readfromBinary.read(4))[0]
        print("Decoded Data Length:", data_length)

        # Read the number of unique elements
        unique_elements_read = struct.unpack('I', readfromBinary.read(4))[0]
        print("Decoded Number of Unique Elements:", unique_elements_read)

        # Read the probabilities
        decoded_probabilities = {}
        for _ in range(unique_elements_read):  # Loop for the number of unique symbols
            symbol = struct.unpack('c', readfromBinary.read(1))[0].decode('utf-8')
            prob = struct.unpack('d', readfromBinary.read(8))[0]
            decoded_probabilities[symbol] = prob
        print("Decoded Probabilities:", decoded_probabilities)

        # Read the compressed floating-point data
        compressed_value = struct.unpack('d', readfromBinary.read(8))[0]
        print("Decoded Compressed Value:", compressed_value)

        # Decompress and validate
        decompressedData = decompressFloatingPoint(compressed_value, decoded_probabilities, data_length)
        print("Decompressed Data:", decompressedData)

        if decompressedData == data:
            print("Decompression successful!")
        else:
            print("Decompression failed!")



runOnfiles()
#runAlgorithm()

