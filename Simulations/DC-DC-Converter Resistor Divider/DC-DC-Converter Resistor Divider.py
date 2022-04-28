# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:49:09 2022

@author: Admin
"""

Rtop = 100
Rvar = 10
Rbot = 3.01

Vref = 1.23

Umax = (Vref / Rbot) * (Rbot + Rtop)
Umin = (Vref / (Rbot + Rvar)) * (Rbot + Rvar + Rtop)


print(f"Umin: {Umin:.1f} V")
print(f"Umax: {Umax:.1f} V")