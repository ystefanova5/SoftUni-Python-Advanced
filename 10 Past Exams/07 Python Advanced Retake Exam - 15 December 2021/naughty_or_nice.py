def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_or_naughty = {"Nice": [], "Naughty": []}

    for data in args:
        counting_numbers = [item[0] for item in santa_list]
        number, status = data.split("-")
        number = int(number)
        if counting_numbers.count(number) == 1:
            for kid_number, kid_name in santa_list:
                if kid_number == number:
                    nice_or_naughty[status].append(kid_name)
                    santa_list.remove((kid_number, kid_name))
                    break

    for name, stat in kwargs.items():
        counting_names = [item[1] for item in santa_list]
        if counting_names.count(name) == 1:
            for kid_number, kid_name in santa_list:
                if name == kid_name:
                    nice_or_naughty[stat].append(name)
                    santa_list.remove((kid_number, kid_name))
                    break

    nice_or_naughty["Not found"] = [x[1] for x in santa_list]

    result = ""

    for status, kids in nice_or_naughty.items():
        if kids:
            result += f"{status}: {', '.join(kids)}\n"

    return result.strip()
