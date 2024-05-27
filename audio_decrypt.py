from twofish import Twofish

def read_audio_file(filename):
    try:
        with open(filename, 'rb') as f:
            audio_data = f.read()
        return audio_data
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

def decrypt_audio(encrypted_data, key):
    try:
        twofish_cipher = Twofish(key)
        decrypted_data = twofish_cipher.decrypt(encrypted_data)
        return decrypted_data
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None

def write_decrypted_audio_file(filename, decrypted_data):
    try:
        with open(filename, 'wb') as f:
            f.write(decrypted_data)
    except IOError as e:
        print(f"Error writing file: {e}")

def decryption(encrypted_audio_file,key):
    encrypted_audio_data = read_audio_file(encrypted_audio_file)
    if encrypted_audio_data is None:
        return

    decrypted_audio_data = decrypt_audio(encrypted_audio_data, key)
    if decrypted_audio_data is None:
        return

    decrypted_audio_file = 'C:\\Users\\admin\\Desktop\\PROJECTS\\CNS\\Encrypted_text_in_audio\\decrypted_audio.wav'
    write_decrypted_audio_file(decrypted_audio_file, decrypted_audio_data)

    print("Audio file decrypted successfully!")
