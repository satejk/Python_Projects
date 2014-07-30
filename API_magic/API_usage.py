# Author : SATEJ VINAYAK KHANDEPARKAR
# HALMSTAD UNIVERSITY , SWEDEN
# MASTERS IN EMBEDDED AND INTELLIGENT SYSTEMS

#!/usr/bin/python 


import requests


response = requests.get("http://placekitten.com")

print response.status_code
print response.headers
print response.text[599:1000]
