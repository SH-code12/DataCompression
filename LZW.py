print("Shahd Elnassag ^_^")

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
def compressWithFile(inputFile,outputFile):
    
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
    text =""
    start = 256
    start_encode =0
    dictionary ={}
    for i in range(0,len(data)):
        num = data[i]
        if num< 256:
            text += chr(num)
            if (i>0):
                dictionary[start] = str (text[start_encode:])
                start_encode = len(text)-1;
                start+=1
        elif num >=start:
            s =text[start_encode:] + text[start_encode]
            text +=  s
            dictionary[start] = str(s)
            start_encode = len(text)-(len(s))
            start+=1
        else:
            s = text[start_encode:]
            text += str(dictionary[num])
            dictionary[start]=  s + dictionary[num][0]
            start_encode = len(text) -(len(dictionary[num]) )
            start+=1
    return text
# Deal with Files
def DecompressWithFile(inputFile,outputFile):
    
    # Read data from input file
    file = open(inputFile ,'r')
    data = file.read()
    file.close()
    
    # convert string to integer
    data = eval(data)
    
    decompressed_data = Decompress_LZW(data)
    
    # write compressed data in output file
    
    file = open(outputFile , 'w')
    file.write(str(decompressed_data))
    file.close()
    
    print("Decompressed Data Save at " + outputFile)
    
#Testing without Files
print("Test Function Compressed LZW techniques ^_^")
testData = input("Enter data to compressed it: ")
compressedDtata = Compress_LZW(testData)
print("Compressed Data: " ,compressedDtata)

print("Test Function Decompressed LZW techniques ^_^")

decompressedDtata = Decompress_LZW(compressedDtata)
print("Decompressed Data: " ,decompressedDtata)

if(decompressedDtata == testData):
    print("GOOD JOBBB ya maloka")

# with Files

testInput = input("Enter Name of input File: ")
outputCompress = input("Enter Name of output of Compressed Data File: ")
outputDecompress = input("Enter Name of output of Compressed Data File: ")
compressWithFile(testInput , outputCompress)
DecompressWithFile(outputCompress,outputDecompress)






