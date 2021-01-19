import os
import sys
from create_dir_tree import Directory, create_tree


DEFAULT_FILES = ['__init__.py', 'controllers.py', 'models.py']


def get_project_path():
    '''
    Defines the path of the main project directory based on sys.argv inputs

        sys.argv[1] =>  Name of module directory
        sys.argv[2] =>  Path of parent directory

    '''
    try:
        return sys.argv[2]
    except IndexError:
        print('Two arguments required:')
        print('  1. module name')
        print('  2. project directory path')
        sys.exit(1)


def get_module_name():
    '''
    Defines the name of the module based on sys.argv inputs

        sys.argv[1] =>  Name of module directory
        sys.argv[2] =>  Path of parent directory

    '''
    try:
        return sys.argv[1]
    except IndexError:
        print('Two arguments required:')
        print('  1. module name')
        print('  2. project directory path')
        sys.exit(1)


def make_directories(proj_path, mod_name):
    '''
    Creates module directory in app and module directory in templates
    '''
    mod_path = os.path.join(proj_path, 'app', mod_name)
    mod_template_path = os.path.join(proj_path, 'app', 'templates', mod_name)
    for dp in [mod_path, mod_template_path]:
        os.makedirs(dp)


def make_files(proj_path, mod_name, file_names):
    '''
    Creates default files for the module
    '''
    files = [os.path.join(proj_path, 'app', mod_name, f) for f in file_names]
    for fp in files:
        open(fp, 'a').close()


def verify():
    '''
    Gets user input to verify the creation of the module
    '''
    y_n = input('\nAre you sure you want to create a module (y/n): ')
    if y_n == 'y':
        return True
    elif y_n == 'n':
        return False
    else:
        print(f'\nYou entered {y_n}.')
        print("Please enter 'y' to create module or 'n' to exit...")
        return verify()


def main():
    # Verify user wants to initiate project
    if verify():
        # Get project path
        project_path = get_project_path()

        # Get module name
        module_name = get_module_name()

        # Make directories
        make_directories(project_path, module_name)

        # Make default files from DEFAULT_FILES
        make_files(project_path, module_name, DEFAULT_FILES)

        # Print a directory tree for the project
        print('\n', create_tree(Directory(project_path)))

    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
