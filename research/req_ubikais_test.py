import requests
Arr = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectArr.fois?downloadYn=1&srchDate=2017-12-15&srchDatesh=20171215&srchAl=&srchFln=&srchDep=&srchArr=RKSI&dummy=175827665&cmd=get-records&limit=100&offset=0'
response = requests.get(Arr)
rep = response.json()
#print(rep["records"][0]["amsOriginal"])

print("status : ", rep["status"],"\n\n")
for i in rep["records"]:
    print("편명 : ", i["fpId"])
    print("등록번호 :", i["acId"])
    print("기종 :", i["acType"])
    print("출발공항 :", i["apIcao"])
    print("출발예정시간 :", i["staDate"], i["schTime"])
    print("출발시각 :", i["staDate"], i["sta"])
    print("도착공항 :", i["apArr"])
    print("예정도착시간 :", i["schDate"], i["eta"])
    print("실제도착시간 :", i["schDate"], i["ata"])
    print("램프/램프인 :", i["standArr"],"/", i["blockOnTime"])
    print("현재상태 :", i["arrStatus"])
    print("amsRecPk / flightPk :", i["amsRecPk"], i["flightPk"])
    print("\n[FPL]\n")

    aRP = {
    'aRP' : i["amsRecPk"],
    'dummy' : 'A182955307'
    }

    import requests
    FPL = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectViewFpl.fois?amsRecPk={aRP}&dummy={dummy}'
    response = requests.get(FPL.format(**aRP))
    if i["amsRecPk"] == None:
        print("FPL이 없습니다!")
    else:
        FPLrep = response.json()
        print(FPLrep["records"][0]["amsOriginal"])
    print("-" * 70, end="\n\n")