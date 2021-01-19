import os
import sys
import venv
from create_dir_tree import Directory, create_tree


# Default sub directories in project directory
DEFAULT_FOLDERS = ['app', 'app\\templates', 'app\\static']

# Default files in project directory
DEFAULT_FILES = ['run.py', 'config.py', 'app\\__init__.py']

# Set True to create virtual environment in main project directory
CREATE_VENV = True


def get_path():
    '''
    Defines the path of the main project directory based on sys.argv inputs

        sys.argv[1] =>  Name of main project directory
        sys.argv[2] =>  Path of parent directory

    '''
    try:
        directory = sys.argv[1]
        parent_dir = sys.argv[2]
    except IndexError:
        print('Two arguments required:')
        print('  1. directory name')
        print('  2. parent directory path')
        sys.exit(1)

    # Directory path
    return os.path.join(parent_dir, directory)


def make_directories(path, folders):
    '''
    Creates the main project directory as well as default subdirectories
    '''
    dirs = [path]
    dirs.extend([os.path.join(path, f) for f in folders])
    for dp in dirs:
        os.makedirs(dp)


def make_files(path, files):
    '''
    Creates default files for the project
    '''
    files = [os.path.join(path, f) for f in files]
    for fp in files:
        open(fp, 'a').close()


def generate_venv(path):
    '''
    Create a virtual environment 'env' within the main project directory
    '''
    venv.EnvBuilder().create(os.path.join(path, 'env'))


def verify():
    '''
    Gets user input to verify the creation of the directory
    '''
    y_n = input('\nAre you sure you want to initiate project (y/n): ')
    if y_n == 'y':
        return True
    elif y_n == 'n':
        return False
    else:
        print(f'\nYou entered {y_n}.')
        print("Please enter 'y' to initiate project or 'n' to exit...")
        return verify()


def main():
    # Verify user wants to initiate project
    if verify():

        # Get project path
        path = get_path()

        # Make project directories
        make_directories(path, DEFAULT_FOLDERS)

        # Make project files
        make_files(path, DEFAULT_FILES)

        # Create virtual environment
        if CREATE_VENV:
            generate_venv(path)

        # Print a directory tree for the project
        print('\n', create_tree(Directory(path)))

    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
