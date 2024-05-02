
FILEPATH = "todo.txt"
def get_todos(filepath = FILEPATH):
    """Reads the todo list from a file and returns it as a list of strings"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Writes the todos list to a file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions.py")