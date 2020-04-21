# -*- coding: utf-8 -*-
"""
Estimating the viability of a drone delivery business
"""
import numpy as np

pi = 3.1415926535897932384626433832795028841971

class city:
    def __init__(self, pop, period, area, price_kwh, work_day, k, infrastructure_cost, minwage):
        self.pop = pop
        self.period = period
        self.area = area
        self.price_kwh = price_kwh
        self.work_day = work_day
        self.k = k
        self.radius = (self.area/pi)**0.5
        self.mean_distance =  (2/3) * self.radius
        self.dialy_demand =  (self.pop*self.k)/self.period
        self.infrastructure_cost = infrastructure_cost
        self.minwage = minwage
       
        
class drone:
    def __init__(self, autonomy, speed, bat_charge, bat_tension, bat_time, price_drone):
        self.autonomy = autonomy
        self.speed = speed
        self.bat_charge = bat_charge
        self.bat_tension = bat_tension
        self.bat_time = bat_time
        self.price_drone = price_drone
        self.bat_energy = self.bat_charge * self.bat_tension/1000000
        self.max_distance = 0.5 * self.speed * (self.autonomy/60)
        
    
class context:
    def __init__(self, city, drone):
        self.city = city
        self.drone = drone
        self.avg_delivery_time = 2*city.mean_distance/drone.speed #average delivery time in hours
        self.del_p_opcy = drone.max_distance/city.mean_distance #deliveries per operation cycle
        self.op_cycle = self.del_p_opcy*(self.avg_delivery_time)+drone.bat_time #hours per operation cycle (between two charges)
        self.bat_price = drone.bat_energy* city.price_kwh #price to charge 1 drone once
        self.del_per_day = (city.work_day/self.op_cycle) * self.del_p_opcy #deliveries a drone makes, on average, in one day
        self.energy_per_day = self.del_per_day * drone.bat_energy #kwh spent per day per drone
        self.price_per_day = self.energy_per_day * city.price_kwh #money spent on charging the drone in one day
        self.drones_needed = int(city.dialy_demand/self.del_per_day)
        self.energy_expense = self.price_per_day * self.drones_needed #total money spent on energy spent in 1 day
        self.drone_expense = drone.price_drone * self.drones_needed
        self.staff_num = int(self.city.dialy_demand * 0.4) + 1
        self.staff_expense = self.city.minwage * self.staff_num
        

class company:
    def __init__(self, context, time_company, time_to_break_even, actual_price_charged):
        self.time_to_break_even = time_to_break_even
        self.actual_price_charged = actual_price_charged
        self.time_company = time_company
        self.min_price_charged = (context.drone_expense + self.time_to_break_even*context.energy_expense + context.city.infrastructure_cost)/(self.time_to_break_even * (context.city.pop * context.city.k/context.city.period))
        self.downtime = context.drone_expense/(((self.actual_price_charged * context.city.k * context.city.pop)/context.city.period) - context.energy_expense)
        self.income = self.actual_price_charged*(context.city.pop * context.city.k/context.city.period)*(self.time_company) 
        self.expense = (context.staff_expense + context.city.infrastructure_cost + context.drone_expense + self.time_company*context.energy_expense)
        self.profit = self.income - self.expense





