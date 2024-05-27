from PIL import Image
from twofish import Twofish
from image_encrypt import encrypt_image
from image_decrypt import decrypt_image
import os
import time
from memory_profiler import memory_usage

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
    # list of binary codes
    # of given data
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):
        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1

        # Eighth pixel of every set tells
        # whether to stop or read further.
        # 0 means keep reading; 1 means stop
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in modPix(newimg.getdata(), data):
        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

folder_path = 'Encrypted_text_in_image/'  # Modify this with your folder path

# Encode data into image
def encode():
    # Prompt for image name
    inputimage = input("Enter image name (with extension) : ")
    img = os.path.join(folder_path, inputimage)
    image = Image.open(img, 'r')
    image.show()

    # Prompt for data to be encoded
    data = input("Enter data to be encoded : ")
    if len(data) == 0:
        raise ValueError('Data is empty')

    newimg = image.copy()

    # Prompt for the name of the new encoded image
    new_img_name = input("Enter the name of the new image (with extension) : ")
    new_img_path = os.path.join(folder_path, new_img_name)

    # Start time with higher resolution
    start_time = time.perf_counter()

    encode_enc(newimg, data)
    newimg.save(new_img_path, str(new_img_name.split(".")[1].upper()))
    print(f"Image successfully encoded and saved as {new_img_name}")
    output_encrypted_path = 'Encrypted_text_in_image\encrypted.enc'
    key =  b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'  # Example key (32 bytes)

    encrypt_image(new_img_path, output_encrypted_path, key)
    print(f"Image successfully encrypted and saved as {output_encrypted_path}")

    # End time with higher resolution
    end_time = time.perf_counter()

    # Calculate total time taken
    time_taken = end_time - start_time

    print(f"Time taken to Encrypt text in image: {time_taken:.2f} seconds")

# Decode the data in the image
def decode():
    input_encrypted_path = 'Encrypted_text_in_image/encrypted.enc'
    img_path= input("Enter the name of image(decrypted) you want save with(with extension) : ")
    img = os.path.join(folder_path, img_path)
    sample_key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    # Start time with higher resolution
    start_time = time.perf_counter()

    decrypt_image(input_encrypted_path, img, sample_key)

    # img = input("Enter image name (with extension) : ")
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            # End time with higher resolution
            end_time = time.perf_counter()

            # Calculate total time taken
            time_taken = end_time - start_time

            print("Decoded Word :  " + data)
            print(f"Time taken to decrypt the hidden text: {time_taken:.2f} seconds")
            return data

# Main Function
def incript():
    while True:
        print("\n\t\t:: TEXT IN IMAGE STEGANOGRAPHY OPERATIONS ::\n")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        choice1 = int(input("Enter the Choice: "))
        if choice1 == 1:
            mem_usage = memory_usage(encode)
            print(f"Memory used for encoding: {max(mem_usage)} MiB")
        elif choice1 == 2:
            mem_usage = memory_usage(decode)
            print(f"Memory used for decoding: {max(mem_usage)} MiB")
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")

# Call the main function
