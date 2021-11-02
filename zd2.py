#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Определение общих символов в двух строках, введенных с клавиатуры.
if __name__ == "__main__":
    print('Введитите 1 строку')
    s1 = set(input())
    print('Введитите 2 строку')
    s2 = set(input())

    # Нахождение пересечений
    a = s1.intersection(s2)
    print(a)
    print(len(a))
