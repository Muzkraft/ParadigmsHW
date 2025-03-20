# import pandas as pd
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#
#          if arr[j]> arr[j+1]:
#              arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# my_array = [5, 6, 3, 8, 9, 0,1, 7, 2, 4]
# sorted_array = bubble_sort(my_array)
# print(sorted_array)
#
# dir(pd.DataFrame)

# OOP example

# import math
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __add__(self, other):
#         return  self.area + other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def area(self):
#         self.area = self.width * self.height
#         return self.area
#
#     def perimeter(self):
#         self.perimeter = 2 * (self.width + self.height)
#         return self.perimeter
#
#     def calc_diagonal_length(self):
#         self.diag = (self.width ** 2 + self.height ** 2) ** 0.5
#         return self.diag
#
#     def calc_diag_angles(self):
#         """
#         calculates and returns two angles between the diagonals in degrees
#         :return: first_angle, second angle
#         """
#         if not hasattr(self, 'diag'):
#             self.calc_diagonal_length()
#
#         cos_diag_height = self.height / self.diag
#         angle_diag_height = math.acos(cos_diag_height)
#         angle_diag_height = math.degrees(angle_diag_height)
#         first_angle = 180 - (2 * angle_diag_height)
#         second_angle = (360 - 2 * first_angle) / 2
#         assert (second_angle + first_angle) == 180
#         return first_angle, second_angle
#
# r = Rectangle(10 ,15)
# r2 = Rectangle(3, 4)
# print(r.area())
# print(r.calc_diagonal_length())
# print(r.perimeter())
# print(r.calc_diag_angles())
#
# r2.area()
# print(r + r2)
# print(r == r2)

def sum_squares(lst: list) -> int:
    return sum(map(lambda x: x ** 2, lst))


some_list = [1, 2, 3.5, 4, 5, 6, 7, 8, 9]

print(sum_squares(some_list))

#  function compose
def compose(f, g):
    return lambda x: f(g(x))