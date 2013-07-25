
IA_WEST  = -96.7
IA_EAST  = -90.1
IA_NORTH = 43.61
IA_SOUTH = 40.37

MW_WEST  = -104.2
MW_EAST  = -80.1
MW_NORTH = 49.51
MW_SOUTH = 35.47


""" Convert NWSLI codes to a state code """
nwsli2state = {
"A2": "AK", "A1": "AL", "A4": "AR", "A3": "AZ", "C1": "CA", "C2": "CO",
"C3": "CT", "D2": "DC", "D1": "DE", "F1": "FL", "G1": "GA", "G5": "GM",
"H1": "HI", "I4": "IA", "I1": "ID", "I2": "IL", "I3": "IN", "K1": "KS",
"K2": "KY", "L1": "LA", "M3": "MA", "M2": "MD", "M1": "ME", "M4": "MI",
"M5": "MN", "M7": "MO", "M6": "MS", "M8": "MT", "N7": "NC",
"N8": "ND", "N1": "NE", "N3": "NH", "N4": "NJ", "N5": "NM", "N2": "NV",
"N6": "NY", "O1": "OH", "O2": "OK", "O3": "OR", "P5": "P1", "P6": "P2",
"P7": "P3", "P8": "P4", "P1": "PA", "R1": "RI", "S1": "SC", "S2": "SD",
"T1": "TN", "T2": "TX", "U1": "UT", "V2": "VA", "V1": "VT", "W1": "WA",
"W3": "WI", "W2": "WV", "W4": "WY", "Q1": "AB", "Q2": "BC", "Q3": "MB",
"B3": "NB", "N9": "NF", "S4": "NS", "Q5": "NW",
"Q6": "ON", "E1": "PE", "Q7": "PQ", "Q8": "SK",
"Q9": "YK", "A5": "AG", "B1": "BJ", "C6": "CH", "C8": "CI", "C7": "CL",
"C4": "CM", "C5": "CP", "D3": "DF", "D4": "DR",
"G2": "GJ", "G3": "GR", "H2": "HD", "J1": "JL", "C9": "MC", "R2": "MR",
"X1": "MX", "L3": "NL", "R3": "NR",
"O4": "OX", "P9": "PB", "S3": "SL", "S5": "SN", "S6": "SO", "T3": "TB",
"T5": "TL", "T4": "TP", "V4": "VC", "Y1": "YC", "Z1": "ZC", "E2": "ES",
"G4": "GT", "H3": "HO", "R5": "JA", "R6": "NU", "L3": "PO", "P4": "PR",
"R4": "RK", "V3": "VI", "CH": "CH", "CL": "CL", "TP": "TP",
}


hailsize = {
 '0.25' : "pea",
 '0.50' : "marble",
 '0.75' : "penny",
 '0.88' : "nickel",
 '1.00' : "quarter",
 '1.25' : "half dollar",
 '1.50' : "ping pong ball",
 '1.75' : "golf ball",
 '2.00' : "egg",
 '2.50' : "tennis ball",
 '2.75' : "baseball",
 '3.00' : "teacup",
 '4.00' : "grapefruit",
 '4.50' : "softball"}

lsr_events = {
 'BLOWING SNOW': 'a',
 'DRIFTING SNOW': 'a',
 'HIGH SUST WINDS': 'A',
 'DOWNBURST': 'B',
 'FUNNEL CLOUD': 'C',
 'FUNNEL': 'C',
 'TSTM WND DMG': 'D',
 'TREES DOWN': 'D',
 'TSTM WIND DMG': 'D',
 'FLOOD': 'E',
 'FLOODING': 'E',
 'FLASH FLOOD' : 'F',
 'MAJ FLASH FLD': 'F',
 'TSTM WND GST': 'G',
 'TSTM WIND': 'G',
 'TSTM WIND GST': 'G',
 'HAIL': 'H',
 'MARINE HAIL': 'H',
 'EXCESSIVE HEAT': 'I',
 'DENSE FOG': 'J',
 'FOG': 'J',
 'LIGHTNING STRIKE': 'K',
 'LIGHTNING': 'L',
 'MARINE TSTM WND': 'M',
 'MARINE TSTM WIND': 'M',
 'NON-TSTM WND GST': 'N',
 'NON TSTM WND GST': 'N',
 'NON-TSTM WND DMG': 'O',
 'NON TSTM WND DMG': 'O',
 'NON-TSTM DMG GST': 'O',
 'NON TSTM DMG GST': 'O',
 'NON-TSTM DMG': 'O',
 'NON-TSTM WND': 'O',
 'HIGH WINDS': 'O',
 'WND DAMAGE': 'O',
 'RIP CURRENTS': 'P',
 'RIP CURRENT': 'P',
 'HIGH SURF': 'P',
 'TROPICAL STORM': 'Q',
 'HEAVY RAIN': 'R',
 'RAIN': 'R',
 'SNOW': 'S',
 'STORM TOTAL SNOW': 'S',
 'SLEET': 's',
 'MODERATE SLEET': 's',
 'HEAVY SLEET': 's',
 'HEAVY SNOW': 'S',
 'TORNADO' : 'T',
 'WILDFIRE' : 'U',
 'FIRE' : 'U',
 'AVALANCHE': 'V',
 'WALL CLOUD': 'X',
 'WATER SPOUT': 'W',
 'WATERSPOUT': 'W',
 'BLIZZARD' : 'Z',
 'HURRICANE': '0',
 'STORM SURGE': '1',
 'DUST STORM': '2',
 'SPRINKLES - FEW': '3',
 'HIGH ASTR TIDES': '4',
 'LOW ASTR TIDES': '4',
 'FREEZING RAIN': '5',
 'FREEZING DRIZZLE': '5',
 'ICE STORM': '5',
 'ICING ON ROADS': '5',
 'EXTREME COLD': '6',
 'FREEZE': '6',
 'EXTR WIND CHILL': '7',
 'WILDFIRE': '8',
 'SEICHE': '9',
 'VOLCANIC ASHFALL': 'z',
 'TSUNAMI': 'y',
 'DEBRIS FLOW': 'x',
 'COASTAL FLOOD': 'v',
 'LAKESHORE FLOOD': 'u',
 'SNEAKER WAVE': 't', 
}

name2ptyz = {
    'GMT': 'UTC',
    'CHDT': 'Etc/GMT-8', 'CHST': 'Etc/GMT-9', 'LST': 'Etc/GMT-10',
    'ADT': 'Etc/GMT-3',
    'VDT': 'Etc/GMT-3', 'VST': 'Etc/GMT-4',
    'EDT': 'US/Eastern', 'AST': 'Etc/GMT-4',
    'CDT': 'US/Central', 'EST': 'US/Eastern', 
    'MDT': 'US/Mountain', 'CST': 'US/Central',
    'PDT': 'US/Pacific', 'MST': 'US/Mountain',
    'AKDT': 'US/Alaska', 'PST': 'US/Pacific',
    'HDT': 'US/Hawaii', 'AKST': 'US/Alaska',
           'HST': 'US/Hawaii',
    'SST':'Etc/GMT+11',
    'PLT': 'Etc/GMT-5',
    'GSST': 'Etc/GMT-4',         
}

offsets = {
 'GMT': 0,
 'CHDT': -8, 'CHST': -9, 'LST': -10,
 'ADT': 3,
 'VDT': 3, 'VST': 4,
 'EDT': 4, 'AST': 4,
 'CDT': 5, 'EST': 5, 
 'MDT': 6, 'CST': 6,
 'PDT': 7, 'MST': 7,
 'AKDT': 8, 'PST': 8,
 'HDT': 9, 'AKST': 9,
           'HST':10,
 'SST':11,
 'PLT': -5,
 'GSST': -4,
}

wfo_dict =  {
 "ABQ": {"name": "ALBUQUERQUE" ,"region": "SR"},
 "ABR": {"name": "ABERDEEN" ,"region": "CR"},
 "AFC": {"name": "ANCHORAGE" ,"region": "PR"},
 "AFG": {"name": "FAIRBANKS" ,"region": "PR"},
 "AJK": {"name": "JUNEAU" ,"region": "PR"},
 "AKQ": {"name": "WAKEFIELD" ,"region": "ER"},
 "ALY": {"name": "ALBANY" ,"region": "ER"},
 "AMA": {"name": "AMARILLO" ,"region": "SR"},
 "APX": {"name": "GAYLORD" ,"region": "CR"},
 "ARX": {"name": "LA_CROSSE" ,"region": "CR"},
 "BGM": {"name": "BINGHAMTON" ,"region": "ER"},
 "BIS": {"name": "BISMARCK" ,"region": "CR"},
 "BMX": {"name": "BIRMINGHAM" ,"region": "SR"},
 "BOI": {"name": "BOISE" ,"region": "WR"},
 "BOU": {"name": "DENVER" ,"region": "CR"},
 "BOX": {"name": "TAUNTON" ,"region": "ER"},
 "BRO": {"name": "BROWNSVILLE" ,"region": "SR"},
 "BTV": {"name": "BURLINGTON" ,"region": "ER"},
 "BUF": {"name": "BUFFALO" ,"region": "ER"},
 "BYZ": {"name": "BILLINGS" ,"region": "WR"},
 "CAE": {"name": "COLUMBIA" ,"region": "SR"},
 "CAR": {"name": "CARIBOU" ,"region": "ER"},
 "CHS": {"name": "CHARLESTON" ,"region": "SR"},
 "CLE": {"name": "CLEVELAND" ,"region": "ER"},
 "CRP": {"name": "CORPUS_CHRISTI" ,"region": "SR"},
 "CTP": {"name": "STATE_COLLEGE" ,"region": "ER"},
 "CYS": {"name": "CHEYENNE" ,"region": "CR"},
 "DDC": {"name": "DODGE_CITY" ,"region": "CR"},
 "DLH": {"name": "DULUTH" ,"region": "CR"},
 "DMX": {"name": "DES_MOINES" ,"region": "CR"},
 "DTX": {"name": "DETROIT" ,"region": "CR"},
 "DVN": {"name": "QUAD_CITIES_IA" ,"region": "CR"},
 "EAX": {"name": "KANSAS_CITY/PLEASANT_HILL" ,"region": "CR"},
 "EKA": {"name": "EUREKA" ,"region": "WR"},
 "EPZ": {"name": "EL_PASO_TX/SANTA_TERESA" ,"region": "SR"},
 "EWX": {"name": "AUSTIN/SAN_ANTONIO" ,"region": "SR"},
 "EYW": {"name": "KEY_WEST" ,"region": "SR"},
 "FFC": {"name": "PEACHTREE_CITY" ,"region": "SR"},
 "FGF": {"name": "EASTERN_NORTH_DAKOTA" ,"region": "CR"},
 "FGZ": {"name": "FLAGSTAFF" ,"region": "WR"},
 "FSD": {"name": "SIOUX_FALLS" ,"region": "CR"},
 "FWD": {"name": "DALLAS/FORT_WORTH" ,"region": "SR"},
 "GGW": {"name": "GLASGOW" ,"region": "WR"},
 "GID": {"name": "HASTINGS" ,"region": "CR"},
 "GJT": {"name": "GRAND_JUNCTION" ,"region": "CR"},
 "GLD": {"name": "GOODLAND" ,"region": "CR"},
 "GRB": {"name": "GREEN_BAY" ,"region": "CR"},
 "GRR": {"name": "GRAND_RAPIDS" ,"region": "CR"},
 "GSP": {"name": "GREENVILLE/SPARTANBURG" ,"region": "ER"},
 "GUM": {"name": "Guam" ,"region": "SR"},
 "GYX": {"name": "GRAY" ,"region": "ER"},
 "HFO": {"name": "HONOLULU" ,"region": "PR"},
 "HGX": {"name": "HOUSTON/GALVESTON" ,"region": "SR"},
 "HNX": {"name": "SAN_JOAQUIN_VALLEY/HANFORD" ,"region": "WR"},
 "HUN": {"name": "Huntsville" ,"region": "SR"},
 "ICT": {"name": "WICHITA" ,"region": "CR"},
 "ILM": {"name": "WILMINGTON" ,"region": "ER"},
 "ILN": {"name": "WILMINGTON" ,"region": "ER"},
 "ILX": {"name": "LINCOLN" ,"region": "CR"},
 "IND": {"name": "INDIANAPOLIS" ,"region": "CR"},
 "IWX": {"name": "NORTHERN_INDIANA" ,"region": "CR"},
 "JAN": {"name": "JACKSON" ,"region": "SR"},
 "JAX": {"name": "JACKSONVILLE" ,"region": "SR"},
 "JKL": {"name": "JACKSON" ,"region": "ER"},
 "JSJ": {"name": "San Juan" ,"region": "SR"},
 "LBF": {"name": "NORTH_PLATTE" ,"region": "CR"},
 "LCH": {"name": "LAKE_CHARLES" ,"region": "SR"},
 "LIX": {"name": "NEW_ORLEANS" ,"region": "SR"},
 "LKN": {"name": "ELKO" ,"region": "WR"},
 "LMK": {"name": "LOUISVILLE" ,"region": "CR"},
 "LOT": {"name": "CHICAGO" ,"region": "CR"},
 "LOX": {"name": "LOS_ANGELES/OXNARD" ,"region": "WR"},
 "LSX": {"name": "ST_LOUIS" ,"region": "CR"},
 "LUB": {"name": "LUBBOCK" ,"region": "SR"},
 "LWX": {"name": "BALTIMORE_MD/_WASHINGTON_DC" ,"region": "ER"},
 "LZK": {"name": "LITTLE_ROCK" ,"region": "SR"},
 "MAF": {"name": "MIDLAND/ODESSA" ,"region": "SR"},
 "MEG": {"name": "MEMPHIS" ,"region": "SR"},
 "MFL": {"name": "MIAMI" ,"region": "SR"},
 "MFR": {"name": "MEDFORD" ,"region": "WR"},
 "MHX": {"name": "NEWPORT/MOREHEAD_CITY" ,"region": "ER"},
 "MKX": {"name": "MILWAUKEE/SULLIVAN" ,"region": "CR"},
 "MLB": {"name": "MELBOURNE" ,"region": "SR"},
 "MOB": {"name": "MOBILE" ,"region": "SR"},
 "MPX": {"name": "TWIN_CITIES/CHANHASSEN" ,"region": "CR"},
 "MQT": {"name": "MARQUETTE" ,"region": "CR"},
 "MRX": {"name": "MORRISTOWN" ,"region": "SR"},
 "MSO": {"name": "MISSOULA" ,"region": "WR"},
 "MTR": {"name": "SAN_FRANCISCO" ,"region": "WR"},
 "OAX": {"name": "OMAHA/VALLEY" ,"region": "CR"},
 "OHX": {"name": "NASHVILLE" ,"region": "SR"},
 "OKX": {"name": "NEW_YORK" ,"region": "ER"},
 "OTX": {"name": "SPOKANE" ,"region": "WR"},
 "OUN": {"name": "NORMAN" ,"region": "SR"},
 "PAH": {"name": "PADUCAH" ,"region": "CR"},
 "PBZ": {"name": "PITTSBURGH" ,"region": "ER"},
 "PDT": {"name": "PENDLETON" ,"region": "WR"},
 "PHI": {"name": "MOUNT_HOLLY" ,"region": "ER"},
 "PIH": {"name": "POCATELLO/IDAHO_FALLS" ,"region": "WR"},
 "PQR": {"name": "PORTLAND" ,"region": "WR"},
 "PSR": {"name": "PHOENIX" ,"region": "WR"},
 "PUB": {"name": "PUEBLO" ,"region": "CR"},
 "RAH": {"name": "RALEIGH" ,"region": "ER"},
 "REV": {"name": "RENO" ,"region": "WR"},
 "RIW": {"name": "RIVERTON" ,"region": "WR"},
 "RLX": {"name": "CHARLESTON" ,"region": "ER"},
 "RNK": {"name": "BLACKSBURG" ,"region": "ER"},
 "SEW": {"name": "SEATTLE" ,"region": "WR"},
 "SGF": {"name": "SPRINGFIELD" ,"region": "CR"},
 "SGX": {"name": "SAN_DIEGO" ,"region": "WR"},
 "SHV": {"name": "SHREVEPORT" ,"region": "SR"},
 "SJT": {"name": "SAN_ANGELO" ,"region": "SR"},
 "SJU": {"name": "SAN_JUAN" ,"region": "SR"},
 "SLC": {"name": "SALT_LAKE_CITY" ,"region": "WR"},
 "STO": {"name": "SACRAMENTO" ,"region": "WR"},
 "TAE": {"name": "TALLAHASSEE" ,"region": "SR"},
 "TBW": {"name": "TAMPA_BAY_AREA/RUSKIN" ,"region": "SR"},
 "TFX": {"name": "GREAT_FALLS" ,"region": "WR"},
 "TOP": {"name": "TOPEKA" ,"region": "CR"},
 "TSA": {"name": "TULSA" ,"region": "WR"},
 "TWC": {"name": "TUCSON" ,"region": "WR"},
 "UNR": {"name": "RAPID_CITY" ,"region": "CR"},
 "VEF": {"name": "LAS_VEGAS" ,"region": "WR"},
}

centertext = {
    "SPC": "Storm Prediction Center",
    "WNS": "Storm Prediction Center",
    "NHC": "National Hurricane Center",
    "WNH": "Hydrometeorological Prediction Center",
    "WNO": "NCEP Central Operations",
}

prodDefinitions = {
    'TOR': 'Tornado Warning (TOR)',
    'SVR': 'Severe Thunderstorm Warning (SVR)',
    'SVS': 'Severe Weather Statement (SVS)',
    'RFD': 'Grassland Fire Danger (RFD)',
    'TWO': 'Tropical Weather Outlook (TWO)',
    'PWO': 'Public Severe Weather Outlook (PWO)',
    'TCM': 'Tropical Storm Forecast (TCM)',
    'TCU': 'Tropical Cyclone Update (TCU)',
    'HLS': 'Hurricane Local Statement (HLS)',
    'NOW': 'Short-term Forecast (NOW)',
    'HWO': 'Hazardous Weather Outlook (HWO)',
    'AFD': 'Area Forecast Discussion (AFD)',
    'AWU': 'Area Weather Update (AWU)',
    'PNS': 'Public Information Statement (PNS)',
    'FFW': 'Flash Flood Warning (FFW)',
    'FLS': 'Flood Advisory (FLS)',
    'FFS': 'Flash Flood Statement (FFS)',
    'FLW': 'Flood Warning (FLW)',
    'ESF': 'Hydrologic Outlook (ESF)',
    'PSH': 'Post Tropical Event Report (PSH)',
    'RER': 'Record Event Report (RER)',
    'FTM': 'Free Text Message (FTM)',
    'ADM': 'Administrative Message (ADM)',
    'CAE': 'Child Abduction Emergency (CAE)',
    'ADR': 'Administrative Message (ADR)',
    'TOE': 'Telephone Outage Emergency (TOE)',
    'LAE': 'Local Area Emergency (LAE)',
    'AVA': 'Avalanche Watch (AVA)',
    'AVW': 'Avalanche Warning (AVW)',
    'CDW': 'Civil Danger Warning (CDW)',
    'CEM': 'Civil Emergency Message (CEM)',
    'EQW': 'Earthquake Warning (EQW)',
    'EVI': 'Evacuation Immediate (EVI)',
    'FRW': 'Fire Warning (FRW)',
    'HMW': 'Hazardous Materials Warning (HMW)',
    'LEW': 'Law Enforcement Warning (LEW)',
    'NMN': 'Network Message Notification (NMN)',
    'NUW': 'Nuclear Power Plant Warning (NUW)',
    'RHW': 'Radiological Hazard Warning (RHW)',
    'SPW': 'Shelter In Place Warning (SPW)',
    'VOW': 'Volcano Warning (VOW)',
    'ZFP': 'Zone Forecast Package (ZFP)',
    'PFM': 'Point Forecast Matrices (PFM)',
    'SFT': 'State Forecast Tabular Product (SFT)',
    'SRF': 'Surf Zone Forecast (SRF)',
    'CWF': 'Coastal Waters Forecast (CWF)',
    'RVS': 'Hydrologic Statement (RVS)',
    'HPA': 'High Pollution Advisory (HPA)',
    'RTP': 'Regional Temperature and Precipitation (RTP)',
    'FWF': 'Fire Weather Planning Forecast (FWF)',
    'DGT': 'Drought Information (DGT)',
    'MWS': 'Marine Weather Statement (MWS)',
    'AQA': 'Air Quality Alert (AQA)',
    'DSA': 'Tropical Disturbance Statement (DSA)',
    'TCE': 'Tropical Cyclone Position Estimate (TCE)',
    'RVF': 'River Forecast (RVF)',
    'RVA': 'Hydrologic Summary (RVA)',
    'EQR': 'Earthquake Report (EQR)',
    'OEP': 'TAF Collaboration Product (OEP)',
    'SIG': 'Convective Sigment (SIG)',
    'VAA': 'Volcanic Ash Advisory (VAA)',
}