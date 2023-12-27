import base64

def image_to_bytecode(image_path):
    with open(image_path, "rb") as image_file:
        image_bytecode = base64.b64encode(image_file.read())
        return image_bytecode

def bytecode_to_image(bytecode, output_path):
    image_data = base64.b64decode(bytecode)

    with open(output_path, "wb") as image_file:
        image_file.write(image_data)


image_path = input("Enter the path to your image file: ")


encoded_bytecode = image_to_bytecode(image_path)
print("Encoded Bytecode:", encoded_bytecode)


output_path = input("Enter the path to your output image file: ")


bytecode_to_image(encoded_bytecode, output_path)
print(f"Decoded image saved to: {output_path}")
