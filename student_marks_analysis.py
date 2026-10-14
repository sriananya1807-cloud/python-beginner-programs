marks = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks)

print("List:", marks)
print("List data type:", type(marks))

print("Tuple:", marks_tuple)
print("Tuple data type:", type(marks_tuple))

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

print("Students scoring at least 40:", 
      (marks[0] >= 40) + (marks[1] >= 40) +
      (marks[2] >= 40) + (marks[3] >= 40) +
      (marks[4] >= 40))

valid = (0 <= marks[0] <= 100 and
         0 <= marks[1] <= 100 and
         0 <= marks[2] <= 100 and
         0 <= marks[3] <= 100 and
         0 <= marks[4] <= 100)
print("All marks are valid:", valid)

marks[0] = 85
print("Modified list:", marks)

print("Original tuple:", marks_tuple)