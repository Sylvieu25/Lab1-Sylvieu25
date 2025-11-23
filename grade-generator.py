assignments = []  # store all assignments

print("=== GRADE GENERATOR CALCULATOR ===")

while True:
    #ssignment Name
    name = input("Enter Assignment Name: ").strip()

    #ategory Validation (FA/SA)
    while True:
        category = input("Enter Category (FA/SA): ").strip().upper()
        if category in ['FA', 'SA']:
            break
        print("Invalid category. Please enter FA or SA.")

    #rade Validation (0–100)
    while True:
        try:
            grade = float(input("Enter Grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric value for grade.")

    #eight Validation (positive number)
    while True:
        try:
            weight = float(input("Enter Weight (positive number): "))
            if weight > 0:
                break
            else:
                print("Weight must be positive.")
        except ValueError:
            print("Please enter a numeric value for weight.")

    #dd to assignments list
    assignments.append({
        "name": name,
        "category": category,
        "grade": grade,
        "weight": weight
    })

    #sk to add more assignments
    more = input("Add another assignment? (y/n): ").lower()
    if more == 'n':
        break

# print cleaned list
print("\nAssignments entered:")
for a in assignments:
    print(f"{a['name']} ({a['category']}): Grade={a['grade']}, Weight={a['weight']}")

# Calculate weighted grades
total_fa = 0
total_sa = 0
fa_total_weight = 0
sa_total_weight = 0

for a in assignments:
    weighted = (a['grade'] / 100) * a['weight']
    a['weighted'] = weighted  # store weighted grade for reference

    if a['category'] == 'FA':
        total_fa += weighted
        fa_total_weight += a['weight']
    else:  # SA
        total_sa += weighted
        sa_total_weight += a['weight']

# Final grade & GPA
final_grade = total_fa + total_sa
gpa = (final_grade / 100) * 5.0

#ass/Fail logic
fa_pass = total_fa >= (fa_total_weight * 0.5)
sa_pass = total_sa >= (sa_total_weight * 0.5)
status = "PASS" if fa_pass and sa_pass else "FAIL"

print("\n=== GRADE SUMMARY ===")
for a in assignments:
    print(f"{a['name']} ({a['category']}): Grade={a['grade']}, Weight={a['weight']}, Weighted={a['weighted']:.2f}")
print(f"\nTotal FA: {total_fa:.2f} / {fa_total_weight}")
print(f"Total SA: {total_sa:.2f} / {sa_total_weight}")
print(f"Final Grade: {final_grade:.2f}")
print(f"GPA: {gpa:.2f}")
print(f"Status: {status}")

import csv

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Assignment", "Category", "Grade", "Weight", "Weighted"])
    for a in assignments:
        writer.writerow([a['name'], a['category'], a['grade'], a['weight'], f"{a['weighted']:.2f}"])

