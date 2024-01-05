from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import webbrowser

def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal_degrees = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    if direction == 'S' or direction == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def extract_gps_info(image_path):
    img = Image.open(image_path)

    # Extract EXIF data
    exif_data = img._getexif()

    # Check if GPSInfo tag is present in the EXIF data
    if 0x8825 in exif_data:
        gps_info = exif_data[0x8825]

        # Convert GPS coordinates from degrees, minutes, seconds to decimal
        latitude = dms_to_decimal(gps_info[2][0], gps_info[2][1], gps_info[2][2], gps_info[3])
        longitude = dms_to_decimal(gps_info[4][0], gps_info[4][1], gps_info[4][2], gps_info[5])

        return latitude, longitude
    else:
        return None

# Example usage
image_path = "pic2.jpg"  # Replace with the actual path to your image
location = extract_gps_info(image_path)

if location:
    print(f"Location: Latitude {location[0]}, Longitude {location[1]}")

    # Open Google Maps with the extracted location
    maps_url = f"https://www.google.com/maps?q={location[0]},{location[1]}"
    webbrowser.open(maps_url)
else:
    print("Location information not found.")
