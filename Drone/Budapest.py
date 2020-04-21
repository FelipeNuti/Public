"""
Estimating sensitivity of variables on drone analysis
"""

import drone as d
import matplotlib.pyplot as plt

city = d.city
drone = d.drone
context = d.context
company = d.company
np = d.np

#ar_x1 = []
# 
#ar_y1 = []
#  
#for k in range(1, 100000):
#    BP = city(3011598,5,7626,0.1161,8,k/100000, 3600, 473)
#    cnt = context(BP, drone(30,50,10000,14.8,1,1000))
#    BPcomp = company(cnt, 360, 60, 2)
#    ar_x1.append(k/100000)
#    ar_y1.append(BPcomp.profit)

# =============================================================================
# plt.plot(ar_x1, ar_y1)
# =============================================================================

## Data for Budapest:
BP = city(1752000,
          5,
          525,
          0.1161,
          8,
          0.001, 
          3600, 
          473)


dr = drone(30,
           50,
           10000,
           14.8,
           1,
           1000)

cnt = context(BP, dr)

BPcomp = company(cnt, 360, 60, 4)


ar_x1 = []
 
ar_y1 = []
  
for k in range(1, 10000):
    BP = city(1752000,
          5,
          525,
          0.1161,
          8,
          k/100000, 
          3600, 
          473)
    cnt = context(BP, drone(30,50,10000,14.8,1,1000))
    BPcomp = company(cnt, 360, 60, 2)
    ar_x1.append(k/100000)
    ar_y1.append(BPcomp.profit)
    
#plt.figure(1)
plt.plot(ar_x1, ar_y1, color = 'black')

m_prof = (ar_y1[-1] - ar_y1[0])/(ar_x1[-1] - ar_x1[0])

ar_x1 = []
 
ar_y1 = []
for k in range(1, 10000):
    BP = city(1752000,
          5,
          525,
          0.1161,
          8,
          k/100000, 
          3600, 
          473)
    cnt = context(BP, drone(30,50,10000,14.8,1,1000))
    BPcomp = company(cnt, 360, 60, 2)
    ar_x1.append(k/100000)
    ar_y1.append(BPcomp.income)
    
#plt.figure(2)
plt.plot(ar_x1, ar_y1, color = 'green')
m_inc = (ar_y1[-1] - ar_y1[0])/(ar_x1[-1] - ar_x1[0])

ar_x1 = []
 
ar_y1 = []
for k in range(1, 10000):
    BP = city(1752000,
          5,
          525,
          0.1161,
          8,
          k/100000, 
          3600, 
          473)
    cnt = context(BP, drone(30,50,10000,14.8,1,1000))
    BPcomp = company(cnt, 360, 60, 2)
    ar_x1.append(k/100000)
    ar_y1.append(cnt.staff_expense + cnt.energy_expense)
    
#plt.figure(3)
plt.plot(ar_x1, ar_y1, color = 'red')
m_exp = (ar_y1[-1] - ar_y1[0])/(ar_x1[-1] - ar_x1[0])






 
