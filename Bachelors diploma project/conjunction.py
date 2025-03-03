import pyclipper

import elemoperations

def conj(element1, element2) -> list:
    """conjunction of 2 elements *"""

    # Если будет пустой элемент - пересечения нет
    if len(element1) == 0 or len(element2) == 0:
        return []

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

    solution = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD)
    print("el1*el2=sol: ", [element1, element2], solution)

    if len(solution[0]) == 1:
        solution = solution[0]

    return solution
