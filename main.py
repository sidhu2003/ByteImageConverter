import base64

def image_to_bytecode(image_path):
    with open(image_path, "rb") as image_file:
        # Read the image file in binary mode
        image_bytecode = base64.b64encode(image_file.read())
        return image_bytecode

def bytecode_to_image(bytecode, output_path):
    # Decode the base64-encoded data
    image_data = base64.b64decode(bytecode)

    # Write the binary data back to an image file
    with open(output_path, "wb") as image_file:
        image_file.write(image_data)

# Replace 'your_image_path.jpg' with the path to your image file
image_path = input("Enter the path to your image file: ")

# Encode the image to bytecode
encoded_bytecode = image_to_bytecode(image_path)
print("Encoded Bytecode:", encoded_bytecode)

# Replace 'output_image.jpg' with the desired output image file path
output_path = input("Enter the path to your output image file: ")

# Decode the bytecode back to an image
bytecode_to_image(encoded_bytecode, output_path)
print(f"Decoded image saved to: {output_path}")
