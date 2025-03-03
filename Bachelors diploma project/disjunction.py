import pyclipper
import elemoperations

def disj(element1, element2) -> list:
    """disjunction of 2 elements +"""
    # Если элемент пустой - вывод другого, если оба пустые - вывод None
    if len(element1) == 0 and len(element2) == 0:
        return []
    elif len(element1) == 0:
        return element2
    elif len(element2) == 0:
        return element1

    # Частный случай совпадения элементов
    if element1 == element2:
        return element1

    #if element1[0] == element1[-2] and element1[1] == element1[-1]:
    #    element1 = element1[0:len(element1) - 2]
    if type(element1[0]) == int:
        element1 = [elemoperations.elem_to_points(element1)]

    #if element2[0] == element2[-2] and element2[1] == element2[-1]:
    #    element2 = elemoperations.elem_to_points(element2[0:len(element2) - 2])
    if type(element2[0]) == int:
        element2 = [elemoperations.elem_to_points(element2)]

    pc = pyclipper.Pyclipper()
    pc.AddPaths(element1, pyclipper.PT_SUBJECT, True)
    pc.AddPaths(element2, pyclipper.PT_CLIP, True)


    solution = pc.Execute(pyclipper.CT_UNION, pyclipper.PFT_EVENODD, pyclipper.PFT_NONZERO)

    # print("el1+el2=sol: ",[element1, element2], solution)
    # print("LLLLLLLLL", len(element1))
    # if solution[-1][-1][0] == 1350:
        #for elem in element1:
            #solution.append(elem)
        # for elem in element2:
            # solution.append(elem)

        # print("ASDASBHJDHJAHSJGJIASHGACVHDIJOJHGASUIGHVHUIOUHJBJIOJHKB", solution)



    if len(solution[0]) == 1:
        solution = solution[0]

    return solution