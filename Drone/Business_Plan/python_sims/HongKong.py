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

## Data for Hong Kong:
HK = city(1,1,1,1,1,1)
HK.pop = 7451000
HK.area = 1.106
HK.k = 0.01
HK.period = 5
HK.price_kwh = 0.145 #USD
HK.work_day = 8

dr = drone(1,1,1,1,1,1)
dr.autonomy = 30 #autonomy of the drone in minutes
dr.speed = 50 #average speed of the drone in km/h
dr.bat_charge = 10000 #batery charge in mAh
dr.bat_tension = 14.8 #voltage of the battery
dr.bat_time = 1 #hours to fully charge battery
dr.price_drone = 1000 #price of 1 drone

cnt = context(HK, dr)

hkcomp = company(cnt, 360, 60, 2)



# =============================================================================
# for k in range(1, 10000):
#     HK.k = k/10000
#     cnt = context(HK, dr)
#     hkcomp = company(cnt, 360, 60, 2)
#     ar_x.append(HK.k)
#     ar_y.append(hkcomp.profit)
#     
# plt.plot(ar_x, ar_y)
# 
# ar_x1 = []
# ar_y1 = []
# 
# for k in range(1, 100000):
#     dr.price = k
#     cnt = context(HK, dr)
#     hkcomp = company(cnt, 360, 60, 2)
#     ar_x1.append(dr.price)
#     ar_y1.append(hkcomp.profit)
#     
# fig, axs = plt.subplots(2)
# axs[0].plot(ar_x, ar_y)
# axs[0].suptitle("Profit against demand")
# axs[1].plot(ar_x1, ar_y1)
# axs[1].suptitle("Profit against drone price")
# =============================================================================


    

# =============================================================================
# ar_x = []
# ar_y = []
# 
# for k in range(1, 10000):
#     HK.k = k/10000
#     cnt = context(HK, dr)
#     hkcomp = company(cnt, 360, 60, 2)
#     ar_x.append(HK.k)
#     ar_y.append(hkcomp.profit)
#     
# plt.plot(ar_x, ar_y)
# 
# ar_x = []
# ar_y = []
# 
# for k in range(1, 10000):
#     HK.k = k/10000
#     cnt = context(HK, dr)
#     hkcomp = company(cnt, 360, 60, 2)
#     ar_x.append(HK.k)
#     ar_y.append(hkcomp.profit)
#     
# plt.plot(ar_x, ar_y)
# =============================================================================
    
    



