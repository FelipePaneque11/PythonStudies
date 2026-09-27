try:   
    with open("users.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission to access the file.")
except OSError:
    print("There is an OS error")
except IsADirectoryError:
    print("Directory Error.")    
except Exception as e:
    print(f"An unexpected error has occured: {e} ")
finally:
    print("After everything, executes this...")