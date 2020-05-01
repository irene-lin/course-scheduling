# data_fmt.py
# Irene Lin
# iwl@alumni.cmu.edu
# This contains implementation of data formatting functions.
# Builds student schedule dictionary objects

# Expected array indices for the input file
STUDENT_ID = 0
COURSE = 1
GRADE = 2
SEMESTER = 3

# global for student information
student_schedules = dict()

# Base class for one student
class Student:
    def __init__(self, id):
        self.id = id
        # key: grade, value: set of semesters
        self.grade_to_sem = dict()
        # key: semester, value set of courses
        self.sem_to_courses = dict()

    def __repr__(self):
        return ("Student %s \n  grade to sem %s\n  sem_to_courses %s"
                % (self.id, self.grade_to_sem, self.sem_to_courses))

# given a path to a csv file, returns 2D array
def parseFile(infile):
    f_in = open(infile, "r")
    txt_in = f_in.read()
    f_in_arr = txt_in.split("\n")[:-1]
    f_in.close()
    res = []
    for line in f_in_arr:
        res.append(line.split(","))
    return res

def process_schedule(filename):
    data_arr = parseFile(filename)
    for row in data_arr:
        id = row[STUDENT_ID]
        course = row[COURSE]
        grade = row[GRADE]
        sem = row[SEMESTER]
        if (id not in student_schedules):
            student_schedules[id] = Student(id)
        student = student_schedules[id]
        #add sem to grade mapping
        if (grade not in student.grade_to_sem):
            student.grade_to_sem[grade] = {sem}
        else:
            student.grade_to_sem[grade].add(sem)
        # add course to semester mapping
        if (sem not in student.sem_to_courses):
            student.sem_to_courses[sem] = set()
        else:
            student.sem_to_courses[sem].add(course)
