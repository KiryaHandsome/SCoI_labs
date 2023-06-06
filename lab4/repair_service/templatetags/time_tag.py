import datetime
import logging

import dateutil.tz as tz
import requests
from django import template

register = template.Library()

API_URL = 'http://ip-api.com/json/'

logger = logging.getLogger('')


@register.simple_tag
def current_time():
    logger.info(f'SENT REQUEST TO {API_URL}')
    ip_request = requests.get(API_URL)
    ip_request = ip_request.json()
    time_zone = ip_request['timezone']
    date_data = datetime.datetime.now(tz=tz.gettz(time_zone)).strftime('%d/%m/%Y')
    return f'{date_data}, {time_zone}'
