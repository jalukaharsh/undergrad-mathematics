"""MAT354: Complex Analysis"""

import cmath
import numpy as np
import matplotlib.pyplot as plt
import itertools


def flt(a, b, c, d, z) -> None:
    transformation = (a * z + b) / (c * z + d)
    plot(transformation.real, transformation.imag)
    return transformation

def diagonal() -> None:
    x_coord = np.arange(0, 10, 0.01)
    y_coord = np.arange(-10, 0, 0.01)
    y_coord = list(y_coord)
    y_coord.reverse()
    y_coord = np.array(y_coord)
    diagonal = make_complex_array(x_coord, y_coord)
    diagonal_2 = make_complex_array(x_coord, x_coord)
    diagonal = np.append(diagonal_2, diagonal)
    flt(-1, 1, 1, 1, diagonal)



def flt_circle(a, b, c, d, r, center) -> None:
    two_pi_array = np.arange(0, 2 * np.pi, 0.0001)
    x_coord = np.sin(two_pi_array)
    y_coord = np.cos(two_pi_array)
    complex_unit_circle = make_complex_array(x_coord, y_coord)
    my_circle = r * complex_unit_circle + center
    transformation = (a * my_circle + b) / (c * my_circle + d)
    plot(transformation.real, transformation.imag)


def ps3q4(r) -> None:
    x_coord = np.arange(-10, 10, 0.1)
    y_coord = np.arange(-10, 10, 0.1)
    x_line = np.arange(-10, 10, 0.01)
    x_line = x_line + 3j
    y_line = np.arange(0, 10, 0.01)
    imag_y = np.zeros(len(y_line), dtype=complex)
    for i in range(0, len(y_line)):
        imag_y[i] = y_line[i] * 1j
    imag_y += 0
    # complex_plane = [x+y for x in x_coord for y in imag_y]
    # plane_minus_arcs = []
    # for item in complex_plane:
    #     if abs(item.real) > 1 or abs(item.imag) > r:
    #         plane_minus_arcs.append(item)
    # plane_minus_arcs = np.array(plane_minus_arcs)
    # # plot(plane_minus_arcs.real, plane_minus_arcs.imag)
    image = np.array([(r * 1j - 1) / (r * 1j + 1)])
    image = np.append(image, [0])
    plot(image.real, image.imag)


def conc_circle(a, b, c, d, r1, r2, center) -> None:
    flt_circle(a, b, c, d, r1, center)
    flt_circle(a, b, c, d, r2, center)


def ps3q3() -> None:
    x_array = np.arange(-1, 1, 0.0010)
    y_array = np.arange(-1, 1, 0.0010)
    imag_y = np.zeros(len(y_array), dtype=complex)
    for i in range(0, len(y_array)):
        imag_y[i] = y_array[i] * 1j
    complex_plane = [x + y for x in x_array for y in imag_y]
    plane_minus_pos_real = []
    for item in complex_plane:
        if item.real < 1 or item.imag != 0:
            plane_minus_pos_real.append(item)
        else:
            print(item)
    plane_minus_pos_real = np.array(plane_minus_pos_real)
    # plot(plane_minus_pos_real.real, plane_minus_pos_real.imag)
    image = (1 - (1 - plane_minus_pos_real) ** 0.25) / (1 + (1 - plane_minus_pos_real) ** 0.25)
    plot(image.real, image.imag)
    # noninjective_domain = []
    # injective_domain = []
    # counter = 0
    # for i in range(0, len(image)):
    #     indices = [j for j, x in enumerate(image) if abs(x - image[i]) < 0.01]
    #     # print(indices)
    #     if len(indices) > 1:
    #         counter += 1
    #         # print('Common found for', image[i], ':')
    #         for index in indices:
    #             noninjective_domain.append(complex_plane[index])
    #             # print(complex_plane[index])
    #     else:
    #         injective_domain.append(complex_plane[indices[0]])
    # # print(counter)
    # noninjective_domain = np.array(noninjective_domain)
    # injective_domain = np.array(injective_domain)
    # print(injective_domain)
    # # plot(noninjective_domain.real, noninjective_domain.imag)
    # noninj_image = (1 - (1 - noninjective_domain) ** 0.25) / (1 + (1 - noninjective_domain) ** 0.25)
    # # plot(noninj_image.real, noninj_image.imag)
    # inj_image = (1 - (1 - injective_domain) ** 0.25) / (1 + (1 - injective_domain) ** 0.25)
    # plot(inj_image.real, inj_image.imag)


def ps3q7() -> None:
    x_array = np.arange(0, 10, 0.1)
    y_array = np.arange(-10, 10, 0.1)
    imag_y = np.zeros(len(y_array), dtype=complex)
    for i in range(0, len(y_array)):
        imag_y[i] = y_array[i] * 1j
    complex_plane = [x + y for x in x_array for y in imag_y]
    complex_plane = np.array(complex_plane)
    image = complex_plane - (complex_plane ** 2 - 1) ** 0.5
    # plot(image.real, image.imag)
    counter = 0
    noninjective_domain = []
    for i in range(0, len(image)):
        indices = [j for j, x in enumerate(image) if abs(x - image[i]) < 0.01]
        print(indices)
        if len(indices) > 1:
            counter += 1
            print('Common found for', image[i], ':')
            for index in indices:
                noninjective_domain.append(complex_plane[index])
                print(complex_plane[index])
    print(counter)
    noninjective_domain = np.array(noninjective_domain)
    plot(noninjective_domain.real, noninjective_domain.imag)


def make_complex_array(x_coord: np.array, y_coord: np.array) -> np.array:
    complex_array = np.zeros(len(x_coord), dtype=complex)
    for i in range(0, len(x_coord)):
        complex_array[i] = complex(x_coord[i], y_coord[i])
    return complex_array


def plot(x_array: np.array, y_array: np.array) -> None:
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.plot(x_array, y_array, marker='.', ls='')
    plt.show()


########
if __name__ == "__main__":
    diagonal()
