site = raw_input("Get fkey for:")

import urllib2

response = urllib2.urlopen("http://%s" % (site))
page_source = response.read()

import re

line = page_source

print(re.search("\"fkey\"\:\"([a-z0-9]{32})\"",line).group(1))
