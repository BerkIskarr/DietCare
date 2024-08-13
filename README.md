# **DietCare**

This is a visual application developed using python and pythonQt5 to help users record and track their food and diet records to achieve better weight loss or fitness results.

Please read the following guide carefully to help you use DietCare.

Before starting the program please make sure you have downloaded:

For running .bat you ONLY need to have the following:
- Python: Please use version 3.6 or above, 3.11 is the recommended version.
- Download the NEWGUI.tar.gz and DietCare.bat.
- This application does not require any further modifications to the code, just run the DietCare.bat.
- Optionally you can extract the contents of NEWGUI.tar.gz and run the login_mata.exe file.

For running the .py files you also need: 
- PyQt5
- Pandas
- matplotlib
- numpy

make sure you download the sqlite3 as well from https://www.sqlite.org/

And install:
You need to clone our repository locally on your computer:
https://cseegit.essex.ac.uk/23-24-ce201-col/23-24_CE201-col_team-16

Please install the necessary python library:
- pip install PyQt5
- pip install Pandas
- pip install matplotlib
- pip install numpy


When installing using these commands, you need to make sure that your Python environment is set up correctly and that the pip tool is up to date.

After this, this program does not require any further modifications to the code, just run login_mata.py.

If you want to use a regular user account, please log in with one of following accounts:
| username | password | name |
| ------ | ------ |  ------ |
|user1 |123| Karl |
|user2|123| Kate |
|user3 | 123 | Lily |


If you want to use an administrator account, please use:
| username | password |
| ------ | ------ |
|admin |123|

If you want to use a nutrition expert account, please use:
| username | password |
| ------ | ------ |
|expert |123|



## Known issue

1. The application might take several seconds to start while using .bat/.sh, since the program needs to extract the archive before running the .exe file.
2. As of now, the application, while using .bat and .exe files, only run on windows. To use the application on unix-based systems one needs to run it through login_mata.py
