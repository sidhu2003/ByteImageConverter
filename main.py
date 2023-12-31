import base64
from PIL import Image
import io

# def image_to_bytecode(image_path):
#     with open(image_path, "rb") as image_file:
#         image_bytecode = base64.b64encode(image_file.read())
#         return image_bytecode

# def bytecode_to_image(bytecode, output_path):
#     image_data = base64.b64decode(bytecode)

#     with open(output_path, "wb") as image_file:
#         image_file.write(image_data)


# image_path = input("Enter the path to your image file: ")


# encoded_bytecode = image_to_bytecode(image_path)
# print("Encoded Bytecode:", encoded_bytecode)


# output_path = input("Enter the path to your output image file: ")


# bytecode_to_image(encoded_bytecode, output_path)
# print(f"Decoded image saved to: {output_path}")

def image_to_binary(image_path):
    # Open the image file
    with open(image_path, "rb") as image_file:
        # Create a Pillow Image object
        img = Image.open(image_file)
        
        # Convert the image to binary data
        img_binary = io.BytesIO()
        img.save(img_binary, format="PNG")
        img_binary.seek(0)
        
        binary_data = img_binary.read()
        return binary_data

def binary_to_image(binary_data, output_path):
    # Create a Pillow Image object from binary data
    img_binary = io.BytesIO(binary_data)
    img = Image.open(img_binary)
    
    # Save the image to the specified output path
    img.save(output_path)

# Replace 'your_image_path.jpg' with the path to your image file
image_path = input("Enter the path to your image file: ")

# Convert the image to binary data
binary_data = image_to_binary(image_path)

# Print the first 50 bytes of the binary data as a sample
print("Binary data:", binary_data[:50])

# Replace 'output_image.jpg' with the desired output image file path
output_path = input("Enter the path to your output image file: ")

# Convert binary data back to an image and save it
binary_to_image(binary_data, output_path)
print(f"Image saved to: {output_path}")
