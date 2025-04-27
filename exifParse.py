import sys
import exifread

def main():
    if len(sys.argv) < 2:
        print("Error! - No Image File Specified!")
        sys.exit(1)

    filename = sys.argv[1]
    print(f"Source File: {filename}")

    try:
        with open(filename, 'rb') as f:
            tags = exifread.process_file(f)
    except FileNotFoundError:
        print("Error! - File Not Found!")
        sys.exit(1)

    # Extract EXIF tags safely
    make = tags.get('Image Make', 'Not Found')
    model = tags.get('Image Model', 'Not Found')
    timeval = tags.get('EXIF DateTimeOriginal', 'Not Found')

    # GPS info
    gps_latitude = tags.get('GPS GPSLatitude', 'Not Found')
    gps_latitude_ref = tags.get('GPS GPSLatitudeRef', 'Not Found')
    gps_longitude = tags.get('GPS GPSLongitude', 'Not Found')
    gps_longitude_ref = tags.get('GPS GPSLongitudeRef', 'Not Found')

    print("Camera Make:", make)
    print("Camera Model:", model)
    print("Original Date/Time:", timeval)

    if gps_latitude != 'Not Found' and gps_longitude != 'Not Found':
        print("Latitude:", gps_latitude, gps_latitude_ref)
        print("Longitude:", gps_longitude, gps_longitude_ref)
    else:
        print("GPS Info: Not Found")

if __name__ == "__main__":
    main()
