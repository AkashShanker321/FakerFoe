import cv2
import numpy as np

def compare_quantization_tables(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Extract quantization tables
    quantization_tables = []
    for i in range(2):
        # Read the JPEG image and extract the quantization table
        jpeg_data = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])[1].tobytes()
        quantization_table = extract_quantization_table(jpeg_data)
        quantization_tables.append(quantization_table)

    # Compare quantization tables
    similarity_score = calculate_similarity_score(quantization_tables[0], quantization_tables[1])

    # Determine if double compression is detected
    if similarity_score < threshold:
        print("Double JPEG compression detected!")
    else:
        print("No double JPEG compression detected.")

def extract_quantization_table(jpeg_data):
    # Extract quantization table from JPEG data
    # ... implementation specific to extracting quantization table from JPEG data ...
    return quantization_table

def calculate_similarity_score(quantization_table1, quantization_table2):
    # Calculate the similarity score between two quantization tables
    # ... implementation specific to calculating similarity score ...
    return similarity_score
