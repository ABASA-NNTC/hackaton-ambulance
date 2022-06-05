import os
import json
import requests
import pandas as pd
import re


class HolidaysParser:
    @staticmethod
    def dload_holidays(year, filename=None):
        holiday_dload_url = f'http://xmlcalendar.ru/data/ru/{year}/calendar.json'
        response = requests.get(holiday_dload_url)
        if response.ok:
            with open(filename, 'w') as file:
                file.write(response.text)
        else:
            raise requests.RequestException("this year is not exists in calendar")

    @staticmethod
    def get_holidays(year, filename=None):
        if filename is None:
            filename = f'{year}.json'

        if not os.path.exists(filename):
            HolidaysParser.dload_holidays(year, filename)

        with open(filename) as file:
            holidays_dict = json.load(file)

        holidays = []
        for month in holidays_dict['months']:
            n_month = month['month']
            days = re.findall(r'\d+', month['days'])
            for day in days:
                day = int(day)
                holidays.append(f'%0.2d.%0.2d.%d' % (day, n_month, year))
        return holidays


if __name__ == '__main__':
    print(HolidaysParse.get_holidays(2022))
