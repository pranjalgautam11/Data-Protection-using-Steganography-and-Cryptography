from twofish import Twofish

def decrypt_image(input_encrypted_path, output_image_path, key):
    # Read encrypted data from file
    with open(input_encrypted_path, 'rb') as f:
        encrypted_data = f.read()

    # Initialize Twofish cipher with the provided key
    cipher = Twofish(key)

    # Decrypt encrypted data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write decrypted data to a new file
    with open(output_image_path, 'wb') as f:
        f.write(decrypted_data)