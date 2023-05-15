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

def zone_countries(lat_range=(-90, 90), long_range=(-180, 180)):
    return [code for code, loc in listB if float(loc[0]) >= lat_range[0] and
            float(loc[0]) <= lat_range[1] and
            float(loc[1]) >= long_range[0] and
            float(loc[1]) <= long_range[1]]

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

while 1:
    print("1: 리스트 A,리스트 B 프린트\t 2:적도 남단의 모든 국가명 출력\t 3:사용자가 국가코드를 입력하면 국가명 출력\t 4: 종료")
    key = int(input("key 입력: "))
    if key == 1:
        print(listA)
        print(listB)
    elif key == 2:
        print(zone_countries(lat_range=(36, 38), long_range=(126, 128)))
    elif key == 3:
        counry = input("검색 원하는 국가코드 입력: ")
        print(get_country_name(counry))
    elif key == 4:
        break



southern_country_codes = zone_countries((-90, 0))
print(southern_country_codes)
print(get_country_name(southern_country_codes))