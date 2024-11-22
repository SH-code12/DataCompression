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
            
            