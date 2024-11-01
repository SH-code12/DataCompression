print("Shahd Elnassag ^_^")



# Will Add Soon God Willing
def Compress_LZW(data):
    # table store ascii and another new chars 
    dictinary_table = {}
    for i in range(256):
        dictinary_table[chr(i)] = i
        
    startcode = 256
    # array store compressed data
    compressedData = []
    currentSeq = ""
    
    for nextSymbol in data:
        newSeq = currentSeq + nextSymbol
        if newSeq in dictinary_table:
            currentSeq = newSeq
        else:
            compressedData.append(dictinary_table[currentSeq])
            dictinary_table[newSeq] = startcode
            startcode += 1
            currentSeq = nextSymbol
            
    if currentSeq:
        compressedData.append(dictinary_table[currentSeq])
        
    return compressedData
    
# Function to deal with files only
def copressWithFile(inputFile,outputFile):
    
    # Read data from input file
    file = open(inputFile ,'r')
    data = file.read()
    file.close()
    
    compressed_data = Compress_LZW(data)
    
    # write compressed data in output file
    
    file = open(outputFile , 'w')
    file.write(str(compressed_data))
    file.close()
    
    print("Compressed Data Save at " + outputFile)
    


def Decompress_LZW(data):
    print("Decompressed Data : not added yet")
    
#  Testing without Files 
print("Test Function Compressed LZW techniques ^_^")
testData = input("Enter data to compressed it: ")
compressedDtata = Compress_LZW(testData)
print("Compressed Data: " ,compressedDtata)

# print("Test Function Decompressed LZW techniques ^_^")
# decompressedDtata = Decompress_LZW(compressedDtata)
# print("Decompressed Data: " ,decompressedDtata)

# with Files 

testInput = input("Enter Name of input File: ")
testOutput = input("Enter Name of output File: ")
copressWithFile(testInput , testOutput)



    