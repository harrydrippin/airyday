search = input("검색하려는 정보를 입력하세요 ARR/DEP : ")

import requests
import time
now = time.localtime()

schCon = {
    'Year' : now.tm_year,
    'Month' : now.tm_mon,
    'Date' : now.tm_mday
}

if search == "ARR":
    URL = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectArr.fois?downloadYn=1&srchDate={Year}-{Month}-{Date}&srchDatesh={Year}{Month}{Date}&srchAl=&srchFln=&srchDep=&srchArr=RKSI&dummy=175827665&cmd=get-records&limit=100&offset=0'
    response = requests.get(URL.format(**schCon))
    rep = response.json()

    result = ''

    print("status : ", rep["status"],"\n")
    for i in rep["records"]:
        result +=  "편명 : " + str(i["fpId"])
        result += "\n등록번호 : " + str(("Not Assigned" if i["acId"] == None else i["acId"]))
        result += "\n기종 : " + str(i["acType"])
        result += "\n출발공항 : " + str(i["apIcao"])
        result += "\n출발시각 : " + str(i["staDate"]) + " " + str(i["sta"])
        result += "\n도착공항 : " + str(i["apArr"])
        result += "\n도착시간 : " + str(i["schDate"]) + " " + str(("None" if i["eta"] == None else i["eta"]))
        result += "\n램프/램프인 : " + str(("Not Assigned" if i["standArr"] == None else i["standArr"])) + " / " + str(("None" if i["blockOnTime"] == None else i["blockOnTime"]))
        result += "\n현재상태 : " +  str(("None" if i["arrStatus"] == None else i["arrStatus"]))
        result += "\namsRecPk / flightPk : " + str(i["amsRecPk"]) + " / " + str(i["flightPk"])
        result += "\n\n[FPL]\n\n"

        aRP = {
        'aRP' : i["amsRecPk"],
        'dummy' : 'A182955307'
        }

        import requests
        FPL = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectViewFpl.fois?amsRecPk={aRP}&dummy={dummy}'
        response = requests.get(FPL.format(**aRP))

        if i["amsRecPk"] == None:
            FPLrep = "FPL이 없습니다!"
        else:
            FPL = response.json()
            FPLrep = FPL["records"][0]["amsOriginal"]

        result += str(FPLrep)
        result += "\n" + "-" * 70 + "\n"

    print(result)
elif search == "DEP":
    URL = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectDep.fois?downloadYn=1&srchDate={Year}-{Month}-{Date}&srchDatesh={Year}{Month}{Date}&srchAl=&srchFln=&srchDep=RKSI&srchArr=&dummy=203004277&cmd=get-records&limit=100&offset=0'
    response = requests.get(URL.format(**schCon))
    rep = response.json()

    result = ''

    print("status : ", rep["status"],"\n")
    for i in rep["records"]:
        result +=  "편명 : " + str(i["fpId"])
        result += "\n등록번호 : " + str(("Not Assigned" if i["acId"] == None else i["acId"]))
        result += "\n기종 : " + str(i["acType"])
        result += "\n출발공항 : " + str(i["apIcao"])
        result += "\n출발시각 : " + str(i["staDate"]) + " " + str(i["sta"])
        result += "\n도착공항 : " + str(i["apArr"])
        result += "\n도착시간 : " + str(i["schDate"]) + " " + str(("None" if i["eta"] == None else i["eta"]))
        result += "\n램프/램프아웃 : " + str(("Not Assigned" if i["standDep"] == None else i["standDep"])) + " / " + str(("None" if i["blockOffTime"] == None else i["blockOffTime"]))
        result += "\n현재상태 : " +  str(("None" if i["depStatus"] == None else i["depStatus"]))
        result += "\namsRecPk / flightPk : " + str(i["amsRecPk"]) + " / " + str(i["flightPk"])
        result += "\n\n[FPL]\n\n"

        aRP = {
        'aRP' : i["amsRecPk"],
        'dummy' : 'A182955307'
        }

        import requests
        FPL = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectViewFpl.fois?amsRecPk={aRP}&dummy={dummy}'
        response = requests.get(FPL.format(**aRP))

        if i["amsRecPk"] == None:
            FPLrep = "FPL이 없습니다!"
        else:
            FPL = response.json()
            FPLrep = FPL["records"][0]["amsOriginal"]

        result += str(FPLrep)
        result += "\n" + "-" * 70 + "\n"

    print(result)
else:
    print("\n ARR과 DEP 중 하나를 입력하세요.")
