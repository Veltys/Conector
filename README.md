# Conector
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/21bad70cf92a45648d2f40bf5a9f5964)](https://app.codacy.com/gh/Veltys/Conector/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
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
- [ ] Full commands translation

### [3.5.3] - 2023-12-14
#### Fixed
- Maybe is good idea to put 'ansible' package in the requirements... Since it is a really required requirement...

### [3.5.2] - 2023-12-14
#### Fixed
- Windows installation process

### [3.5.1] - 2023-12-14
#### Added
- Bastion host indication in "Connecting to..." message

#### Fixed
- English texts

### [3.5.0] - 2023-12-14
#### Added
- *break-system-packages* parameter detection

#### Fixed
- Wrong bastion port

### [3.4.0] - 2023-12-14
#### Added
- Default Ansible port support

#### Fixed
- Wrong varaible name in **config.py.template**

### [3.3.0] - 2023-12-13
#### Added
- SSH bastion hosts support

#### Fixed
- Better **README.md** format
- Internal *--break-system-packages* parameter in **uninstall.py**

### [3.2.4] - 2023-11-21
#### Fixed
- Code quality

### [3.2.3] - 2023-11-04
#### Added
- Codacy badge

#### Fixed
- Code quality

### [3.2.2] - 2023-07-20
#### Added
- *-v* parameter to show version number

### [3.2.1] - 2023-07-20
#### Deleted
- *host_id* variable as it is redundant

### [3.2.0] - 2023-04-20
#### Added
- Posibility to load multiple inventories

### [3.1.1] - 2023-04-20
#### Fixed
- Wrong class variable name

### [3.1.0] - 2023-03-24
#### Added
- *-L* parameter to stablish a local SSH tunnel bind

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

  ```bash
  python3 --version
  ```

   If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

2. It's recommended to create a virtual environment for the installation to avoid potential conflicts with other packages. You can do this by running the following commands:

  ```bash
  python3 -m venv conector-env
  source conector-env/bin/activate  # On Windows, use 'conector-env\Scripts\activate'
  ```

3. Clone the 'Conector' repository from GitHub:

  ```bash
  git clone https://github.com/Veltys/Conector.git
  ```

4. Navigate to the cloned repository's directory:

  ```bash
  cd Conector
  ```

5. Install the 'conector' package using pip:

  ```bash
   sudo pip install [ --break-system-packages ] .
  ```

  Note: Do not forget the final dot.

Now the 'conector' package should be installed on your system and ready to use.

Note: To exit the virtual environment after you've finished using the 'conector' package, simply run the following command:

  ```bash
  deactivate
  ```

## Uninstalling
Keep in mind that the normal uninstall process will leave some residue on the system. That is why a clean uninstall script is provided.

To uninstall the 'conector' package and remove the Bash autocompletion files, follow these steps:

1. Navigate to the cloned repository's directory:

  ```bash
  cd Conector
  ```

2. Run the following command, this will remove the 'conector' package and the associated bash autocompletion files:

  ```bash
  python3 uninstall.py [ --break-system-packages ]
  ```


## Acknowledgments, sources consulted and other credits
* To the [official Ansible documentation](https://docs.ansible.com/ansible/latest/index.html), for the more-or-less enough Python API documentation
* To the [official Python documentation](https://docs.python.org/3/), for obvious reasons
