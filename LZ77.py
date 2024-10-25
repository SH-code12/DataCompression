print("Shahd Elnassag ^_^\n Welcome ^_^ ")



def Decompress_LZ77(Compress_LZ77):
    
    # array store Decompressed Data
    Decompress_Data = []
    
    for position ,length,nextSymbol in Compress_LZ77:
        # exist match! substring match string and add it to Decompressed Data
        if position > 0 :
            startIndex = len(Decompress_Data) - position
            
            Decompress_Data += Decompress_Data[startIndex : startIndex + length]
                        
        # Add char direct if position = 0
        Decompress_Data += nextSymbol
        
        # ' ' to print characters with space 
        
    return ' '.join(Decompress_Data)


compressed_data = [(0, 0, 'A'), (0, 0, 'B'), (2, 1, 'A'), (3, 2, 'B'), (5, 3, 'B'), (2, 2, 'B'), (5, 5, 'B'), (1 ,1 , 'A')]
decompressed = Decompress_LZ77(compressed_data)
print("Decompressed Data Using LZ77 Technique:", decompressed)

