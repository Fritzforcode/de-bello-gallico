from PIL import Image, ImageDraw, ImageFont

def calculate_text_dimensions(text, font_path="arial.ttf", font_size=24):
    """
    Calculate the dimensions of the given text using the specified font.

    Args:
        text (str): The text to measure.
        font_path (str): Path to the .ttf font file.
        font_size (int): Font size to use.

    Returns:
        tuple: Width and height of the text in pixels.
    """
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()  # Fallback if the specified font is not available

    # Create a dummy image to measure text size
    image = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:4]  # Use textbbox for accurate size

    return text_width, text_height

def calculate_scaling_factors(actual_width, actual_height, penguinmod_width, penguinmod_height):
    """
    Calculate scaling factors based on PenguinMod dimensions.

    Args:
        actual_width (float): The width of the text calculated by this script.
        actual_height (float): The height of the text calculated by this script.
        penguinmod_width (float): The width of the text in PenguinMod.
        penguinmod_height (float): The height of the text in PenguinMod.

    Returns:
        tuple: Width and height scaling factors.
    """
    width_factor = penguinmod_width / actual_width
    height_factor = penguinmod_height / actual_height

    return width_factor, height_factor

if __name__ == "__main__":
    # Example usage
    width_factors = []
    height_factors = []
    while True:
        try:
            text = input("Enter the text to measure: ")
            font_size = int(input("Enter the font size (e.g., 24): "))

            # Calculate dimensions using PIL
            actual_width, actual_height = calculate_text_dimensions(text, font_size=font_size)
            print(f"Calculated dimensions: {actual_width}px by {actual_height}px")

            # Get PenguinMod dimensions
            penguinmod_width = float(input("Enter the PenguinMod width: "))
            penguinmod_height = float(input("Enter the PenguinMod height: "))

            # Calculate scaling factors
            width_factor, height_factor = calculate_scaling_factors(
                actual_width, actual_height, penguinmod_width, penguinmod_height
            )
            width_factors.append(width_factor)
            height_factors.append(height_factors)
            print(f"Scaling factors:\n  Width: {width_factor:.2f}\n  Height: {height_factor:.2f}")
        except SyntaxError:
            print("SyntaxError")
        except KeyboardInterrupt:
            print("->", width_factors, height_factors)

#Hello There!