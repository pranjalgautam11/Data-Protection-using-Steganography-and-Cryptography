from textinaudio import aud_steg
from textinimage import incript
from imageinimage import image_steg


def main():
    while True:
        print("Welcome to Steganography and Cryptography Portal\n")
        choice = input(" Enter 1: text in audio\n Enter 2: text in image\n Enter 3: image in image\n Enter 0: Exit\nChoice: ")
        if choice == '1':
            aud_steg()
        elif choice == '2':
            incript()
        elif choice == '3':
            image_steg()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()