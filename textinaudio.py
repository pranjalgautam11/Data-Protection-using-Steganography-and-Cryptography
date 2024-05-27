import wave
import os
from audio_encrypt import encryption
from audio_decrypt import decryption
import time
from memory_profiler import memory_usage

folder_path = 'Encrypted_text_in_audio/'

# Using a 32-byte key for encryption
key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f' * 2  # Example 32-byte key

def encode_aud_data():
    name = input("Enter name of the file (with extension): ")
    nameoffile = os.path.join(folder_path, name)
    song = wave.open(nameoffile, mode='rb')

    nframes = song.getnframes()
    frames = song.readframes(nframes)
    frame_list = list(frames)
    frame_bytes = bytearray(frame_list)

    data = input("\nEnter the secret message: ")

    encoded = input("Enter name of the stego file (with extension): ")
    stegofile = os.path.join(folder_path,encoded)

    # Start time with higher resolution
    start_time = time.perf_counter()

    res = ''.join(format(i, '08b') for i in bytearray(data, encoding='utf-8'))
    length = len(res)

    data = data + '*^*^*'

    result = []
    for c in data:
        bits = bin(ord(c))[2:].zfill(8)
        result.extend([int(b) for b in bits])

    j = 0
    for i in range(len(result)):
        res = bin(frame_bytes[j])[2:].zfill(8)
        if res[-4] == str(result[i]):
            frame_bytes[j] = (frame_bytes[j] & 253)
        else:
            frame_bytes[j] = (frame_bytes[j] & 253) | 2
            frame_bytes[j] = (frame_bytes[j] & 254) | result[i]
        j += 1

    frame_modified = bytes(frame_bytes)

    
    with wave.open(stegofile, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    print("Encoded the data successfully in the audio file.")
    print("Encrypting the encoded audio file.")
    encryption(stegofile,key)

    # End time with higher resolution
    end_time = time.perf_counter()
    # Calculate total time taken
    time_taken = end_time - start_time

    print(f"Time taken to Encrypt tect in audio: {time_taken:.2f} seconds")

    song.close()

def decode_aud_data():
    encrypted_path = input("Enter name of the file to be decrypted :- ")
    encrypted_audio_file = os.path.join(folder_path,encrypted_path)

    # Start time with higher resolution
    start_time = time.perf_counter()

    decryption(encrypted_audio_file,key)

    decoded_file = input("Enter name of the file to be decoded :- ")
    nameoffile = os.path.join(folder_path,decoded_file)
    song = wave.open(nameoffile, mode='rb')

    nframes=song.getnframes()
    frames=song.readframes(nframes)
    frame_list=list(frames)
    frame_bytes=bytearray(frame_list)

    extracted = ""
    p=0
    for i in range(len(frame_bytes)):
        if(p==1):
            break
        res = bin(frame_bytes[i])[2:].zfill(8)
        if res[len(res)-2]==0:
            extracted+=res[len(res)-4]
        else:
            extracted+=res[len(res)-1]
    
        all_bytes = [ extracted[i: i+8] for i in range(0, len(extracted), 8) ]
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "*^*^*":
                print("The Encoded data was :--",decoded_data[:-5])
                p=1
                break  
    
    # End time with higher resolution
    end_time = time.perf_counter()
    # Calculate total time taken
    time_taken = end_time - start_time

    print(f"Time taken to decrypt hidden text: {time_taken:.2f} seconds")

def aud_steg():
    while True:
        print("\n\t\tAUDIO STEGANOGRAPHY OPERATIONS")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        choice1 = int(input("Enter the Choice: "))
        if choice1 == 1:
            mem_usage = memory_usage(encode_aud_data)
            print(f"Memory used for encrypting: {max(mem_usage)} MiB")
        elif choice1 == 2:
            mem_usage = memory_usage(decode_aud_data)
            print(f"Memory used for decrypting: {max(mem_usage)} MiB")
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
