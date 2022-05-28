# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:49:09 2022

@author: Admin
"""

# Rtop = 100
# Rvar = 10
# Rbot = 3.01


# 2000 Ohm & 39.0 kOhm -> 23.53 V (Theoretical: 25.2 V), Diff:  2.07 V
#  860 Ohm & 20.0 kOhm -> 26.66 V (Theoretical: 31.2 V), Diff:  4.54 V
#  680 Ohm & 15.0 kOhm -> 23.64 V (Theoretical: 28.4 V), Diff:  4.75 V
#  680 Ohm & 18.0 kOhm -> 28.00 V (Theoretical: 33.8 V), Diff:  5.80 V
#  470 Ohm & 12.0 kOhm -> 25.33 V (Theoretical: 32.6 V), Diff:  7.27 V
#  270 Ohm &  6.8 kOhm -> 21.75 V (Theoretical: 32.2 V), Diff: 10.45 V
#  270 Ohm &  6.8 kOhm -> 21.75 V (Theoretical: 32.2 V), Diff: 10.45 V


Rtop = 39000
Rvar = 10000
Rbot = 2000

Vref = 1.23

Umax = (Vref / Rbot) * (Rbot + Rtop)
Umin = (Vref / (Rbot + Rvar)) * (Rbot + Rvar + Rtop)


print(f"Umin: {Umin:.1f} V")
print(f"Umax: {Umax:.1f} V")