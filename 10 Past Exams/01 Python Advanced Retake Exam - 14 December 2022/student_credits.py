def students_credits(*args):
    result = ""
    grades = {}
    total_credits = 0

    for course_info in args:
        course, credits, max_test_points, diyan_points = [int(x) if x.isdigit() else x for x in course_info.split("-")]
        diyan_credits = (diyan_points / max_test_points) * credits
        grades[course] = diyan_credits
        total_credits += diyan_credits

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        credits_needed = 240 - total_credits
        result += f"Diyan needs {credits_needed:.1f} credits more for a diploma.\n"

    sorted_grades = sorted(grades.items(), key=lambda x: -x[1])

    for course_name, credit in sorted_grades:
        result += f"{course_name} - {credit:.1f}\n"

    return result

