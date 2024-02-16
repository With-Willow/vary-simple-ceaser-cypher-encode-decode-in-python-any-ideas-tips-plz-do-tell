# Inputs

message = input("Input message to decode:")
shift = 7

# Result Placeholder
result = ""

# Go throught each letter in message
for char in message.upper():
        if char.isalpha():
            # Convert to ASCII
            char_code = ord(char)
            new_char_code = char_code - shift
            
            if new_char_code < 65:
                new_char_code += 26
            new_char = chr(new_char_code)
            
            result += new_char
        else:
            result += char
print(result)