from stegano import lsb
from PIL import Image
from image_encrypt import encrypt_image
from image_decrypt import decrypt_image
import os
import time
from memory_profiler import memory_usage

def encode_image(source_image_path, secret_image_path, output_image_path):
    # Open images using PIL
    source_image = lsb.hide(source_image_path, secret_image_path)
    source_image.save(output_image_path)

def decode_image(encoded_image_path, output_secret_image_path):
    # Use lsb.reveal to get the hidden message
    secret_message = lsb.reveal(encoded_image_path)

    # Create an image from the decoded message (assuming it's a valid image format)
    decoded_image = Image.open(secret_message)

    # Save the decoded image
    decoded_image.save(output_secret_image_path)

folder_path = 'Encrypted_image_in_image/'  # Modify this with your folder path

def encrypt():
    source_image_path = input("Enter cover image name: ")
    simg = os.path.join(folder_path, source_image_path)

    secret_image_path = input("Enter secret image path: ")
    secret_img = os.path.join(folder_path, secret_image_path)

    output_image_path = input("Enter encoded image path: ")
    oimg = os.path.join(folder_path, output_image_path)

    # Start time with higher resolution
    start_time = time.perf_counter()
    
    encode_image(simg, secret_img, oimg)

    encrypted_path = input("Enter name for encrypted image: ")
    eimg = os.path.join(folder_path, encrypted_path)

    encrypt_key =  b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    encrypt_image(oimg, eimg, encrypt_key)

    # End time with higher resolution
    end_time = time.perf_counter()
    # Calculate total time taken
    time_taken = end_time - start_time

    print("Encrypted image is saved as " + encrypted_path)
    print(f"Time taken to Encrypt image in image: {time_taken:.2f} seconds")

def decrypt():
    encrypted_path = input("Enter name for encrypted image: ")
    encrypted_path = os.path.join(folder_path,encrypted_path)
    img = 'Encrypted_image_in_image\decrypted_hidden_message.jpg'
    decrypt_key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    
    # Start time with higher resolution
    start_time = time.perf_counter()
    
    decrypt_image(encrypted_path, img, decrypt_key)
    decode_image(img, 'Encrypted_image_in_image\decoded_secret_image.png')

    # End time with higher resolution
    end_time = time.perf_counter()
    # Calculate total time taken
    time_taken = end_time - start_time

    print(f"Time taken to decrypt hidden image: {time_taken:.2f} seconds")


def image_steg():
    while True:
        print("\n\t\t:: IMAGE IN IMAGE STEGANOGRAPHY OPERATIONS ::\n")
        print("1. Encode the Image ")
        print("2. Decode the Image ")
        print("3. Exit")
        choice = int(input("Enter the Choice: "))
        if choice == 1:
            mem_usage = memory_usage(encrypt)
            print(f"Memory used for encrypting: {max(mem_usage)} MiB")
        elif choice == 2:
            mem_usage = memory_usage(decrypt)
            print(f"Memory used for decrypting: {max(mem_usage)} MiB")
        elif choice == 3:
            break
        else:
            print("Incorrect Choice")

