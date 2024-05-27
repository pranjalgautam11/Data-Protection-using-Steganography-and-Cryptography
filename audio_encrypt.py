from twofish import Twofish  # Make sure the Twofish class is correctly defined in 'twofish.py'

def read_audio_file(filename):
    try:
        with open(filename, 'rb') as f:
            audio_data = f.read()
        return audio_data
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

def write_encrypted_audio_file(filename, encrypted_data):
    try:
        with open(filename, 'wb') as f:
            f.write(encrypted_data)
    except IOError as e:
        print(f"Error writing file: {e}")

def encrypt_audio(audio_data, key):
    try:
        twofish_cipher = Twofish(key)
        encrypted_data = twofish_cipher.encrypt(audio_data)
        return encrypted_data
    except Exception as e:
        print(f"Encryption failed: {e}")
        return None

def encryption(audio_file, key):
    audio_data = read_audio_file(audio_file)
    if audio_data is None:
        return

    # Ensuring the data length is multiple of 16
    padded_data_length = (len(audio_data) + 15) // 16 * 16
    padded_audio_data = audio_data.ljust(padded_data_length, b'\0')

    encrypted_audio_data = encrypt_audio(padded_audio_data, key)
    if encrypted_audio_data is None:
        return

    encrypted_audio_file = 'C:\\Users\\admin\\Desktop\\PROJECTS\\CNS\\Encrypted_text_in_audio\\encrypted_audio.enc'
    write_encrypted_audio_file(encrypted_audio_file, encrypted_audio_data)

    print("Audio file encrypted successfully!")