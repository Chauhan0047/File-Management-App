import os

def create_file(filename):
  try:
    with open(filename, 'x') as f:
       print(f"File name {filename} created successfully")
  except FileExistsError:
    print(f"Error: File {filename} already exists")
  except Exception as E:
    print("An error occurred: ")

def view_all_files():
  files = os.listdir()
  if not files:
    print("No files found")
  else:
    print("All files in the current directory:")
    for file in files:
      print(file)

def delete_file(filename):
  try:
    os.remove(filename)
    print(f"File {filename} deleted successfully")
  except FileNotFoundError:
    print(f"Error: File {filename} not found")
  except Exception as E:
    print("An error occurred: ")

def read_file(filename):
  try:
    with open(filename, 'r') as f:
      content = f.read()
      print(f"content of '{filename}' :\n{content}")
  except FileNotFoundError:
    print(f"Error: File {filename} not found")
  except Exception as E:
    print("An error occurred: ")

def edit_file(filename):
  try:
    with open(filename, 'a') as f:
     new_content = input("Enter new content: ")
     f.write(new_content + "\n") 
    print(f"Content of '{filename}' edited successfully")
  except FileNotFoundError:
    print(f"Error: File {filename} not found")
  except Exception as E:
    print("An error occurred: ")
  
def main():
  print("Welcome to the File Management App!")
  while True:
    print("\nChoose an option:")
    print("1. Create a new file")
    print("2. View all files")
    print("3. Delete a file")
    print("4. Read a file")
    print("5. Edit a file")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
      filename = input("Enter the name of the file: ")
      create_file(filename)

    elif choice == '2':
      view_all_files()

    elif choice == '3':
      filename = input("Enter the name of the file to delete: ")
      delete_file(filename)

    elif choice == '4':
      filename = input("Enter the name of the file to read: ")
      read_file(filename)

    elif choice == '5':
      filename = input("Enter the name of the file to edit: ")
      edit_file(filename)

    elif choice == '6':
      print("Exiting the File Management App...")
      break

    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()

