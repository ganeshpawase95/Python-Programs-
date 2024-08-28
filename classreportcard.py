# PROG 6: School Report
def get_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'
    


def publish_result(student_name, physics_marks, chemistry_marks, maths_marks, max_marks=100, computation_type='p'):
    # Calculate grades
    physics_grade = get_grade(physics_marks)
    chemistry_grade = get_grade(chemistry_marks)
    maths_grade = get_grade(maths_marks)

    total_marks = physics_marks + chemistry_marks + maths_marks
    total_percentage = (total_marks / (3 * max_marks)) * 100
    total_grade = get_grade(total_percentage)

    if computation_type == 'g':
        # Print the report card with grades
        print(f"\nNew School Of Learning - Class XI - {student_name}")
        print("--------------------------------")
        print("|     Subject     |   Grade    |")
        print("--------------------------------")
        print(f"|     Physics     |     {physics_grade}      |")
        print(f"|    Chemistry    |     {chemistry_grade}      |")
        print(f"|   Mathematics   |     {maths_grade}      |")
        print("--------------------------------")
        print(f"|      Total      |     {total_grade}      |")
        print("--------------------------------")
    elif computation_type == 'p':
       print(f"\n{SCHOOL_NAME} - {student_name}")
       print(f"{'-' * 72}")
       print(f"| {'Subject':^15} | {'Total Marks':^15} | {'Marks Obtained':^15} | {'Percentage':^15} |")
       print(f"{'-' * 72}")
       print(f"| {'Physics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_phys_marks:^15}",
              f"| {student_phys_perc:^15} |")
       print(f"| {'Chemistry':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_chem_marks:^15}",
              f"| {student_chem_perc:^15} |")
       print(f"| {'Mathematics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_math_marks:^15}",
              f"| {student_math_perc:^15} |")
       print(f"{'-' * 72}")
       print(f"| {'Total':^15} | {TOTAL_MARKS:^15} | {total_student_marks:^15}",
              f"| {round((total_student_marks / TOTAL_MARKS) * 100, 2):^15} |")
       print(f"{'-' * 72}\n")

SCHOOL_NAME = "New School Of Learning"
TOTAL_SUBJECT_MARKS = 100
TOTAL_MARKS = TOTAL_SUBJECT_MARKS*3
NUMBER_STUDENTS = 1 

# Step 2: Defining Global Variables for subject-wise total marks along with
# class average and percentage and initializing the same to 0
total_phys_marks = total_chem_marks = total_math_marks = 0
class_phys_avg = class_chem_avg = class_math_avg = 0.0
class_phys_perc = class_chem_perc = class_math_perc = 0.0
overall_total_student_marks = overall_perc = 0

# Step 3: Loop through each student to get input and calculate total marks
for i in range(NUMBER_STUDENTS):

  # Step 4: Get student name, if Not valid then breaking the loop
  student_name = input(f"Enter name of student : ")
  max_marks = input("Enter max marks per subject (default is 100): ")
  if max_marks:
    max_marks = int(max_marks)
  else:
    max_marks = 100
  if len(student_name) == 0 or student_name.isalpha() == False :
    print(f"Invalid Input: Student Name {student_name}")
    overall_total_student_marks = None
    break;

  # Step 5: Get student name , physics, chemistry and maths marks for Student.
  # Validate the input and Calculate total marks for student
  phys_marks_entered = input(f"Enter Physics marks out of 100 for student : ")
  chem_marks_entered = input(f"Enter Chemistry marks out of 100 for student : ")
  math_marks_entered = input(f"Enter Mathematics marks out of 100 for student : ")
  computation_type = input(f"Enter computation type (g for grades, p for percentage): ")

  student_phys_marks = (phys_marks_entered.isdigit() and
                        int(phys_marks_entered) or None)
  student_chem_marks = (chem_marks_entered.isdigit() and
                        int(chem_marks_entered) or None)
  student_math_marks = (math_marks_entered.isdigit() and
                        int(math_marks_entered) or None)

  if (student_phys_marks is None or 0 < student_phys_marks > 100 or
      student_chem_marks is None or 0 < student_chem_marks > 100 or
      student_math_marks is None or 0 < student_math_marks > 100) :
      overall_total_student_marks = None
      print(f"Invalid Input: Physics Mark: {phys_marks_entered}, Chemistry",
            f"Marks: {chem_marks_entered} or Maths Marks: {math_marks_entered}")
      break;

  total_student_marks = student_phys_marks + student_chem_marks + student_math_marks

  # Step 6: Calculating physics, chemistry and maths percentage for student
  student_phys_perc = round((student_phys_marks / TOTAL_SUBJECT_MARKS) * 100, 2)
  student_chem_perc = round((student_chem_marks / TOTAL_SUBJECT_MARKS) * 100, 2)
  student_math_perc = round((student_math_marks / TOTAL_SUBJECT_MARKS) * 100, 2)

  # Step 7: Calculate total marks and overall marks obtained by all
  # students in each subject
  total_phys_marks += student_phys_marks
  total_chem_marks += student_chem_marks
  total_math_marks += student_math_marks
  overall_total_student_marks += total_student_marks

  # Step 8: Print results for student
  """print(f"\n{SCHOOL_NAME} - {student_name}")
  print(f"{'-' * 72}")
  print(f"| {'Subject':^15} | {'Grade':^15} |")
  print(f"{'-' * 72}")
  print(f"| {'Physics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_phys_marks:^15}",
        f"| {student_phys_perc:^15} |")
  print(f"| {'Chemistry':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_chem_marks:^15}",
        f"| {student_chem_perc:^15} |")
  print(f"| {'Mathematics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {student_math_marks:^15}",
        f"| {student_math_perc:^15} |")
  print(f"{'-' * 72}")
  print(f"| {'Total':^15} | {TOTAL_MARKS:^15} | {total_student_marks:^15}",
        f"| {round((total_student_marks / TOTAL_MARKS) * 100, 2):^15} |")
  print(f"{'-' * 72}\n")"""

if overall_total_student_marks is not None :
  # Step 9: Calculate class averages for each subject if overall student
  # marks is not None
  class_phys_avg = total_phys_marks / NUMBER_STUDENTS
  class_chem_avg = total_chem_marks / NUMBER_STUDENTS
  class_math_avg = total_math_marks / NUMBER_STUDENTS

  # Step 10: Calculate the class average percentage for each subject
  class_phys_perc = (class_phys_avg / TOTAL_SUBJECT_MARKS) * 100
  class_chem_perc = (class_chem_avg / TOTAL_SUBJECT_MARKS) * 100
  class_math_perc = (class_math_avg / TOTAL_SUBJECT_MARKS) * 100

  # Step 11: Calculate overall percentage
  overall_perc = (overall_total_student_marks / (NUMBER_STUDENTS * TOTAL_MARKS)) * 100

  # Step 12: Print the class average percentage for each subject
  