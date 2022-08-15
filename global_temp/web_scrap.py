import urllib.request as r

response = r.urlopen(
    'https://www.nsstc.uah.edu/data/msu/v6.0/tlt/uahncdc_lt_6.0.txt')
data = response.read()
print(data)

# Write data to file
filename = "./global_temp/file/global.txt"
file_ = open(filename, 'wb')
file_.write(data)
