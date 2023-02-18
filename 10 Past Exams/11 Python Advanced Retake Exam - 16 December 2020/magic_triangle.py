def get_magic_triangle(number):
    triangle = [[1], [1, 1]]
    last_line_idx = 1

    while len(triangle) < number:
        next_line = triangle[last_line_idx] + [1]

        for idx in range(1, len(next_line) - 1):
            next_line[idx] = triangle[last_line_idx][idx - 1] + triangle[last_line_idx][idx]

        triangle.append(next_line)
        last_line_idx += 1

    return triangle
