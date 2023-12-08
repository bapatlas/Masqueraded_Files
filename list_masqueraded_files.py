import os

def list_masqueraded_files(folder_path):
    # List to store masqueraded files
    masqueraded_files = []

    # Allowed file extensions and corresponding signatures
    allowed_extensions = {
        'mp4': b'\x00\x00\x00\x00\x00\x00\x00\x18',
        'png': b'\x89PNG\r\n\x1a\n',
        'pdf': b'%PDF-',
        'jpg': b'\xff\xd8\xff'
    }

    # Iterate through files in the specified folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Get the file signature (first 8 bytes of the file)
            with open(file_path, 'rb') as f:
                file_signature = f.read(8)

            # Extract the file extension from the file name
            file_extension = os.path.splitext(file_name)[1][1:].lower()

            # Check if the file extension is in the allowed list
            if file_extension in allowed_extensions:
                # Compare file extension with file signature
                if allowed_extensions[file_extension] not in file_signature:
                    masqueraded_files.append(file_path)

    return masqueraded_files

# Take input folder path from the user
folder_path = input("Enter the folder path: ")

masqueraded_files = list_masqueraded_files(folder_path)

if masqueraded_files:
    print("Masqueraded Files:")
    for file_path in masqueraded_files:
        print(file_path)
else:
    print("No masqueraded files found.")
