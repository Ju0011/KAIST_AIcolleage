listA = list()
listB = list()
header = True
with open("./average-latitude-longitude-countries.csv", "r") as f:
    for line in f:
        if header:
            header = False
            continue
        items = line.strip().split(",")
        listA.append((items[0].strip('"'), ",".join(items[1:-2]).strip('"')))
        listB.append((items[0].strip('"'), (items[-2], items[-1])))
        # lines.append(line.strip().split(","))
        # split 함수 인자의 이름이 sep (separator)
        # CSV = Comma-separated Values
        # TSV = Tab-separated Values
#print(listA)
#print(listB)

# define ranges for countries within lat/long ranges
# return country codes
def zone_countries(lat_range=(-90, 90), long_range=(-180, 180)):
    return [code for code, loc in listB if float(loc[0]) >= lat_range[0] and
            float(loc[0]) <= lat_range[1] and
            float(loc[1]) >= long_range[0] and
            float(loc[1]) <= long_range[1]]

#print(zone_countries(lat_range=(36, 38), long_range=(126, 128)))

# take country code/s and return country name
def get_country_name(code):
    if type(code) is list:
        return_list = list()
        for one_code in code:
            return_list += [cn for cc, cn in listA if cc == one_code]
        return return_list
    elif type(code) is str: # e.g., "KR"
        # print("str")
        return [cn for cc, cn in listA if cc == code]
    else:
        return


#print(get_country_name("KR"))

southern_country_codes = zone_countries((-90, 0))
print(southern_country_codes)
print(get_country_name(southern_country_codes))