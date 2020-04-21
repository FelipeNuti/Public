# -*- coding: utf-8 -*-
"""
Estimating the viability of a drone delivery business
"""
import numpy as np

pi = np.pi

#City variables:
pop = 750000 #number of inhabitants
period = 4 #number of days between consecutive orders for household/medicine supplies
area = 140 #number of square kilometers of the urban area of the city
price_kwh = 0.2237 #price of 1 kWh in the city 
work_day = 12 #hours available for delivery
k = 0.15 #fraction of people in the city that actually use the delivery service

#Drone variables:
autonomy = 30 #autonomy of the drone in minutes
speed = 50 #average speed of the drone in km/h
bat_charge = 6000 #batery charge in mAh
bat_tension = 14.8 #voltage of the battery
bat_time = 1 #hours to fully charge battery
price_drone = 10000 #price of 1 drone

#Consequences of city variables:
radius = (area/pi)**0.5 #city approximated to a circle - radius in km
mean_distance = (2/3) * radius #average distance from a point to the center of the city (km)
dialy_demand = (pop*k)/period #number of deliveries needed in 1 day

#Consequences of drone variables:
bat_energy = bat_charge * bat_tension/1000000 #energy of 1 full charge in kWh
max_distance = 0.5 * speed * (autonomy/60) #maximum distance the delivery site can be from the center (km)

#Consequences of both drone and city:
avg_delivery_time = 2*mean_distance/speed #average delivery time in hours
del_p_opcy = max_distance/mean_distance #deliveries per operation cycle
op_cycle = del_p_opcy*(avg_delivery_time)+bat_time #hours per operation cycle (between two charges)
bat_price = bat_energy * price_kwh #price to charge 1 drone once
del_per_day = (work_day/op_cycle) * del_p_opcy #deliveries a drone makes, on average, in one day
energy_per_day = del_per_day * bat_energy #kwh spent per day per drone
price_per_day = energy_per_day * price_kwh #money spent on charging the drone in one day
drones_needed = dialy_demand/del_per_day 
energy_expense = price_per_day * drones_needed #total money spent on energy spent in 1 day
drone_expense = price_drone * drones_needed


time_to_break_even = 30 #days

# drone_expense + time*energy_expense = price_charged * time * (pop * k/period)

min_price_charged = (drone_expense + time_to_break_even*energy_expense)/(time_to_break_even * (pop * k/period))

print("You need to charge at least", min_price_charged, "per delivery.")

actual_price_charged = 5
time_company = 150 #number of days of operation
profit = actual_price_charged*(pop * k/period)*(time_company) - (drone_expense + time_company*energy_expense)
average_profit = profit/time_company

print("The total profit of the undertaking would be", profit, ", and the average profit would be", average_profit, "per day.")