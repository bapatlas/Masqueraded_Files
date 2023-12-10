README file that includes information for both Windows and Mac users. This assumes that your Python script works on both platforms. Please adapt it according to your specific program and requirements.
# List Masqueraded Files 
## Introduction
This program goal is to detect masqueraded files within a specified folder. It compares the file extension with the file signature to identify potential discrepancies.
## Features
- Lists masqueraded files based on file extension and signature analysis.
- Supports specific file extensions: mp4, png, pdf, jpg.
## Prerequisites
- Python 3.x
- Operating System: Windows/Linux/Mac
## Installation
### Windows
1. Download and install Python from [python.org](https://www.python.org/).
2. Clone the repository:
   git clone https://github.com/bapatlas/Masqueraded_Files
3.	Navigate to the project directory:
cd Masqueraded_Files
4.	Run the program:
           python list_masqueraded_files.py 
5.	Enter the folder path when prompted.
   
Mac
1.	Mac typically comes with Python pre-installed. If not, you can install it using Homebrew.
brew install python 
2.	Clone the repository:
git clone https://github.com/bapatlas/Masqueraded_Files
3.	Navigate to the project directory:
cd Masqueraded_Files
4.	Run the program:
python3 list_masqueraded_files.py 
5.	Enter the folder path when prompted.
Program Logic
1.	Allowed Extensions: The program checks for masqueraded files with the extensions: mp4, png, pdf, jpg.
2.	File Signature Comparison: It compares the file extension with the file signature (first 8 bytes of the file).
3.	Output: The program lists files where the file extension and signature indicate a difference.
Example
Enter the folder path: /path/to/your/folder Masqueraded Files: 
/path/to/your/folder/masqueraded_file.jpg /path/to/your/folder/masqueraded_file.mp4 ... 
Troubleshooting
•	If the program is not working as expected, ensure that Python is installed, and the required dependencies are met.
•	Verify that the specified folder contains the expected file types.
Contributions
Contributions are welcome! If you find any issues or want to enhance the program, feel free to open an issue or create a pull request.
License
N/A
