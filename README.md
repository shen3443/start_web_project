# start_web_project
Automates tasks to help kick off a modular web app project with an organized file structure


## initiate_project.py
Creates a directory, fills it with default files and subdirectories, and generates a new virtual environment. The default structure looks like:

```
~\[project_name]
  |-- config.py
  |-- run.py
  |__ \app
      |-- __init__.py
      |__ \templates
      |__ \static
  |__ \env
```
The default structure can be edited by changing the global variables `DEFAULT_FOLDERS`, `DEFAULT_FILES`, and the default creation of a virtual environment can be turned off by setting `CREATE_VENV = False`

Takes two system arguments, the name of the project and the path of the parent directory to create the project directory in

ex: `~\start_web_project> py initiate_project.py MyApp C:\Users\chris`

## add_module.py
Creates sub directorys and default files in an existing project folder for a new module. For example running `add_module.py` to add a module `auth` to a project with the file structure above (created by `initiate_project.py`) would result in a structure like:

```
~\[project_name]
  |-- config.py
  |-- run.py
  |__ \app
      |-- __init__.py
      |__ \auth
          |-- __init__.py
          |-- controllers.py
          |-- models.py
      |__ \templates
          |-- \auth
      |__ \static
  |__ \env
```
The default files to be created can be edited by changing the global variable `DEFAULT_FILES`

Takes two system arguments, the name of the module and the path of the project directory
ex: `~\start_web_project> py add_module.py auth C:\Users\chris\MyApp`

## create_dir_tree.py
Automatically generates a directory tree for a given directory to help keep track of the organizational structure of a project. This tree can either be printed to the consol or saved to a .txt file

Takes two system arguments, the name of the directory and either the file path for the .txt file to save the tree or the keyword `print`

ex: `~\start_web_project> py create_dir_tree.py C:\Users\chris\MyApp\dir_tree.txt` would save a directory tree to dir_tree.txt
or: `~\start_web_project> py create_dir_tree.py print` would print a directory tree to the consol
