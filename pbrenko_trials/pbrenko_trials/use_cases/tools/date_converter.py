from datetime import datetime


def convert_to_date(date_string):
    date_object = datetime.strptime(date_string, "%Y%m%d%H%M%S")
    return date_object