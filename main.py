import sys
import data_fmt
import common_courses

def print_invalid_command():
    print("Invalid command. Options:")
    print("common_courses <course1> <course2>:")
    print("\tInput two courses and get a chart of which third course was most")
    print("\tcommonly taken in the same semester as the two courses")


if __name__ == '__main__':
    # path to file
    filename = sys.argv[1]
    cmd = sys.argv[2]

    print("filename \t%s" % (filename))
    data_fmt.process_schedule(filename)

    if (cmd == "common_course"):
        course1 = sys.argv[3]
        course2 = sys.argv[4]
        common_courses.common_third_course(data_fmt.student_schedules,
                                           course1, course2)
    else:
        print_invalid_command()
