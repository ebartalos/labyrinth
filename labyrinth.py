import copy


def isEmpty(s):
    """
    Finds out if the point is empty.
    :param s: string.
    :return: bool.
    """
    if isinstance(s, str):
        return not bool(s and s.strip())
    else:
        return False


def isDistanceLower(_matrix_index, _distance):
    """
    Compare distance in the current flooding iteration and in the matrix map.
    :param _matrix_index: matrix map distance. Constant.
    :param _distance: current flooding iteration. Constant.
    :return: true if the distance is lower in current flooding iteration.
    """
    if isinstance(_matrix_index, str) and _matrix_index == '*':
        return False
    if isinstance(_matrix_index, int):
        return _matrix_index > _distance


def flood(_start_index_x, _start_index_y, _distance):
    """
    Flooding algorithm to fill every gap in the labyring with the distance.
    :param _start_index_x: X index of matrix. Variable.
    :param _start_index_y: Y index of matrix. Variable.
    :param _distance: Distance from the beginning. Variable.
    :return: Nothing.
    """
    global matrix
    matrix_pointers = [(_start_index_x + 1, _start_index_y), (_start_index_x - 1, _start_index_y),
                       (_start_index_x, _start_index_y + 1), (_start_index_x, _start_index_y - 1)]

    for matrix_pointer in matrix_pointers:
        if isEmpty(matrix[matrix_pointer[0]][matrix_pointer[1]]) or isDistanceLower(
                matrix[matrix_pointer[0]][matrix_pointer[1]], _distance):
            matrix[matrix_pointer[0]][matrix_pointer[1]] = _distance
            flood(matrix_pointer[0], matrix_pointer[1], _distance + 1)


def find_all_ways(matrix, _start_index_x, _start_index_y, _distance, _way_previous):
    """
    Finds all ways from the A to the B point.
    :param matrix: resolved matrix. Constant.
    :param _start_index_x: X index of matrix. Variable.
    :param _start_index_y: Y index of matrix. Variable.
    :param _distance: Distance from the beginning. Variable.
    :param _way_previous: Previous path to actual point. Variable.
    :return: Just to break when the final path is found.
    """
    global all_ways

    matrix_pointers = [(_start_index_x + 1, _start_index_y), (_start_index_x - 1, _start_index_y),
                       (_start_index_x, _start_index_y + 1), (_start_index_x, _start_index_y - 1)]

    for matrix_pointer in matrix_pointers:
        if matrix[matrix_pointer[0]][matrix_pointer[1]] == "b":
            _way_previous.append(matrix_pointer)
            all_ways.append(_way_previous)
            return
        if matrix[matrix_pointer[0]][matrix_pointer[1]] == _distance + 1:
            _way = copy.copy(_way_previous)
            _way.append(matrix_pointer)
            find_all_ways(matrix, matrix_pointer[0], matrix_pointer[1], _distance + 1, _way)


def find_fastest_way(_all_ways):
    """
    Finds the fastest way in the arrays of ways.
    :param _all_ways: Array of arrays with different paths.
    :return: arrays with the fewest elements - the fastest way.
    """
    return min(_all_ways)

# Initialize arrays with the labyrinth
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

# Flood and save results
flood(start_index[0], start_index[1], 1)

with open("schema_result.txt", 'w') as file_result:
    for row in matrix:
        for column in row:
            _col = str(column)
            if len(_col) == 1:
                _col += " "
            file_result.write(_col + " ")
        file_result.write("\n")

# Find all paths and choose the fastest one
all_ways = []

find_all_ways(matrix, start_index[0], start_index[1], 0, [])

print("The fastest way from A to B is: " + str(find_fastest_way(all_ways)))
