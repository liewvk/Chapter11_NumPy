import numpy as np


print("NumPy Student Data Analyzer")
print("---------------------------")

# Columns:
# Column 0 = Score
# Column 1 = Attendance
student_data = np.array([
    [85, 92],
    [72, 80],
    [90, 95],
    [45, 60],
    [58, 75]
])

scores = student_data[:, 0]
attendance = student_data[:, 1]

average_score = np.mean(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)

pass_count = np.sum(scores >= 50)
fail_count = np.sum(scores < 50)

high_attendance = attendance >= 80
high_attendance_students = student_data[high_attendance]

minimum_score = np.min(scores)
maximum_score = np.max(scores)

normalized_scores = (scores - minimum_score) / (maximum_score - minimum_score)

print()
print("Student Data")
print("------------")
print(student_data)

print()
print("Scores:", scores)
print("Attendance:", attendance)

print()
print("Summary")
print("-------")
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Students passed: {pass_count}")
print(f"Students failed: {fail_count}")

print()
print("Students with attendance 80% or above")
print("-------------------------------------")
print(high_attendance_students)

print()
print("Normalized Scores")
print("-----------------")
print(normalized_scores)
