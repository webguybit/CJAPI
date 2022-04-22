import maxminddb
import os
import json
import pprint
pp = pprint.PrettyPrinter(indent=2)
from re import sub

from config import PROJECT_ROOT
MMURL = os.path.join(PROJECT_ROOT,  'GeoLite2-City.mmdb')

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])

def country_lookup(ip):
    city_name = 'unknownCountry'
    try:
        with maxminddb.open_database(MMURL) as reader:
            city_info = reader.get(ip)
            # pp.pprint(city_info)
            city_name = city_info['country']['names']['en']
        return camel_case(city_name)
    except Exception as e:
        print(e)
        return city_name

# print(country_lookup('127.0.0.1'))
        
