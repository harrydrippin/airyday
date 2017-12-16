import requests, json
from config import FlightPlanConfig as FPC

class FlightPlan:
    """
    UBI-KAIS의 Flight Plan을 가져와서 해석합니다.
    """

    # FPL의 정규 주소 템플릿
    fpl_template = 'http://ubikais.fois.go.kr/sysUbikais/biz/fpl/selectViewFpl.fois?amsRecPk={amsRecPk}&dummy={dummy}'

    @classmethod
    def get(cls, amsRecPk, dummy="A123218181"):
        """
        해당 amsRecPk에 따른 FPL을 찾아서 정규화합니다.
        성공 시에 FPL 형식의 Dictionary를, 실패 시에 None을 반환합니다.
        """

        # amsRecPk의 타입을 통해 요청이 불가능한 경우 None을 반환합니다.
        if amsRecPk == None:
            print("[-] No amsRecPk Found")
            return None

        # 템플릿을 통해 FPL 링크를 정의합니다.
        fpl_link = cls.fpl_template.format(amsRecPk=amsRecPk, dummy=dummy)

        # GET 요청을 통해 JSON을 받아옵니다.
        fpl_response = requests.get(fpl_link)

        # Session Fail일 경우 HTML이 반환되는 점을 이용해 실패 여부를 판정합니다.
        if fpl_response.text.count("<body>") != 0:
            print("[-] UBI-KAIS Session Fail")
            return None

        # 성공한 JSON을 String으로 변환합니다.
        fpl_json = fpl_response.json()

        # JSON에서, UBIKAIS측 System Fail을 검출합니다.
        if fpl_json["status"] != "success":
            print("[-] UBI-KAIS System Fail")
            return None

        # FPL을 검출합니다.
        fpl_str = fpl_json["records"][0]["amsOriginal"]

        # 파싱한 FPL을 반환합니다.
        return cls.parse(fpl_str)
    
    @classmethod
    def parse(cls, fpl):
        """
        주어진 FPL String을 ICAO FPL Standard에 맞추어 파싱합니다.
        실패했을 경우 None을, 성공했을 경우 해당 Dictionary를 반환합니다.
        """
        # 괄호를 기준으로 AMS Prefix를 제외한 실제 FPL을 분리해냅니다.
        fpl_start, fpl_end = fpl.index("(") + 1, fpl.index(")")
        fpl_real = fpl[fpl_start:fpl_end].strip().replace("\r\n", "")

        # FPL이 들어갈 Dictionary를 초기화합니다.
        ret = dict()
        
        # 아이템을 '-' 기준으로 나눕니다.
        fpl_items = fpl_real.split("-")
        
        # 6. MESSAGE TYPE (일반적으로 'FPL')
        ret["message_type"] = fpl_items[0]

        # 7. AIRCRAFT IDENTIFICATION (편명)
        ret["aircraft_id"] = fpl_items[1]

        # 8. FLIGHT RULES AND TYPES (비행 방법과 유형)
        fpl_rules, fpl_types = fpl_items[2][0], fpl_items[2][1]

        # 8-1. FLIGHT RULES (비행 방법)
        ret["flight_rules"] = {
            "code": fpl_rules,
            "explain": FPC.flight_rules[fpl_rules]
        }

        # 8-2. FLIGHT TYPES (비행 유형)
        ret["flight_types"] = {
            "code": fpl_types,
            "explain": FPC.flight_types[fpl_types]
        }

        # 9. AIRCRAFT INFORMATION (항공기 정보)
        fpl_aircraft_info = fpl_items[3].split("/")

        # 9-1. AIRCRAFT TYPE (항공기 종류)
        ret["aircraft_type"] = fpl_aircraft_info[0]

        # 9-2. WAKE TURBULENCE (비행익상 소용돌이)
        ret["wake_turbulence"] = {
            "code": fpl_aircraft_info[1],
            "explain": FPC.wake_turbulence[fpl_aircraft_info[1]]
        }

        # 10. EQUIPMENT AND CAPABILITIES (장착 장비와 기능성) 
        pass
        
        return ret

if __name__ == "__main__":
    print(json.dumps(FlightPlan.get("48993912"), indent=4, ensure_ascii=False))