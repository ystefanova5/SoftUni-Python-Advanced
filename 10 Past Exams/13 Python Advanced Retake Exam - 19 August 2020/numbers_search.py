def numbers_searching(*args):
    missing_number = 0
    passed_nums = []
    repetitions = []
    first_num = True
    previous_num = 0

    for num in sorted(args):
        if first_num:
            previous_num = num
            first_num = False
            passed_nums.append(num)
            continue

        if num in passed_nums and num not in repetitions:
            repetitions.append(num)
            continue

        expected_num = previous_num + 1
        if expected_num < num:
            missing_number = expected_num

        passed_nums.append(num)
        previous_num = num

    return [missing_number, repetitions]
