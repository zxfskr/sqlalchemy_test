# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Project:        autoops_common
    File Name:      color_helper.py
    Description:
    Author:         puyj(pyjapple@gmail.com)
    Org:            Using.ai
    Date:           2019/6/25
-------------------------------------------------
"""
__author__ = 'puyj'

import random


COLOR_WHEEL = [
    "#E60012",
    "#EB6100",
    "#F39800",
    "#FCC800",
    "#FFF100",
    "#CFDB00",
    "#8FC31F",
    "#22AC38",
    "#009944",
    "#009B6B",
    "#009E96",
    "#00A0C1",
    "#00A0E9",
    "#0086D1",
    "#0068B7",
    "#00479D",
    "#1D2088",
    "#601986",
    "#920783",
    "#BE0081",
    "#E4007F",
    "#E5006A",
    "#E5004F",
    "#E60033",
]


def get_color_wheel(labels, exist_colors=None):
    ret = {}
    if len(labels) == 0:
         return ret
    exist_colors = [] if exist_colors is None else exist_colors
    color_wheel = COLOR_WHEEL.copy()
    for _color in exist_colors:
        color_wheel.remove(_color)
    interval = len(color_wheel) // len(labels)
    if interval == 0:
        for i, label in enumerate(labels):
            ret[label] = '#' + ''.join(random.sample("0123456789ABCDEF", 6))
    else:
        for i, label in enumerate(labels):
            ret[label] = color_wheel[interval * i]
    return ret


if __name__ == '__main__':
    my_colors = get_color_wheel(['A', 'B'], ["#E60012"])
    print(my_colors)
    ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    my_colors_ = get_color_wheel(ls)
    print(my_colors_)