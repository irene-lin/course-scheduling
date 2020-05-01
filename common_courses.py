# common_courses.py
# Irene Lin
# iwl@alumni.cmu.edu
# This file contains data processing to find which courses are taken together
# Input two courses and get a chart of which third course was most commonly
# taken in the same semester as the two courses

import data_fmt

def common_third_course(student_scheds,course1,course2):
    results = dict() # key: course, value: count
    # iterate over every student
    for s in student_scheds.values():
        # iterate over semester course sets
        for sem in s.sem_to_courses.values():
            # update results if both courses taken in the same semester
            if (course1 in sem and course2 in sem):
                for course in sem:
                    if course in results:
                        results[course] += 1
                    else:
                        results[course] = 1

    total_students = results[course1]
    results.pop(course1)
    results.pop(course2)
    # sort by value
    res_sorted = sorted(results.items(), key=lambda tup: tup[1], reverse=True)
    print("Total students: %d" % total_students)
    num = min(len(res_sorted), 10)
    print("Top %d third course choices taken with %s and %s:"
            %(num, course1, course2))
    for i in range(num):
        print("Course %s Count: %d" %(res_sorted[i][0], res_sorted[i][1]))
