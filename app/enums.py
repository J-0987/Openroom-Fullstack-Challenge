from enum import Enum

class SexEnum(str, Enum):
    """Enumeration for biological sex."""
    male = "male"
    female = "female"
    other = "other"
    prefer_not_to_say = "prefer not to say"

class ProvinceEnum(str, Enum):
    """Enumeration for Canadian provinces."""
    ON = "Ontario"
    QC = "Quebec"
    BC = "British Columbia"
    AB = "Alberta"
    MB = "Manitoba"
    SK = "Saskatchewan"
    NS = "Nova Scotia"
    NB = "New Brunswick"
    PE = "Prince Edward Island"
    NL = "Newfoundland and Labrador"
    NT = "Northwest Territories"
    YT = "Yukon"
    NU = "Nunavut"