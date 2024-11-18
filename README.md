# Bank accounts - part 1 (959)
For raw project instructions see: http://syllabus.africacode.net/projects/oop/bank-accounts/part-1/

## Project Setup

### 1. Environment Setup:
In the instructions below, information is provided to install the necessary tools needed to run the project and its dependencies on any capable machine:
- Set up Python on your computer. Refer to: [GETTING SET UP TO WRITE PYTHON ON YOUR COMPUTER](http://syllabus.africacode.net/environment-setup/python-on-computer/index.html).
- Configure Git on your system. Follow the instructions in: [GETTING GIT SET UP](http://syllabus.africacode.net/environment-setup/git/).
- Additional resources: [MORE ABOUT GIT](https://docs.github.com/en/get-started/using-git/about-git).
- To avoid reading and following the above-mentioned instructions on setting up an environment for the project, command prompts can be used in Windows Terminal or Command Prompt as follows:
  1. Create a new virtual environment to run the tests in by using the following command in the terminal window: 
  ~~~
  python -m venv <virtual_environment_name>
  ~~~
  2. Activate the new virtual environment that you just created using the following command:
  ~~~
  <virtual_environment_name>\Scripts\activate
  ~~~
  
### 2. Cloning the Repository:
In the instructions below, information is provided to clone the repository of the project. Cloning the repository pulls down a full copy of all the repository data associated with the GitHub.com uploads:
- Use the following command in Windows Terminal or Command Prompt as follows to clone the repository to your machine: 
~~~
git clone https://github.com/Umuzi-org/Oageng-Moche-959-contentitem-python.git
~~~
  
### 3. Installing the Required Python Packages:
Once the repository has been cloned and the virtual environment has been set up:
1. Navigate to the project directory by using the following command in the virtual environment Command Terminal or Windows Terminal:
~~~
cd Oageng-Moche-959-contentitem-python
~~~

- Once the virtual environment has been set up and activated, you will need to install all the relevant packages for the project in development mode
- The packages will need to be installed in the newly activated virtual environment by running the following command in the Windows Terminal or Command Prompt:
1. In the Windows Terminal or Command Prompt of the virtual environment, type in the following command to install the modules required to run the files for the project:
~~~
pip install -r requirements.txt
~~~
2. Ensure that Setuptools is installed on your machine. If you are unsure that Setuptools is installed on your machine, use the following command in the virtual environment Command Terminal or Windows Terminal to install it:
~~~
pip install setuptools
~~~
3. Once Setuptools has been installed on your machine, the packages will need to be installed in the newly activated virtual environment by running the following command in the Windows Terminal or Command Prompt:
~~~
python setup.py develop
~~~

### 4. Running the Bank Accounts Part 1 project and its test cases:
- After installing the required packages, make sure you are in the project directory
- To run the tests/test cases of the project, ensure that pytest is installed on your machine. If you are unsure that pytest is installed on your machine, use the following command in the virtual environment Command Terminal or Windows Terminal to install pytest:
~~~
pip install pytest
~~~
- Once pytest has been installed on your machine, to run the tests/test cases of the project, use the following command in the virtual environment Command Terminal or Windows Terminal:
~~~
python -m pytest
~~~

### 5. Deactivating environment setup:
Once the necessary tasks have been completed, deactivate the virtual environment that was set up to run the tasks by typing the following command in the Windows Terminal or Command Prompt:
~~~
deactivate
~~~
