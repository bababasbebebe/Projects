# import numba as nb

# new elem operations

def bin_search_for_sublist(sublists, item, coord, offset) -> int:
    """binary search for pointer in sublistS"""

    midpoint = len(sublists) // 2
    if sublists[midpoint][0][coord] == item:
        return midpoint + offset
    if item < sublists[midpoint][0][coord]:
        return bin_search_for_sublist(sublists[:midpoint], item, coord, offset)
    offset += midpoint + 1
    return bin_search_for_sublist(sublists[midpoint + 1:], item, coord, offset)


def bin_search_for_point(sublist, item, coord, offset) -> int:
    """binary search for pointer in sublist"""

    midpoint = len(sublist) // 2
    if sublist[midpoint][coord] == item:
        return midpoint + offset
    if item < sublist[midpoint][coord]:
        return bin_search_for_point(sublist[:midpoint], item, coord, offset)
    offset += midpoint + 1
    return bin_search_for_point(sublist[midpoint + 1:], item, coord, offset)


def sublist_form(elem_points) -> list[list]:
    """form x and y sublists"""

    x_sublists = []
    y_sublists = []

    elem_points_copy = elem_points.copy()
    elem_points.sort()
    # формирование отсортированных саблистов по х и у
    for point in range(len(elem_points) - 1):
        if elem_points[point][0] != elem_points[point - 1][0]:
            start = point
            point += 1
            while point != len(elem_points) and elem_points[point][0] == elem_points[point - 1][0]:
                point += 1
            sublist = sorted(elem_points[start:point], key=lambda x: x[1])
            y_sublists.append(sublist)

    elem_points_copy.sort(key=lambda x: x[1])
    for point in range(len(elem_points_copy) - 1):
        if elem_points_copy[point][1] != elem_points_copy[point - 1][1]:
            start = point
            point += 1
            while point != len(elem_points_copy) and elem_points_copy[point][1] == elem_points_copy[point - 1][1]:
                point += 1
            sublist = sorted(elem_points_copy[start:point], key=lambda x: x[0])
            x_sublists.append(sublist)
            # print("x_sub", x_sublists)
            # print("y_sub", y_sublists)

    return [y_sublists] + [x_sublists]


def delete_repeating_points(_list):
    """find and delete repeating points in list"""

    _list.sort()
    offset = 0
    index = 0
    while (index - offset) < len(_list) - 1:
        if _list[index - offset] == _list[index - offset + 1]:
            _list.pop(index - offset)
            offset += 1
        index += 1
    return _list


def elem_to_points(elem) -> list:
    """element structure x1,y1,x2,y2... structure changes to [x1,y1],[x2,y2],... point structure"""

    points = []

    for i in range(0, len(elem) - 1, 2):
        points.append([elem[i], elem[i + 1]])

    return points


def points_to_elem(points) -> list:
    """point structure [x1,y1],[x2,y2],... changes to x1,y1,x2,y2... element structure"""

    element_points = []
    for coord in points:
        element_points.append(coord[0])
        element_points.append(coord[1])

    return element_points


def form_element(start_points) -> list:
    """form element from points"""

    list_of_sublists = sublist_form(start_points)  # сп    # # print("before checker: ", list_of_sublists)
    # print("x: ", list_of_sublists[0], "\n", "y: ", list_of_sublists[1])

    # print("after checker: ", list_of_sublists)
    form_points = [list_of_sublists[0][0][0]]  # итоговый список сформированного элемента
    elem_start = form_points[0]  # начальная точка отсчета(для рассмотрения замыканий)

    switch = True  # переход между саблистами
    x_or_y = 0  # какой саблист выбран
    pointer = list_of_sublists[0][0][1]  # указатель на точку
    point_counter = 0  # счетчик пройденных точек
    points_amount = len(start_points)  # всего точек

    while point_counter != points_amount - 1:
        point_counter += 1

        # ПЕРЕДЕЛАТЬ
        if pointer == elem_start:

            for i in range(0, len(list_of_sublists[x_or_y]) - 1):
                for j in range(0, len(list_of_sublists[x_or_y][i]) - 1):
                    if list_of_sublists[x_or_y][i][j] not in form_points:
                        pointer = list_of_sublists[x_or_y][i][j]
                        elem_start = pointer
                        break

        # disjunction
        """if flag == 1: 
            if pointer in interior_and_intersect_points:
                interior_or_intersect_pointer = pointer
            else:
                last_pointer = pointer"""
        # # print(form_points)
        form_points.append(pointer)

        # Переход из одного саблиста в другой
        if switch:
            x_or_y = 1
            switch = not switch
        else:
            x_or_y = 0
            switch = not switch

        # поиск элемента в другом саблисте
        num_of_sublist = bin_search_for_sublist(list_of_sublists[x_or_y], pointer[int(not switch)], int(not switch), 0)
        num_of_point = bin_search_for_point(list_of_sublists[x_or_y][num_of_sublist], pointer[int(switch)], int(switch),
                                            0)

        # выбор относительно четности элемента с каким элементом соединять
        if num_of_point % 2 == 0:
            pointer = list_of_sublists[int(not switch)][num_of_sublist][num_of_point + 1]
        else:
            pointer = list_of_sublists[int(not switch)][num_of_sublist][num_of_point - 1]

    # print("form", form_points)
    form_points[1:] = form_points[-1:-len(form_points):-1]
    # print("form_reverse", form_points)
    element_points = points_to_elem(form_points)

    return element_points
