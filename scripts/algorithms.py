import math


def bresenham(initial_pixel: list, final_pixel: list) -> list:
    try:
        m_reflection = (final_pixel[1] - initial_pixel[1]) / (final_pixel[0] - initial_pixel[0])
    except ZeroDivisionError:
        m_reflection = 2

    swap_x_and_y, swap_x, swap_y = reflection(m_reflection, initial_pixel, final_pixel)

    x = initial_pixel[0]
    y = initial_pixel[1]

    delta_x = final_pixel[0] - initial_pixel[0]
    delta_y = (final_pixel[1] - initial_pixel[1])

    m = delta_y / delta_x

    e = m - 0.5

    result_list = list()

    result_list.append([x, y])

    while x < final_pixel[0]:
        if e >= 0:
            y += 1
            e -= 1
        x += 1
        e += m

        result_list.append([x, y])

    if swap_x_and_y or swap_x or swap_y:
        result_list = reverse_reflection(result_list, swap_x, swap_y, swap_x_and_y)

    return result_list


def reflection(m_reflection: int, initial_pixel: list, final_pixel: list) -> tuple:
    swap_x_and_y = False
    swap_x = False
    swap_y = False

    if m_reflection > 1 or m_reflection < -1:
        initial_pixel[0], initial_pixel[1] = initial_pixel[1], initial_pixel[0]
        final_pixel[0], final_pixel[1] = final_pixel[1], final_pixel[0]
        swap_x_and_y = True

    if initial_pixel[0] > final_pixel[0]:
        initial_pixel[0] = initial_pixel[0] * (-1)
        final_pixel[0] = final_pixel[0] * (-1)
        swap_x = True

    if initial_pixel[1] > final_pixel[1]:
        initial_pixel[1] = initial_pixel[1] * (-1)
        final_pixel[1] = final_pixel[1] * (-1)
        swap_y = True

    return swap_x_and_y, swap_x, swap_y


def reverse_reflection(result_list: list, swap_x: bool, swap_y: bool, swap_x_and_y: bool) -> list:
    for result in result_list:
        if swap_y is True:
            result[1] = result[1] * (-1)
        if swap_x is True:
            result[0] = result[0] * (-1)
        if swap_x_and_y is True:
            result[0], result[1] = result[1], result[0]

        result_list[result_list.index(result)] = result

    return result_list


def circle(initial_pixel, final_pixel=None, r=None):
    no_radius_return = None
    radius = None
    if final_pixel:
        point = [final_pixel[0] - initial_pixel[0], final_pixel[1] - initial_pixel[1]]
        radius = math.floor(math.sqrt((point[0] ** 2 + point[1] ** 2)))
        no_radius_return = False
    if r:
        radius = r
        no_radius_return = True

    x = 0
    y = radius
    e = 1 - radius

    result = list()
    result.append([x, y])

    while x <= y:
        e += 2 * x + 1
        x += 1
        if e >= 0:
            e += 2 - 2 * y
            y -= 1
        result.append([x, y])

    leng = len(result)
    ct = 0
    for po in result:
        result.append([po[1], po[0]])
        result.append([po[1]*(-1), po[0]])
        result.append([po[0]*(-1), po[1]])
        result.append([po[0]*(-1), po[1]*(-1)])
        result.append([po[1]*(-1), po[0]*(-1)])
        result.append([po[1], po[0]*(-1)])
        result.append([po[0], po[1]*(-1)])
        ct += 1
        if ct == leng:
            break

    for po in result:
        po[0], po[1] = po[0] + initial_pixel[0], po[1] + initial_pixel[1]

    if no_radius_return:
        return result
    else:
        return radius, result

