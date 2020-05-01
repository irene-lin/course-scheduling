# Course Scheduling Data Analytics Tool
Python command line interface to analyze student course scheduling patterns.

Requires Python3

## Expected Data Format
Input file must be a .csv with four columns.
* Index 0: Unique student id
* Index 1: Course number
* Index 2: Student grade (Freshman/Sophomore/Junior/Senior/Masters)
* Index 3: Semester and year (ex: F20 for Fall 2020)

## Usage
To run the script:
```
python main.py <filename> <command> <args>
```
## Options and Arguments
### Third Course Choice
```
python main.py <filename> common_course <course1> <course2>
```
This command takes in two courses as arguments and counts which third course is usually taken in the same semester as the first two courses. Top 10 third course choices are printed as output.
