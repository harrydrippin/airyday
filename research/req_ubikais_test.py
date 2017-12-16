import requests
Arr = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectArr.fois?downloadYn=1&srchDate=2017-12-15&srchDatesh=20171215&srchAl=&srchFln=&srchDep=&srchArr=RKSI&dummy=175827665&cmd=get-records&limit=100&offset=0'
response = requests.get(Arr)
rep = response.json()
#print(rep["records"][0]["amsOriginal"])

print("status : ", rep["status"],"\n\n")
for i in rep["records"]:
    FltNum =  "편명 : " + i["fpId"]
    RegNum = "\n등록번호 : " + ("Not Assigned" if i["acId"] == None else i["acId"])
    AcType = "\n기종 : " + i["acType"]
    Orig = "\n출발공항 : " + i["apIcao"]
    ActDep = "\n출발시각 : " + i["staDate"] + " " + i["sta"]
    Dest = "\n도착공항 : " + i["apArr"]
    EstArr = "\n도착시간 : " + i["schDate"] + " " + ("None" if i["eta"] == None else i["eta"])
    Ramp = "\n램프/램프인 : " + ("Not Assigned" if i["standArr"] == None else i["standArr"]) + " / " + ("None" if i["blockOnTime"] == None else i["blockOnTime"])
    Stat = "\n현재상태 : " +  ("None" if i["arrStatus"] == None else i["arrStatus"])
    PriKey = "\namsRecPk / flightPk : " + str(i["amsRecPk"]) + " / " + str(i["flightPk"])
    FplHead = "\n\n[FPL]\n"
    
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