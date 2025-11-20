#!/usr/bin/env python3
import csv

def prompt_assignment():
    name = input("Assignment Name: ").strip()
    while not name:
        print("Assignment name cannot be empty.")
        name = input("Assignment Name: ").strip()

    category = input("Category (FA for Formative, SA for Summative): ").strip().upper()
    while category not in {"FA", "SA"}:
        print("Category must be 'FA' or 'SA'.")
        category = input("Category (FA for Formative, SA for Summative): ").strip().upper()

    while True:
        grade_input = input("Grade Obtained (0-100): ").strip()
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Grade must be a number.")

    while True:
        weight_input = input("Weight (positive number, e.g., 30): ").strip()
        try:
            weight = float(weight_input)
            if weight > 0:
                break
            else:
                print("Weight must be a positive number.")
        except ValueError:
            print("Weight must be a number.")

    return {"Assignment": name, "Category": category, "Grade": grade, "Weight": weight}

def summarize(assignments):
    total_fa_weight = sum(a["Weight"] for a in assignments if a["Category"] == "FA")
    total_sa_weight = sum(a["Weight"] for a in assignments if a["Category"] == "SA")

    total_fa_score = sum((a["Grade"] / 100.0) * a["Weight"] for a in assignments if a["Category"] == "FA")
    total_sa_score = sum((a["Grade"] / 100.0) * a["Weight"] for a in assignments if a["Category"] == "SA")

    total_grade = total_fa_score + total_sa_score
    gpa = (total_grade / 100.0) * 5.0

    fa_required = 0.5 * total_fa_weight
    sa_required = 0.5 * total_sa_weight
    fa_pass = total_fa_score >= fa_required if total_fa_weight > 0 else False
    sa_pass = total_sa_score >= sa_required if total_sa_weight > 0 else False
    overall_pass = fa_pass and sa_pass

    return {
        "total_fa_weight": total_fa_weight,
        "total_sa_weight": total_sa_weight,
        "total_fa_score": total_fa_score,
        "total_sa_score": total_sa_score,
        "total_grade": total_grade,
        "gpa": gpa,
        "fa_required": fa_required,
        "sa_required": sa_required,
        "fa_pass": fa_pass,
        "sa_pass": sa_pass,
        "overall_pass": overall_pass
    }

def print_summary(assignments, summary):
    print("\n===== Grade Summary =====")
    print(f"Assignments entered: {len(assignments)}")

    print("\nFormative (FA):")
    print(f"  Total FA weight: {summary['total_fa_weight']:.2f}")
    print(f"  Total FA score:  {summary['total_fa_score']:.2f}")
    print(f"  Required to pass FA (50% of weight): {summary['fa_required']:.2f}")
    print(f"  FA status: {'PASS' if summary['fa_pass'] else 'FAIL'}")

    print("\nSummative (SA):")
    print(f"  Total SA weight: {summary['total_sa_weight']:.2f}")
    print(f"  Total SA score:  {summary['total_sa_score']:.2f}")
    print(f"  Required to pass SA (50% of weight): {summary['sa_required']:.2f}")
    print(f"  SA status: {'PASS' if summary['sa_pass'] else 'FAIL'}")

    print("\nTotals:")
    print(f"  Final grade (weighted total): {summary['total_grade']:.2f} / 100")
    print(f"  GPA (out of 5.0): {summary['gpa']:.2f}")
    print(f"\nOverall Status: {'PASS' if summary['overall_pass'] else 'FAIL'}")
    print("=========================\n")

def export_csv(assignments, filename="grades.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Assignment", "Category", "Grade", "Weight"])
        writer.writeheader()
        for a in assignments:
            writer.writerow({
                "Assignment": a["Assignment"],
                "Category": a["Category"],
                "Grade": f"{a['Grade']:.2f}",
                "Weight": f"{a['Weight']:.2f}"
            })
    print(f"Data exported to {filename}")

def main():
    print("AFRICAN LEADERSHIP UNIVERSITY")
    print("INDIVIDUAL CODING LAB")
    print("INTRODUCTION TO PYTHON PROGRAMMING AND DATABASES")
    print("BSE YEAR 1 TRIMESTER 2\n")

    assignments = []

    while True:
        assignments.append(prompt_assignment())
        current_summary = summarize(assignments)
        total_weight = current_summary["total_fa_weight"] + current_summary["total_sa_weight"]
        if total_weight > 100:
            print(f"Warning: Total combined weight is now {total_weight:.2f}, which exceeds 100.")
        add_more = input("Add another assignment? (y/n): ").strip().lower()
        while add_more not in {"y", "n"}:
            add_more = input("Please enter 'y' or 'n': ").strip().lower()
        if add_more == "n":
            break

    summary = summarize(assignments)
    print_summary(assignments, summary)
    export_csv(assignments)

if __name__ == "__main__":
    main()

