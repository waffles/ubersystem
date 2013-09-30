from utils import *
from splinter import Browser
from datetime import timedelta
import datetime
import sys

from hotel_base import *
from hotel_gaylord import *
from hotel_hamptoninn import *

def CheckAllNights(hotels_to_check, night_start, night_end):

    nights = []
    hotel_results = []

    for night in daterange(night_start, night_end):
        nights.append(night)

    browser = Browser()

    try:
        for hotel_to_check in hotels_to_check:
            results = hotel_to_check.check_nights(nights, browser)
            hotel_results.append(results)
    except:
        # sys.exit(-1)
        raise
    else:
        browser.quit()

    return hotel_results