"""
    Flight Plan Parser
    @author harrydrippin
"""
import requests

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

        print(fpl_str)

if __name__ == "__main__":
    FlightPlan.get("48993912")