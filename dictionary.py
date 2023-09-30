print('Enter student,s details')
student_details={}
size=int(input('enter the size of the dictionary:'))
for i in range(size):
  name=str(input('enter the student name:'))
  registration_number=str(input('enter the student registration number:'))
  age=int(input('enter the student age:'))
  program=str(input('enter the student program admitted in:'))
  year_of_study=int(input('enter the year of study:'))
  subjects={}
  for i in range(1):
      subject1=str(input('enter the first subject:'))
      subject2=str(input('enter the second subject:'))
      subject3=str(input('enter the third subject:'))
      subjects[subject1]=subject1
      subjects[subject2]=subject2
      subjects[subject3]=subject3
  scores={}
  for i in range(1):
      marks1=int(input('enter the marks for subject1:'))
      marks2=int(input('enter the marks for subject2:'))
      marks3=int(input('enter the marks for subject3:'))
      scores[marks1]=marks1
      scores[marks2]=marks2
      scores[marks3]=marks3
  grades={}
  for i in range(1):
      grade1=str(input('enter the grade for subject1:'))
      grade2=str(input('enter the grade for subject2:'))
      grade3=str(input('enter the grade for subject3:'))
      grades[grade1]=grade1
      grades[grade2]=grade2
      grades[grade3]=grade3
      student_details[registration_number]={
        'Name':name,
        'Age':age, 
        'Program':program,
        'Year of study':year_of_study,
        'subjects':subjects,
        'scores':scores,
        'Grade':grades
        } 
def find_max_min_marks(values):
   max_mark =max(values)
   min_mark =min(values)
   return max_mark,min_mark

for regNo, student in student_details.items():
   max_marks,min_marks = find_max_min_marks(student['scores'].values())
print(f"Student:{student['Name']},Max Marks:{max_marks},Min Marks:{min_marks}")
print(student_details)







