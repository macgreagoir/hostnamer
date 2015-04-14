#!/usr/bin/env python
"""Print randomly generated hostnames"""

from os import urandom

vowels = "euioa"
consonants = "rtpsdfghlcbnm"


def pick(letter, num):
    return ''.join(letter[ord(urandom(1)) % len(letter)] for i in range(num))


def generate():
    return "%s%s%s%s" % (pick(consonants, 1),
                         pick(vowels, 2),
                         pick(consonants, 2),
                         pick(vowels, 1))


for i in range(9):
    print generate()
