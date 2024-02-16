# Inputs

message = input("Input message to encode:")
shift = input("Input shift ammount:")
new_shift = int(shift)
# Result Placeholder
result = ""




# Go throught each letter in message
for char in message.upper():
        if char.isalpha():
            # Convert to ASCIIHello
            char_code = ord(char)
            new_char_code = char_code + new_shift
            
            if new_char_code > 90:
                new_char_code -= 26
            new_char = chr(new_char_code)
            
            result += new_char
        else:
            result += char
print(result)