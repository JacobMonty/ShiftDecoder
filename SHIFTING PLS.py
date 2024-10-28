#Shift Cypher Decoder

#indput
Cypher = input("Please enter the Cypher: ")

print("Starting Cypher = " + Cypher)

def shifting(char, shift):
    return chr(((ord(char) - ord('a') + shift) % 26) +ord('a'))

for i in range (1, 26):
    SHIFT = ''.join(shifting(char, i) for char in Cypher)
    print(f"Shift {i}: " + SHIFT)

    
