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
