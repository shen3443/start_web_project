import os
import sys


# Folders who's contents wont be diagramed in the tree
VOID_FOLDERS = ['env', '.vscode', '__pycache__']


class Directory():
    def __init__(self, path):
        self.path = path
        self.name = path.split('\\')[-1]

        if self.name in VOID_FOLDERS:
            self.content = []
            self.files = []
            self.subdirs = []
        else:
            raw_content = os.listdir(self.path)
            self.content = self.process_content(raw_content)
            self.files = [f for f in self.content if isinstance(f, File)]
            self.subdirs = [
                d for d in self.content if isinstance(d, Directory)]

    def __repr__(self):
        return self.name

    def process_content(self, raw_content):
        content = []
        for child in raw_content:
            child_path = os.path.join(self.path, child)
            if os.path.isdir(child_path):
                content.append(Directory(child_path))
            else:
                content.append(File(child_path))
        return content

    def print_content(self):
        print('\n' + self.name)
        for x in self.content:
            if isinstance(x, File):
                print(x)
            elif isinstance(x, Directory):
                x.print_content()


class File():
    def __init__(self, path):
        self.path = path
        self.name = path.split('\\')[-1]

    def __repr__(self):
        return self.name


def get_dir_path():
    '''
    Returns the path of the directory to make a directory tree for, entered
    as sys.argv[1]
    '''
    try:
        path = sys.argv[1]
        return path
    except IndexError:
        print('directory path argument required')
        sys.exit(1)


def get_tree_path():
    '''
    Returns the path to which the directory tree should be saved, entered as
    sys.argv[2]
    '''
    try:
        path = sys.argv[2]
    except IndexError:
        path = 'dir_tree.txt'

    if path != 'print':
        path = os.path.join(get_dir_path(), path)

    return path


def create_tree(directory, depth=0):
    '''
    Creates directory tree with string manipulation and recursive calls for
    sub directories
    '''
    if depth:
        tree = '    ' * depth
        tree += f'|__ \\{directory}\n'
    else:
        tree = f'~\\{directory}\n'
    for f in directory.files:
        tree += add_file_line(f, depth=(depth + 1))
    for d in directory.subdirs:
        tree += create_tree(d, depth=(depth + 1))
    return tree


def add_file_line(f_name, depth=1):
    '''
    Adds a line to the directory tree to represent a file
    '''
    line = '    ' * depth
    line += f'|-- {f_name}\n'
    return line


def save_tree(tree, file_path):
    '''
    Saves the directory tree to a file
    '''
    with open(file_path, 'w') as fp:
        fp.write(tree)


def main():
    print('\nCreating Directory Tree...')
    d = Directory(get_dir_path())
    tree = create_tree(d)
    print('\nDone.')
    tree_path = get_tree_path()
    if tree_path == 'print':
        print(tree)
    else:
        print(f'\nSaving Tree to {tree_path}')
        save_tree(tree, tree_path)
        print('\nDone.')


if __name__ == "__main__":
    main()
