# codingTasks
Cybersecurity Bootcamp tasks are mini projects that have helped me to get an undertanding of Python. Each task below is a part of my learning and journey into python coding. 

# Table of contents 

| Project | Description |
| --- | ------ |
| [Award.py](#p1) | Calculates awards in triathalon |
| [Email.py](#p2) | Email management system |
| [Password_hasher.py](#p3) | Hashes passwords | 

# Project 1 - Award.py  <a name="p1"></a>
Award.py calculates if a participant is to be given an award for completing a triathlon.

The program takes the total amount of time taken for a contestant to complete each event of cycling, running and swimming and adds them together. 

If the total time is within pre-defined ranges it will tell the user or contest if they have been awarded. 


## Installation 
You can clone the project directly from this repo to your local system.

### 1. Git clone 

```bash
git clone https://github.com/xxxxxxxxxxxxxxx.
```

The `.` will clone it to the current directory so make sure you are inside your project folder.

### 2. Python 
You will need Python to run the program. Download the latest version of Python here:

#### For Mac OS  
```
https://www.python.org/downloads/macos/
```

#### For Windows: 
```
https://www.python.org/downloads/windows
```

#### For Lunix:
```
https://www.python.org/downloads/source/
```

## Running Award.py

Open you terminal and go to the file where the award.py code has been saved. 

To run award.py enter the following: 

#### For Mac OS  
```
python3 award.py
```

#### For Windows: 
```
python award.py 
```

## Operating Award.py
Once the program is running you will be promted to privide inputs in the form of minutes taken to complete each event. 

### Example of inputs 

<img width="940" alt="Screenshot 2025-01-19 at 18 46 53" src="https://github.com/user-attachments/assets/7ec86afb-6185-46b8-900b-d2b2328008e8" />

### Criteria 

The program will then add the minutes together and compare the total to the pre-defined criteria below: 

<!-- prettier-ignore -->
| Total Score | Award |
| --- | ------ | 
| <= 100 | Honorary Colours| 
| 101 <= total <= 105 | Honorary Half Colours |
| 106 <= total <= 110   | Honorary Scroll |
| >110 | No award |

### Example of output 

<img width="949" alt="Screenshot 2025-01-19 at 19 05 52" src="https://github.com/user-attachments/assets/419ba347-498a-438d-8494-7b9db5cff231" />

## Future enhancements to Award.py

<!-- prettier-ignore -->
| Feature | Benefit | Priority|
| --- | ------ | --- |
| Multiple attempts and Average Calcualtion| Allow users to enter times for multiple attempts and calculate the average time to determine the award. | ✅ |
| Leaderboard or Ranking system | Allow users to enter their names and store their total times. Display a leaderboard showing the top performers.  | ✅ |
| Detailed Feedback   | Provide feedback on how close the user was to achieving the next award tier. | ✅ |
| Custom Award Criteria | Allow users to customize the award criteria for different types of events or levels of difficulty.  | ✅ |
| Time Conversion | Offer an option to input times in hours and minutes, converting them to total minutes automatically. | ❌ |
| Graphical User Interface | Develop a simple GUI using libraries like Tkinter to make the program more interactive and visually appealing.  | ❌ |





# Project 2 - Email.py  <a name="p2"></a>
Email management service that alllows users to view and marks emails as read. 

The program poppulates an inbox with emails and lists emails with thier subject, read emails by selecting from an index and identify unread emails. 

The main purpose of this task was to learn how to use objects orientated programming concepts. 


## Installation 
You can clone the project directly from this repo to your local system.

### 1. Git clone 

```bash
git clone https://github.com/xxxxxxxxxxxxxxx.
```

The `.` will clone it to the current directory so make sure you are inside your project folder.

### 2. Python 
You will need Python to run the program. Download the latest version of Python here:

#### For Mac OS  
```
https://www.python.org/downloads/macos/
```

#### For Windows: 
```
https://www.python.org/downloads/windows
```

#### For Lunix:
```
https://www.python.org/downloads/source/
```

## Running email.py

Open you terminal and go to the file where the award.py code has been saved. 

To run email.py enter the following: 

#### For Mac OS  and Lunix
```
python3 email.py
```

#### For Windows: 
```
python email.py 
```

## Operating email.py
Once the program is running you will be promted to select an action from a menu. 

1. Read email
2. View unread emails
3. Quit application

Make a selection...

### Example of menu  

<img width="253" alt="Screenshot 2025-01-20 at 14 37 42" src="https://github.com/user-attachments/assets/33d82be7-e519-4ee7-acbf-8a949a1a461d" />

### 1. Read email
Select a email to read. 

<img width="287" alt="Screenshot 2025-01-20 at 14 38 53" src="https://github.com/user-attachments/assets/392de172-b9d6-49f4-a209-eb42b157a557" />

In this example we have chosen the first email to read. By clicking number 1 the program displays the email content. 

<img width="299" alt="Screenshot 2025-01-20 at 14 39 39" src="https://github.com/user-attachments/assets/c98fd9dd-507e-4b63-9df0-d958e111fa16" />

### 2. View unread emails
To view the emails that have not yet been read selct number 2. In the exaple above we have already viewed email number one, therefore the program only shows emails 2 and 3 that are unread. 


<img width="243" alt="Screenshot 2025-01-20 at 14 40 31" src="https://github.com/user-attachments/assets/88546ca8-b4cf-4d3a-9650-0be4cf26fe36" />

### 3. Quit application 
Selecting the number 3 from the menu will exit the application. 

<img width="253" alt="Screenshot 2025-01-20 at 14 41 24" src="https://github.com/user-attachments/assets/e4b8b252-ebe9-4a16-bff7-86ef008ca9a6" />


## Future enhancements to email.py

<!-- prettier-ignore -->
| Feature | Benefit | Priority|
| --- | ------ | --- |
| Enhanced User Interface| Using a library like curses for a more interactive terminal interface. | ❌  |
| Email Sorting | Allow sorting of emails by different criteria such as date, sender, or subject.  | ✅ |
| Email Deletion   | Implement a search feature to find emails by subject line or sender. | ✅ |
| Peristence | Save emails to a file or database so that they persist between program runs. | ✅ |
| Multiple inboxes | Support multiple inboxes for different email addresses.| ❌ |
|Search Function| Implement a search featu | ❌ |



# Project 3 - Password_hasher.py <a name="p3"></a>
Hash passwords inputted by the user. 


The program prompts the user to enter a password or word they want to hash. With the use of bcrypt library the pregram also adds a salt to make the password more secure. 

The main purpose of this task was to learn about setting up virtual enviroments in Python and hashing.  


## Installation 
You can clone the project directly from this repo to your local system.

### 1. Git clone 

```bash
git clone https://github.com/xxxxxxxxxxxxxxx.
```

The `.` will clone it to the current directory so make sure you are inside your project folder.

### 2. Python 
You will need Python to run the program. Download the latest version of Python here:

#### For Mac OS  
```
https://www.python.org/downloads/macos/
```

#### For Windows: 
```
https://www.python.org/downloads/windows
```

#### For Lunix:
```
https://www.python.org/downloads/source/
```

## Dependencies - Bcrypt 
bcrypt is a type of cryptographic algorithm used to securely store passwords. It scrambles a user's password into a unique code. 

The program uses the bcrypt library to function with Python. 

To downwload bcrypt from the home page: 
```
https://pypi.org/project/bcrypt/
```

## Virtual environment (Optional Step)

As bcrypt is not a standard library in Python, it is advisable to use a virtual enviroment in Python and download the code there. A virtual environment as a container where you can install and test different libraries without having to worry about anything affecting your global workspace (just like a sandbox). Once you’re done using it, you can simply remove the virtual environment (don’t worry, you can always create a new one if you need it). 

### 1. Create a Python virtual environment

Create a file in your computer locally where you wanto to run the program. Then create a virtual environment by typing the command below in the shell:

```
python3 -m venv venv 
```


### 2. Activate the virtual environment

Once the environment has been created navigate the venv file and activate it by: 

```
source venv/bin/activate
```
The virtual environemnt should start to run and the (venv) should be shown in the terminal like below:

<img width="286" alt="Screenshot 2025-01-20 at 16 18 28" src="https://github.com/user-attachments/assets/fcccccf3-b6b9-4601-90c0-1871ba515571" />


### 3. Make sure you have Pip installed 

Pip is a python package manager that allows you to download libraries that are not on the standard Python download.

Full guide on downloading pip visit:

```
https://packaging.python.org/en/latest/tutorials/installing-packages/
```


### 4. Download bcrypt 

Bcrypt can now be downloaded in the virtual environment if you are on Mac OS use the command: 

```
pip install bcrypt
```

On Lunix and windows...
```
https://pypi.org/project/bcrypt/
```

### 5. Create a requirements/dependencies text file (optional)

As you are working in a virtual environment created specifically for this project, it will be useful to create a text file that lists all the dependencies for the project - such as bcrypt. This is useful because it will help you track which libraries you need in this environment at a later date. Or if you want to migrate the project to another environment later you will have a list of dependencies that you can re-download and get the program running quicker. 

## Run password_hasher.py: 

### For Mac OS and Lunix
```
python3 password_hasher.py
```

### For Windows: 
```
python password_hasher.py 
```

## Operating password_hasher.py
Once the program is running you will be promted to type in a password. 

<img width="471" alt="Screenshot 2025-01-20 at 16 48 26" src="https://github.com/user-attachments/assets/d1cd48f9-65d3-4eb6-9f7f-a6f7270d6e65" />

### Example of output 
The program will then hash and salt the password and return the newly created hashed password. 

<img width="589" alt="Screenshot 2025-01-20 at 16 49 48" src="https://github.com/user-attachments/assets/0ccf3b7b-18fa-45de-8ebc-4513132ffbee" />

## Close the virtual enviroment 
Once you have finished using the program please close the virtual environment by typing in...
```
deactivate 
```

## Future enhancements to email.py

<!-- prettier-ignore -->
| Feature | Benefit | Priority|
| --- | ------ | --- |
| Password Verification| Add the ability to verify if a given password matches a previously stored hashed password. | ❌  |
| Multiple Hashing Algorithms | Allow users to choose between different hashing algorithms or parameters  | ✅ |
| Command Line Arguments  | Enable the program to accept command line arguments for automation or scripting purposes. | ✅ |
| Interactive Menu | Implement a simple menu to allow users to choose between hashing a new password or verifying an existing one | ✅ |
| File I/O | Save hashed passwords to a file and allow the program to read and verify passwords from the file.| ❌ |

















