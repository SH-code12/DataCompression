print("Shahd Elnassag ^_^\n Welcome ^_^ ")

def Compress(data):
    search_window_length =int( 0.4 * len(data))
    look_ahead_window_length = int(0.3 *len(data))
    code=[]
    for current_pointer in range(0, len(data),1):
        back_pointer = max(0,current_pointer-search_window_length)
        still_max_search = min(current_pointer+ look_ahead_window_length,len(data))
        counter =0
        max_match =0
        I_go_backed_for = 0
        next_char = data[current_pointer]
        temp_pointer = current_pointer
        while(back_pointer<temp_pointer and current_pointer<still_max_search):
            if(data[back_pointer]==data[current_pointer]):
                current_pointer+=1
                counter+=1
            else:
                if(counter>max_match):
                    max_match = counter
                    I_go_backed_for = temp_pointer-back_pointer-counter
                    next_char = data[current_pointer]
                current_pointer = temp_pointer
                counter =0

            back_pointer+=1
    code.append((I_go_backed_for,max_match,next_char))
    return code



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
        
    return ''.join(Decompress_Data)


compressed_data = [(0, 0, 'A'), (0, 0, 'B'), (2, 1, 'A'), (3, 2, 'B'), (5, 3, 'B'), (2, 2, 'B'), (5, 5, 'B'), (1 ,1 , 'A')]
TestSpace = [(0, 0, 's'), (0, 0, 'h'), (0, 0, 'a'), (2, 1, 'd'), (0, 0, ' '), (0, 0, 'm'), (0, 0, 'o'), (5, 1, 'a'),(4, 1, 'e'), (8, 1, '')]

decompressed = Decompress_LZ77(TestSpace)
print("Decompressed Data Using LZ77 Technique:", decompressed)


# Mytext = "ABBBBAB"
# mycode = Compress(Mytext)
# for code3 in mycode:
#     print(code3)


