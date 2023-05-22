from PIL import Image, ImageChops, ImageEnhance

def calculate_ela(image_path):
    # Load the original image
    original_image = Image.open(image_path)

    # Perform Error Level Analysis
    ela_image = original_image.copy()

    # Calculate the absolute difference between the original and ELA images
    ela_diff = ImageChops.difference(original_image, ela_image)

    # Convert the difference image to grayscale
    ela_diff = ela_diff.convert("L")

    # Normalize the ELA image for visualization
    ela_normalized = ImageEnhance.Contrast(ela_diff).enhance(2.0)

    # Save the ELA image
    ela_normalized.save("ela.jpg")

    # Return the ELA image
    return ela_normalized
