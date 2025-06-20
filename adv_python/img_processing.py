import cv2
import numpy as np
import os

def image_compression(image,input_path, output_path="compressed_image.jpg"):
    quality = int(input("Enter the Compression value(0 to 100): "))
    cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    print(f"Compressed image saved to {output_path} with quality = {quality}")
    
    compressed = cv2.imread(output_path)

    #before compression
    if os.path.exists(input_path):
        original_size = os.path.getsize(input_path) / 1024  # KB
        print(f"File size [Before Compression] : {original_size:.2f} KB")

    #after compression
    if os.path.exists(output_path):
        compressed_size = os.path.getsize(output_path) / 1024  # KB
        print(f"File size [After Compression] : {compressed_size:.2f} KB")
    return compressed

def read_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Cannot open image at path: {path}")
    return image

def save_image(path, image):
    cv2.imwrite(path, image)
    print(f"Processed image saved to {path}")

def color_enhancing(image, alpha=1.6, beta=20):
    enhanced = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return enhanced

def black_and_white(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def negative(image):
    return cv2.bitwise_not(image)

def blur_image(image, ksize=(5, 5)):
    return cv2.GaussianBlur(image, ksize, 5)

def rotate_image(image):
    angle = int(input("Enter Rotation Angle(90,180,270) in deg : "))       
    if angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        raise ValueError("Only 90, 180, 270 degrees supported.")
    
def pencil_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

def mirror_flip(image):
    print("0 - Vertical \n1 - Horizontal")
    direction = int(input("Enter Flip Direction : "))
    if direction == 1:
        return cv2.flip(image, 1)  # Left-right flip
    elif direction == 0:
        return cv2.flip(image, 0)  # Top-bottom flip
    else:
        raise ValueError("Direction must be 'horizontal', 'vertical', or 'both'")

def main():
    input_path = input("Enter the path of the image: ")
    try:
        image = read_image(input_path)
        print("\nChoose an operation:")
        print("1. Image Compression ")
        print("2. Pencil Sketch")
        print("3. Black and white")
        print("4. Negative")
        print("5. Blur")
        print("6. Color Enhancing")
        print("7. Rotate Image")
        print("8. Image Flipping")
        print()
        choice = input("Enter your choice : ")
        print()
        if choice == '1':
            processed = image_compression(image,input_path)
            output_path = "Compressed_image.jpg"
        elif choice == '2':
            processed = pencil_sketch(image)
            output_path = "pencil_sketch.jpg"  
        elif choice == '3':
            processed = black_and_white(image)
            output_path = "grayscale_image.jpg"
        elif choice == '4':
            processed = negative(image)
            output_path = "inverted_image.jpg"
        elif choice == '5':
            processed = blur_image(image)
            output_path = "blurred_image.jpg"
        elif choice == '6':
            processed  = color_enhancing(image)
            output_path = "color_enhanced_image.jpg"
        elif choice == '7':
            processed = rotate_image(image)
            output_path = "rotated_image.jpg"    
        elif choice == '8':
            processed = mirror_flip(image)
            output_path = "flipped_image.jpg"
        else:
            print("Invalid choice. Exiting.")
            return

        save_image(output_path, processed)
    except Exception as e:
        print(f"Error: {e}")

main()