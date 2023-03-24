# Conector
<!-- Faltan badges -->
[![GitHub commits](https://badgen.net/github/commits/Veltys/conector)](https://GitHub.com/Veltys/conector/commit/)
[![GitHub latest commit](https://badgen.net/github/last-commit/Veltys/conector)](https://GitHub.com/Veltys/conector/commit/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/Veltys/conector/blob/master/LICENSE)

Python-powered system connection manager and mounts via SSH


## Description
System connection manager using Python which connects and mounts home directory through SSH


## Changelog
### To-do (*TODO*)
- [ ] PowerShell completion facilities
- [ ] Internationalization

### [3.0.1] - 2023-03-24
#### Fixed
- Some Eclipse / Pydev warnings

### [3.0.0] - 2023-03-21
#### Added
- Conversion to Python package
- Scripts to manage installation

### [2.0.0] - 2023-02-21
#### Added
- Scripts to mount and unmount home directory

#### Fixed
- Conversion to library

### [1.0.0] - 2023-01-25
#### Added
- Initial script to establish a connection


## Configuration
Before you start using the 'conector' package, you need to configure it according to your needs. The configuration settings are stored in the `conector/config.py` file. Follow these steps to set up the configuration:

1. Navigate to the 'conector' directory where you cloned the repository.

2. Copy the `config.py.template` file located in the 'conector' directory to `config.py`.

2. Open the `config.py` file using your preferred text editor.

3. In the `config.py` file, you will find a list of constants that need to be configured. Fill in the required information for each constant. For instance:

   SSH_KEY = 'path/to/your/ssh/key'
   DEFAULT_ANSIBLE_USER = 'your_ssh_user'
   INVENTORY_DIR_NAME = 'path/to/your/ansible/inventory/directory/or/file'
   VAULT_PASS_FILE = 'path/to/your/ansible/vault_pass/file'

Replace all the sample values with your specific values.

4. Save the changes to the `config.py` file and close the text editor.

Now the 'conector' package is configured and ready to use.

## Installing
To install the 'conector' package, follow these steps:

1. Make sure you have Python 3.6 or higher installed on your system. You can check your Python version by running the following command in your terminal:

   python3 --version

   If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

2. It's recommended to create a virtual environment for the installation to avoid potential conflicts with other packages. You can do this by running the following commands:

   python3 -m venv conector-env
   source conector-env/bin/activate  # On Windows, use 'conector-env\Scripts\activate'

3. Clone the 'Conector' repository from GitHub:

   git clone https://github.com/Veltys/Conector.git

4. Navigate to the cloned repository's directory:

   cd Conector

5. Install the 'conector' package using pip:

   sudo pip install .

Now the 'conector' package should be installed on your system and ready to use.

Note: To exit the virtual environment after you've finished using the 'conector' package, simply run the following command:

   deactivate


## Uninstalling
Keep in mind that the normal uninstall process will leave some residue on the system. That is why a clean uninstall script is provided.

To uninstall the 'conector' package and remove the Bash autocompletion files, follow these steps:

1. Navigate to the cloned repository's directory:

   cd Conector

2. Run the following command, this will remove the 'conector' package and the associated bash autocompletion files:

  python3 uninstall.py


## Acknowledgments, sources consulted and other credits
* To the [official Ansible documentation](https://docs.ansible.com/ansible/latest/index.html), for the more-or-less enough Python API documentation
* To the [official Python documentation](https://docs.python.org/3/), for obvious reasons
