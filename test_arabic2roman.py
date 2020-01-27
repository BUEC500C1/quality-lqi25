# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:56:48 2020

@author: 18367
"""
import pytest
from Arabic2Roman import arabic2roman

def test_result():
    assert arabic2roman(77) == 'LXXVII'
    assert arabic2roman(66) == 'LXVI'
    assert arabic2roman(55) == 'LV'
    assert arabic2roman(8) == 'VIII'
    assert arabic2roman(1200) == 'MCC'
    assert arabic2roman(34) == 'XXXIV'
    assert arabic2roman(65) == 'LXV'
    assert arabic2roman(3) == 'III'
    assert arabic2roman(21) == 'XXI'
    assert arabic2roman(99) == 'XCIX'