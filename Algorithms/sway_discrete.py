#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2016, Jianfeng Chen <jchen37@ncsu.edu>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.


from __future__ import division
from Algorithms.sway_sampler import sway, cont_dominate
from gmpy2 import popcount, mpz
import random


def count1(decint):
    return popcount(mpz(decint))


def split_products(pop, groupC=5):
    rand = random.choice(pop)
    center = count1(int(rand, 2))

    workloads = list()
    dists = list()
    for p in pop:
        wl = count1(int(p, 2))
        dist = count1(wl ^ center)
        workloads.append(wl)
        dists.append(dist)

    poptuple = [(p, i, j) for p, i, j in zip(pop, workloads, dists)]

    # sort by the workloads
    poptuple = sorted(poptuple, key=lambda i:i[1])

    n = int(len(poptuple)/groupC)
    groups = [poptuple[i*n:i*n+n] for i in range(groupC)]

    west, east, westItems, eastItems = list(), list(), list(), list()

    for g in groups:
        k = sorted(g, key=lambda i:i[2])

        # filling the answers
        west.append(k[0][0])
        east.append(k[-1][0])
        westItems.extend(map(lambda i: i[0], k[:len(k)//2]))
        eastItems.extend(map(lambda i: i[0], k[len(k)//2:]))

    return west, east, westItems, eastItems


def comparing(part1, part2):
    onewin = 0
    twowin = 0

    for i, j in zip(part1, part2):
        if cont_dominate(i, j) > 0:
            onewin += 1
        else:
            twowin += 1

    return onewin >= twowin


def optimize(init_pop, eval_func):
    import warnings
    warnings.filterwarnings('ignore')
    return sway(init_pop, eval_func, split_products, comparing)