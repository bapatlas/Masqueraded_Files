# Masqueraded Files Detector
A python program that lists all the masqueraded files in any given folder. This is accomplished by the program checking "the file signature" and comparing it with the file's extension in it's name. If the file extension and the file signature indicates a difference, the program must output the file's path. 
Masqueraded Files Detector
Overview
This Python script, list_masqueraded_files.py, is designed to identify masqueraded files within a specified folder. Masqueraded files are those whose file extensions do not match their actual file signatures. The script compares the allowed file extensions with the first 8 bytes (file signature) of each file to determine if there is a discrepancy.
Features
•	Finds masqueraded files based on allowed file extensions and signatures.
•	Provides a simple command-line interface for user interaction.
•	Outputs the paths of masqueraded files found in the specified folder.
Prerequisites
•	Python installed on your machine.
Installation
1.	Clone the repository to your local machine:
bashCopy code
           git clone https://github.com/bapatlas/Masqueraded_Files 
2.	Navigate to the project directory:
bashCopy code
cd masquerade-detector 
Usage
1.	Run the script by executing the following command:
bashCopy code
python masquerade_detector.py 
2.	Enter the path to the folder you want to scan when prompted.
3.	Observe the script's output, which will display the paths of masqueraded files found.
Example
bashCopy code
Enter the folder path: /path/to/your/folder
Masqueraded Files: /path/to/your/folder/masqueraded_file.jpg
                  /path/to/your/folder/masqueraded_file.mp4 
                  /path/to/your/folder/masqueraded_file.pdf
  	             /path/to/your/folder/masqueraded_file.png 
Notes
•	Ensure that the folder you are scanning contains the file types you want to test (jpg, mp4, pdf, png).
•	The script compares file extensions and signatures for the specified file types.
Contribution 
