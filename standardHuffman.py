# 1. calculate propability

def calculate_probabilities(data):
    frequencies = {}
    
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    total_Length = len(data)
    
    probabilities = {}
    
    for char, freq in frequencies.items():
        probabilities[char] = freq / total_Length
            
    return probabilities


data = "bbbacacbcd"
probabilities = calculate_probabilities(data)
print("Character Probabilities:")
for char, prob in probabilities.items():
    print(f"'{char}': {prob:.4f}")


def decompress (compressedText,diction):
    dict = {}
    for key,value in diction.items():
        dict[value] = key
    pointer  =0
    character =""
    original_text =""
    while(pointer<len(compressedText)):
        character += compressedText[pointer]
        if(dict.get(character) is not None):
            original_text+= dict[character]
            character=""
        pointer+=1
    return original_text


print(decompress("0111011010",{'A':"0",'B':"11",'C':"10"}))

            
            