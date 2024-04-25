#!/usr/bin/env python

"""
Download ERA5 Land PPT data...


That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (25.04.2024)"
__email__ = "mdekauwe@gmail.com"


import os
import cdsapi
import sys
import datetime

def get_data(start_year, end_year, start_month, end_month, start_day, end_day,
             lon_min, lat_min, lon_max, lat_max, out_dir):

    st = datetime.datetime.now()

    c = cdsapi.Client()
    variables_list = 'total_precipitation'

    years = [str(start_year +i ) for i in range(end_year-start_year+1)]
    days = [str(start_day +i ).zfill(2) for i in range(end_day-start_day+1)]
    months = [str(start_month +i ).zfill(2) for i in range(end_month-start_month+1)]
    #times = ['00:00', '01:00', '02:00','03:00', '04:00', '05:00', '06:00', '07:00',\
    #         '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00',\
    #         '15:00', '16:00', '17:00','18:00', '19:00', '20:00','21:00', \
    #         '22:00', '23:00']



    # Test
    #days = ['11']
    #months = ['06']
    #times = ['08:00']

    for year in years:
        ofname = os.path.join(out_dir, 'era5land_' + str(year) + '.nc')
        c.retrieve(
        'reanalysis-era5-land',
        {
            'variable': variables_list,
            'year': years,
            'month': months,
            'day': days,
            #'time': times,
            'time': '00:00',
            'area': [
                lat_min, lon_min, lat_max, lon_max
            ],
            'format': 'netcdf',
        },
        ofname)

        print('Process completed in ', datetime.datetime.now()-st)


if __name__ == '__main__':

    start_year = 1950
    end_year = 1950
    start_month = 1
    end_month = 12
    start_day = 1
    end_day = 31

    #lon_min, lat_min, lon_max, lat_max = [79.71, 5.9, 81.88, 9.9] # Sri Lanka
    lon_min, lat_min, lon_max, lat_max = [79.6951668639, 5.96836985923, \
                                          81.7879590189, 9.8240776636] # Sri Lanka


    out_dir = "/Users/xj21307/Desktop/sri_lanka_ppt"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)


    get_data(start_year, end_year, start_month, end_month, start_day, end_day,
             lon_min, lat_min, lon_max, lat_max, out_dir)
