import pandas

students_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [50, 60, 80]
}

student_data_frame = pandas.DataFrame(students_dict)

#using traditional method to iterate
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

###Uing the iterrows method
for (index, value) in student_data_frame.iterrows():
    if value.score == 50:
        print(value.student)