# codingTasks
Cybersecurity Bootcamp tasks are mini projects that have helped me to get an undertanding of python. Each task below is a part of my learning and journey into python coding. 

# Award.py 
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
Once the program is running you will bew promted to privide inputs in the form of minutes taken to complete each event. 

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

























