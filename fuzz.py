# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:39:36 2020

@author: mario
"""


import numpy as np
import skfuzzy as fuzz

# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
def fis( qual, serv, [a,b,c,d,e,f,g,h,i,j,k,l] ):
    x_qual = np.arange(0, 11, 1)
    x_serv = np.arange(0, 11, 1)
    x_tip  = np.arange(0, 26, 1)
    
    # Generate fuzzy membership functions
    qual_lo = fuzz.trimf(x_qual, [a, b, c])
    qual_md = fuzz.trimf(x_qual, [d, e, f])
    qual_hi = fuzz.trimf(x_qual, [g, 10, 10])
    
    serv_lo = fuzz.trimf(x_serv, [0, h, i])
    serv_md = fuzz.trimf(x_serv, [0, j, k])
    serv_hi = fuzz.trimf(x_serv, [l, 10, 10])
    
    tip_lo = fuzz.trimf(x_tip, [0, 0, 12])
    tip_md = fuzz.trimf(x_tip, [0, 12, 25])
    tip_hi = fuzz.trimf(x_tip, [15, 25, 25])
    
    qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, qual)
    qual_level_md = fuzz.interp_membership(x_qual, qual_md, qual)
    qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, qual)

    serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, serv)
    serv_level_md = fuzz.interp_membership(x_serv, serv_md, serv)
    serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, serv)
    
    active_rule1 = np.fmax(qual_level_lo, serv_level_lo)
    tip_activation_lo = np.fmin(active_rule1, tip_lo)
    
    tip_activation_md = np.fmin(serv_level_md, tip_md)
    active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
    tip_activation_hi = np.fmin(active_rule3, tip_hi)
    
    aggregated = np.fmax(tip_activation_lo,
                     np.fmax(tip_activation_md, tip_activation_hi))

    # Calculate defuzzified result
    tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
    return tip

print(fis(6.8, 9.8)) # 19.86871794871795
print(fis(9.8, 6.2)) # 14.73946220298622
print(fis(1, 6.2))   # 10.861837419879945
print(fis(6.8, 9.2)) # 17.409762738234146
print(fis(9.8, 2.2)) # 13.373494881187186
print(fis(2, 6.2))   # 11.339482339482338









        
    
    
    
    
    