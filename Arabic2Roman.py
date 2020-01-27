# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:13:20 2019

@author: 18367
"""
def arabic2roman(num):
  arabic_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  roman_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  res=''
  for i in range(len(arabic_list)):
    while num>=arabic_list[i]:
      num-=arabic_list[i]
      res+=roman_list[i]
  return res


        