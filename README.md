# Artifact Extractor for Windows System (AEWS)
The AEWS is a Python program that utilizes the 'psutil' and 'pandas' libraries to gather essential information about processes, services, memory usage, disk space, and logged-in users on the system and creates a dataframe for further analysis.

## Features
The AEWS provides the following features: 
* **Process and Service Information**: Retrieve detailed information about running processes and services on the system, including process ID, name, status, and more. The data is stored in CSV files named 'processes.csv' and 'services.csv'.

* **Memory Usage**: Get an overview of memory usage statistics, including total memory, available memory, used memory, and memory usage percentages. Memory data is stored in a text file named 'sys_info.txt'.

* **Disk Space**: Obtain information about disk space usage for all mounted partitions, including total disk space, used space, free space, and utilization percentages. Disk space data is stored in a text file named 'sys_info.txt'.

* **Logged-In Users**: View data regarding users currently logged in to the system. User data is stored in a csv file named 'users.csv'.

## Installation & Usage
To use this program, you need to have Python 3.7 installed on your machine. Follow these steps to get started: 
1. Clone this repository to your local machine:

   `git clone https://github.com/MeenakshiPathiyil/Artifact-Extractor-for-Windows-System.git`

2. Navigate to the project directory:

   `cd Artifact-Extractor-for-Windows-System`

3. Install the required Python packages:

   `pip install -r requirements.txt`

4. Run the 'AEWS.py' script using the following command:

   `python3 AEWS.py`

## Data Storage
1. Process, service and user data are stored in CSV files for further analysis. You can load these CSV files into a Jupyter Notebook or any other data analysis tool to perform more in-depth investigations.
2. Memory and disk space data are stored in a text file for easy access and reference.

## Acknowledgements
* [**Pandas Library**](https://pandas.pydata.org/) - Used to create dataframes for process, service and user information and to present data in a tabular format for better readability.
* [**Psutil Library**](https://pypi.org/project/psutil/) - Used to retrieve system-related information, such as process data, memory usage, disk usage, and logged-in users.

## Contribution
Contributions to this project are welcome! If you have any suggestions, improvements or bug reports, please open an issue on the GitHub repository. 
