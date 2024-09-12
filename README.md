File Management App

Description:
This Python application provides a simple command-line interface for managing files in the current directory. It allows users to create, view, delete, read, and edit files. This tool is useful for basic file operations and learning about file handling in Python.

Features:
Create a New File: Create a new file with a specified name.
View All Files: List all files in the current directory.
Delete a File: Delete a file by name.
Read a File: Display the contents of a file.
Edit a File: Append content to an existing file.
Exit: Close the application.

Requirements:
Python 3.x

Usage:
Clone the Repository
If you have Git installed, you can clone this repository using:
Copy code = https://github.com/Chauhan0047/File-Management-App
 
Run the Application:
Ensure you have Python 3 installed. Navigate to the directory containing app.py and run:

Copy code = python app.py

Choose an Option:
Follow the on-screen prompts to choose an action:

1 to create a new file
2 to view all files
3 to delete a file
4 to read a file
5 to edit a file
6 to exit the application

Functions:

create_file(filename)
Creates a new file with the given filename. If the file already exists, an error message is shown.

view_all_files()
Lists all files in the current directory. If no files are found, it displays a corresponding message.

delete_file(filename)
Deletes the file specified by filename. If the file does not exist, an error message is shown.

read_file(filename)
Reads and displays the content of the file specified by filename. If the file does not exist, an error message is shown.

edit_file(filename)
Appends new content to the file specified by filename. If the file does not exist, an error message is shown.

Error Handling:
The application handles various file-related errors, including:

FileAlreadyExistsError: When trying to create a file that already exists.
FileNotFoundError: When trying to delete, read, or edit a file that does not exist.
Other Exceptions: General errors are caught and displayed with a message.

Contributing:
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code is well-tested and follows the existing code style.
