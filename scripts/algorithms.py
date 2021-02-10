def bresenham(initial_pixel: list, final_pixel: list) -> list:
    swap_x_and_y = False
    swap_x = False
    swap_y = False

    m = (final_pixel[1] - initial_pixel[1]) / (final_pixel[0] - initial_pixel[0])

    if m > 1 or m < -1:
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

    x = initial_pixel[0]
    y = initial_pixel[1]

    m = (final_pixel[1] - initial_pixel[1]) / (final_pixel[0] - initial_pixel[0])  # TODO: Separar calculo dos deltas

    e = m - 0.5

    result_list = list()

    result_list.append([x, y])

    while x < final_pixel[0]:
        if e >= 0:
            y += 1
            e -= 1
        x += 1
        e += m

        result_list.append([x, y])  # Desenha o ponto

    if swap_x_and_y or swap_x or swap_y:
        for result in result_list:
            if swap_y is True:
                result[1] = result[1]*(-1)
            if swap_x is True:
                result[0] = result[0]*(-1)
            if swap_x_and_y is True:
                result[0], result[1] = result[1], result[0]

            result_list[result_list.index(result)] = result

    return result_list

