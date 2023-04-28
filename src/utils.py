def bit_array(charset):
    binary_list = [bin(ord(char))[2:].zfill(8) for char in charset]
    return ''.join(binary_list)

def binary_to_char(binary_string, bits_per_char=8):
    if bits_per_char not in [7, 8]:
        raise ValueError("Bits per char must be either 7 or 8.")
    chars = []
    for i in range(0, len(binary_string), bits_per_char):
        binary_segment = binary_string[i:i+bits_per_char]
        decimal = int(binary_segment, 2)
        chars.append(chr(decimal))
    return ''.join(chars)