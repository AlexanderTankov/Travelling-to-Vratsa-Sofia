# -*- coding: utf-8 -*-
from facebook_logger import Facebook_Logger
from datetime import date


class Travel():

    def __init__(self, day, month, year, destination, hour, free_spots=3):
        self.day = day
        self.month = month
        self.year = year

        days = {'Monday': 'Понеделник',
                'Tuesday': 'Вторник',
                'Wednesday': 'Сряда',
                'Thursday': 'Четвъртък',
                'Friday': 'Петък',
                'Saturday': 'Събота',
                'Sunday': 'Неделя'
                }

        self.weekday = days[date(int(year), int(month), int(day)).strftime('%A')]
        self.destination = destination
        self.hour = hour
        self.free_spots = free_spots

    def search_people(self, fbAPI):
        fb_logger = Facebook_Logger(fbAPI, self)
            

    
        

