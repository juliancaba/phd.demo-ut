#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-



from hwt_proxy import sendMessage
from arm_casting_ieee754 import *

import sys
    

def scale2(sum):
    din = []
    din.extend(int_to_byte(float_to_ieee754(sum)))

    idout = sendMessage(0x42000000, 0x00010104, 0x00000001, din)
    _ret = ieee754_to_float(idout[0])
    
    return _ret


def sum_hist_pow(histIN):
    din = []

    for it in histIN:
        din.extend(int_to_byte(float_to_ieee754(it)))

    idout = sendMessage(0x42000000, 0x00010204, 0x00000010, din)

    _ret = ieee754_to_float(idout[0])
    return _ret


def mult_hist_scale(histAUX, scale, histOUT):    
    din = []

    for it in histAUX:
        din.extend(int_to_byte(float_to_ieee754(it)))
        
    din.extend(int_to_byte(float_to_ieee754(scale)))

    idout = sendMessage(0x42000000, 0x00010304, 0x00000011, din)
    
    _ret = []
    for indx in range(0,16):
        _ret.append(ieee754_to_float(idout[indx]))

    histOUT = _ret

