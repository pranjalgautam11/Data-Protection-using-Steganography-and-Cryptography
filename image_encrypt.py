from twofish import Twofish

def encrypt_image(input_image_path, output_encrypted_path, key):
    # Read image as binary data
    with open(input_image_path, 'rb') as f:
        image_data = f.read()

    # Pad the image data to make its size a multiple of 16 bytes
    padded_size = (len(image_data) + 15) // 16 * 16
    padded_data = image_data.ljust(padded_size, b'\0')
    
    # Initialize Twofish cipher with the provided key
    cipher = Twofish(key)

    # Encrypt image data
    encrypted_data = cipher.encrypt(padded_data)

    # Write encrypted data to a new file
    with open(output_encrypted_path, 'wb') as f:
        f.write(encrypted_data)
