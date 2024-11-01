def Compress(data):
    searchWindow= int(0.4 * len(data))
    lookAheadWindow= int(0.3 * len(data))
    
    compressedCode = []
    currPointer = 0
    
    while currPointer < len(data):
        maxMatch = 0
        goBackedFor = 0
        nextChar = data[currPointer] if currPointer < len(data) else ''
        backPointer = max(0, currPointer - searchWindow)
        currMaxSearch = min(currPointer + lookAheadWindow, len(data))

        for j in range(backPointer, currPointer):
            match = 0
            while (currPointer + match < currMaxSearch and 
                data[j + match] == data[currPointer + match]):
                match += 1

            if match > maxMatch:
                maxMatch = match
                goBackedFor = currPointer - j
                if currPointer + match< len(data):
                    nextChar = data[currPointer + match]
                else:
                    nextChar = ''

        compressedCode.append((goBackedFor, maxMatch, nextChar))
        currPointer += maxMatch + 1

    return compressedCode





def Decompress_LZ77(Compress_LZ77):
    
    # array store Decompressed Data
    Decompress_Data = []
    
    for position ,length,nextSymbol in Compress_LZ77:
        # exist match! substring match string and add it to Decompressed Data
        if position > 0 :
            startIndex = len(Decompress_Data) - position
            
            Decompress_Data += Decompress_Data[startIndex : startIndex + length]
                        
        if nextSymbol:
        # Add char direct if position = 0
            Decompress_Data += nextSymbol
        
        # ' ' to print characters with space 
        
    return ''.join(Decompress_Data)


#compressed_data = [(0, 0, 'A'), (0, 0, 'B'), (2, 1, 'A'), (3, 2, 'B'), (5, 3, 'B'), (2, 2, 'B'), (5, 5, 'B'), (1 ,1 , 'A')]
#TestSpace = [(0, 0, 's'), (0, 0, 'h'), (0, 0, 'a'), (2, 1, 'd'), (0, 0, ' '), (0, 0, 'm'), (0, 0, 'o'), (5, 1, 'a'),(4, 1, 'e'), (8, 1, '')]

#decompressed = Decompress_LZ77(TestSpace)
#print("Decompressed Data Using LZ77 Technique:", decompressed)

print("Enter text to copress and Decompress it: ")
data = input()
# data = "AsmaaAtef Omran"
compressed_data = Compress(data)
print("Compressed Data:", compressed_data)

decompressed_data = Decompress_LZ77(compressed_data)
print("Decompressed Data:", decompressed_data)