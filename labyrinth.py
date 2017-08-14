def isEmpty(s):
    if isinstance(s, str):
        return not bool(s and s.strip())
    else:
        return False


def isDistanceLower(_matrix_index, _distance):
    if isinstance(_matrix_index, str) and _matrix_index == '*':
        return False
    if isinstance(_matrix_index, int):
        return _matrix_index > _distance


def findPath(_start_index_x, _start_index_y, _distance):
    global matrix
    matrix_pointers = [(_start_index_x + 1, _start_index_y), (_start_index_x - 1, _start_index_y),
                       (_start_index_x, _start_index_y + 1), (_start_index_x, _start_index_y - 1)]

    for matrix_pointer in matrix_pointers:
        if isEmpty(matrix[matrix_pointer[0]][matrix_pointer[1]]) or isDistanceLower(
                matrix[matrix_pointer[0]][matrix_pointer[1]], _distance):
            matrix[matrix_pointer[0]][matrix_pointer[1]] = _distance
            findPath(matrix_pointer[0], matrix_pointer[1], _distance + 1)

start_index = None

with open("schema.txt", 'r') as file:
    number_of_columns = len(file.readline()) - 1
    number_of_lines = len(file.readlines()) + 1
    file.seek(0)

    matrix = [[0 for x in range(number_of_columns)] for y in range(number_of_lines)]
    line_index = 0
    for line in file.readlines():
        column_index = 0
        for column in line.rstrip('\n'):
            # set start and end as well
            if column == 'a':
                start_index = (line_index, column_index)
            elif column == 'b':
                end_index = (line_index, column_index)

            matrix[line_index][column_index] = column
            column_index += 1
        line_index += 1

findPath(start_index[0], start_index[1], 1)

with open("schema_result.txt", 'w') as file_result:
    for row in matrix:
        for column in row:
            _col = str(column)
            if len(_col) == 1:
                _col += " "
            file_result.write(_col + " ")
        file_result.write("\n")

pass
