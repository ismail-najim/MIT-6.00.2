#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:07:41 2020

@author: inajim
"""
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    #initialize
    result = np.zeros(len(choices))
    best_result = np.zeros(len(choices))
    close_value = 0
    close_result = np.zeros(len(choices))
    
    #define all combinations
    for i in range(2**len(choices)):
        
        #define and run for one combination
        for j in range(len(choices)):
            result[j] = (i // 2**j) % 2
        
        
        #does the combination work?
        if np.sum(result * choices) == total and (best_result.sum() ==0 or result.sum() < best_result.sum()):
            best_result = result.copy()
        
        #do we have a result that works so far?
        elif best_result.sum() == 0 and np.sum(result * choices) < total and (close_value ==0 or total-np.sum(result * choices) < close_value):
            close_value = total - np.sum(result*choices)
            close_result = result.copy()
    best_result = best_result.astype(int) 
    close_result = close_result.astype(int)            
    if best_result.sum() >0:
        return best_result
    else:
        return close_result
        
                