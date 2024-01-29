# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.md for details.

import functools
from copy import deepcopy
from car_driver.OPi.constants import BOARD, BCM, SUNXI, CUSTOM


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin (LSX: Only available for OrangePi 5 plus,
    # for other develop board, check github and modify the mapping yourself)
    BOARD: {
        3: 16,
        5: 15,
        7: 62,
        8: 33,
        10: 32,
        11: 36,
        12: 97,
        13: 39,
        15: 40,
        16: 109,
        18: 110,
        19: 42,
        21: 41,
        22: 34,
        23: 43,
        24: 44,
        26: 45,
        27: 47,
        28: 46,
        29: 63, 
        31: 96,
        32: 35,
        33: 114,
        35: 98,
        36: 101,
        37: 113,
        38: 100,
        40: 99
    },

    # BCM pin to actual GPIO pin
    BCM: {
        2: 12,
        3: 11,
        4: 6,
        7: 10,
        8: 13,
        9: 16,
        10: 15,
        11: 14,
        14: 198,
        15: 199,
        17: 1,
        18: 7,
        22: 3,
        23: 19,
        24: 18,
        25: 2,
        27: 0
    },

    SUNXI: _sunXi(),

    # User defined, initialized as empty
    CUSTOM: {
        3:  16,
        5:  15,
        7:  62,
        8:  33,
        11: 36,


    }
}


def set_custom_pin_mappings(mappings):
    _pin_map[CUSTOM] = deepcopy(mappings)


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI, CUSTOM]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
custom = functools.partial(get_gpio_pin, CUSTOM)
