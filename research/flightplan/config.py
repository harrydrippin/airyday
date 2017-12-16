class FlightPlanConfig:
    """
    FPL 분석에 필요한 Token들을 선언하고 분석 함수를 정의합니다.
    """

    # 8-1. FLIGHT RULES (비행 방법)
    flight_rules = {
        "I": "IFR (계기 비행)",
        "V": "VFR (시계 비행)",
        "Y": "IFR에서 VFR로 비행 중 변경",
        "Z": "VFR에서 IFR로 비행 중 변경"
    }

    # 8-2. FLIGHT TYPES (비행 유형)
    flight_types = {
        "S": "여객기, 운송기 (예정됨)",
        "N": "여객기, 운송기 (예정되지 않음)",
        "G": "일반 항공기 (전용기, 훈련기, 경비행기 등)",
        "M": "군용 항공기",
        "X": "기타"
    }

    # 9-2. WAKE TURBULENCE (비행익상 소용돌이)
    wake_turbulence = {
        "H": "강력함 (이륙 질량 136,000kg 이상)",
        "M": "일반적 수준 (이륙 질량 7,000kg ~ 136,000kg)",
        "L": "약함 (이륙 질량 7,000 미만)"
    }

    # 10-1. EQUIPMENTS (장착 장비)
    equipments = {
        "N": "일반 COM/NAV/APPR 장비 사용 안 함 / 불가능",
        "S": "일반 COM/NAV/APPR 장비 (VHF, VOR, ILS)",
        "A": "GBAS Ldg System",
        "B": "LPV",
        "C": "Loran C",
        "D": "DME",
        "E1": "FMC WPR ACARS",
        "E2": "D-FIS ACARS",
        "E3": "PDC ACARS",
        "F": "ADF",
        "G": "GPS / GNSS",
        "H": "HF RTF",
        "I": "INS (Inertial Nav)",
        "J1": "CPDLC ATN VDL Mode 2",
        "J2": "CPDLC FANS 1/A HFDL",
        "J3": "CPDLC FANS 1/A VDL Mode 4",
        "J4": "CPDLC FANS 1/A VDL Mode 2",
        "J5": "CPDLC FANS 1/A SATCOM (INMARSAT)",
        "J6": "CPDLC FANS 1/A SATCOM (MTSAT)",
        "J7": "CPDLC FANS 1/A SATCOM (Iridium)",
        "K": "MLS",
        "L": "ILS",
        "M1": "ATC RTF SATCOM (INMARSAT)",
        "M2": "ATC RTF (MTSAT)",
        "M3": "ATC RTF (Iridium)",
        "O": "VOR",
        "R": "PBN (추가 정보란에 PBN으로 명시함)",
        "T": "TACAN",
        "U": "UHF RTF",
        "V": "VHF RTF",
        "W": "RVSM (FL290-FL410)",
        "X": "MNPS",
        "Y": "8.33 kHz Radio",
        "Z": "기타 (추가 정보란에 COM, NAV, DAT로 명시함)"
    }

    # 10-2. TRANSPONDER TYPE (응답기 유형)
    transponder_type = {
        "N": "감시 장비 없음",
        "A": "Mode A만 장착됨 (고도 보고 기능 없음)",
        "C": "Mode C",
        "E": "Mode S (비행기 ID, 기압 고도, ADS-B)",
        "H": "Mode S (비행기 ID, 기압 고도, 발전된 감시 기능)",
        "I": "Mode S (비행기 ID)",
        "L": "Mode S (비행기 ID, 기압 고도, ADS-B, 발전된 감시 기능)",
        "P": "Mode S (기압 고도)",
        "S": "Mode S (비행기 ID, 기압 고도)",
        "X": "Mode S (모든 정보 제외)"
    }

    # 10-3. ADS-B / ADS-C
    ads_type = {
        "B1": "ADS-B (전용 출력 기능)",
        "B2": "ADS-B (전용 입출력 기능)",
        "U1": "ADS-B (UAT 기반 출력 기능)",
        "U2": "ADS-B (UAT 기반 입출력 기능)",
        "V1": "ADS-B (VDL Mode 4 기반 출력 기능)",
        "V2": "ADS-B (VDL Mode 4 기반 입출력 기능)",
        "D1": "ADS-C (FANS 1/A)",
        "G1": "ADS-C (ATN)"
    }

    # 13. DEPARTURE AERODROME (도착 비행장)
    departure_aerodrome = {
        "ZZZZ": "설정되지 않음 (추가 정보란에서 DEP로 명시함)",
        "AFIL": "이 FPL이 비행 중 접수됨 (추가 정보란에서 DEP로 명시함)"
    }

    # 15-1. CRUISING SPEED (비행 속도)
    # 단위와 이후 문자의 갯수를 포함한 Tuple로 나타냅니다.
    cruising_speed = {
        "K": ("km/h", 4),
        "N": ("kt", 4),
        "M": ("Mach", 3)
    }

    # 15-2. LEVELS (비행 고도)
    # 단위와 이후 문자의 갯수를 포함한 Tuple로 나타냅니다.
    level = {
        "F": ("FL (100ft)", 3),
        "S": ("m", 4),
        "A": ("100ft", 3),
        "M": ("10m", 4),
        "VFR": ("명시하지 않음 (시계 비행)", 0)
    }

    @classmethod
    def get_equips_and_capabilities(cls, token_str):
        """
        Item 10번에 있는 토큰 행렬을 파싱합니다.
        """
        ret = {
            "equipments": list(),
            "transponder": {
                "code": str(),
                "explain": str()
            },
            "ads": list()
        }
        token_split = token_str.split("/")
        fpl_equip, fpl_capa = token_split[0], token_split[1]

        # Equipments 문자열을 한 글자씩 분석하고 모든 문자열이 적용될 때까지 반복합니다.
        cur = str()
        for i in range(0, len(fpl_equip)):
            cur += fpl_equip[i]
            if cur in cls.equipments:
                ret["equipments"].append({
                    "code": cur,
                    "explain": cls.equipments[cur]
                })
                cur = str()

        # Transponder는 fpl_capa의 첫 문자입니다.
        ret["transponder"]["code"] = fpl_capa[0]
        ret["transponder"]["explain"] = cls.transponder_type[fpl_capa[0]]

        # fpl_capa에서 첫 글자를 제거합니다.
        fpl_capa = fpl_capa[1:]

        # ADS Type은 무조건 2글자이므로, 2글자씩 읽어들여 분석합니다.
        for i in range(0, len(fpl_capa), 2):
            cur = fpl_capa[i:i + 2]
            ret["ads"].append({
                "code": cur,
                "explain": cls.ads_type[cur]
            })
        
        return ret
    
    @classmethod
    def get_speed_and_level(cls, token_str):
        """
        Item 15번에 있는 토큰 행렬을 파싱합니다.
        """
        # 비행 속도의 단위와 값을 분석합니다.
        ret_speed = {
            "speed": int(),
            "unit": str()
        }
        speed_unit = token_str[0]
        speed_end_ind = cls.cruising_speed[speed_unit][1] + 1
        ret_speed["unit"] = cls.cruising_speed[speed_unit][0]
        ret_speed["speed"] = int(token_str[1:speed_end_ind])

        # 비행 레벨의 단위와 값을 분석합니다.
        ret_level = {
            "level": int(),
            "unit": str()
        }
        level_unit = token_str[speed_end_ind]

        # 시계 비행 상황일 경우 Level 파싱을 건너뜁니다.
        if level_unit == "V":
            ret_level["unit"] = cls.level["VFR"]
            ret_level["level"] = 0
        else:
            ret_level["unit"] = cls.level[level_unit][0]
            ret_level["level"] = int(token_str[speed_end_ind + 1:])

        return ret_speed, ret_level