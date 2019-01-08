#!/usr/bin/env python

import requests

print(requests.__verision__)

r = requests.get("www.google.com")
print(r.status.code)

print(r.headers)


