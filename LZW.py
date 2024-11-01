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
    
    
def Decompress_LZW(data):
    print("Decompressed Data : not added yet")
    
print("Test Function Compressed LZW techniques ^_^")
testData = input("Enter data to compressed it: ")
print(Compress_LZW(testData))

    