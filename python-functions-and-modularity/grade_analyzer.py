#Task 1 — Process the Scores
def process_scores(students):
    result = {}
    for name,scores in students.items():
        if scores and sum(scores):
            average = round(sum(scores)/len(scores),2)
        else:
            average = 0
        result[name] = average
    return result

#Task 2 — Classify the Grades
def classify_grades(averages):
    result_with_grades = {}
    for name,average in averages.items():
        if int(average) >= 90:
            grade = "A"
        elif int(average) >= 75:
            grade = "B"
        elif int(average) >= 60:
            grade = "C"
        else:
            grade = "F"
        result_with_grades[name] = (average, grade)
    return result_with_grades

#Task 3 — Generate the Report
def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    
    total_students = len(classified)
    passed_count = 0

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        
        if status == "PASS":
            passed_count += 1

        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total_students - passed_count}")

    
students = {
    "Mithun": [85, 90, 78],
    "Vasanth": [88, 76, 92],
    "Tushar": [100, 95],
    "Rakkesh": [60,90,30]
}
averages = process_scores(students)
print(f"Average of students: {averages}")
averages_with_grades = classify_grades(averages)
print(f"Grades with averages: {averages_with_grades}")

#without passing_avg argument
generate_report(averages_with_grades)

#with passing_avg argument
generate_report(averages_with_grades,50)
