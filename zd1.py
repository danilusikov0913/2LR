#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Подсчитайте количество гласных в строке, введенной с клавиатуры с использованием множеств.
if __name__ == "__main__":

    # Определим универсальное множество
    a = set("aeiouy")
    print('Введите строку')
    b = set(input())

    # Найдем количество гласных
    c = a.intersection(b)
    print(len(c))
    print(c)

