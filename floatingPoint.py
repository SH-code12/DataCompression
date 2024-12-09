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

# Testing Function

def runAlgorithm():
    
    inputData = input("Enter Data to Compressed it: ").strip()
    
    probabilities = getProbabilities(inputData)
    

    compressedData = compressFloatingPoint(inputData , probabilities)

    print("Compressed Data:", compressedData)

# runAlgorithm()

def runOnfiles():
    input_filename = 'Floatinput.txt'
    compressed_filename = 'Floatinput.bin'

    file1 = open(input_filename,"r+")
    data = file1.read().strip()
    print(data)
    probablity = getProbabilities(data)
    compressedData =  compressFloatingPoint(data, probablity)
    print(compressedData)
    # successful writing to binary
    writeTofile = open(compressed_filename,"wb")
    writeTofile.write(struct.pack('d',compressedData))
    writeTofile.close()
    # succesful reading from binary file

    print("succesful")
    readfromBinary = open(compressed_filename,"rb")
    print(struct.unpack('d',readfromBinary.read(8))[0])
    # here pass the converted double from binary to decompression



runOnfiles()

