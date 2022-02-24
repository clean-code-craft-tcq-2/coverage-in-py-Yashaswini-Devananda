import enum

class Range:
    def __init__(self, **kwargs):
        self.lowerlimit = kwargs.get('lowerlimit', 0)
        self.upperlimit = kwargs.get('upperlimit', 0)
        
    def classify_breach(self, parameter_value): #classify breach check
        if parameter_value < self.lowerlimit:
            return BreachType.TOO_LOW
        elif parameter_value > self.upperlimit:
            return BreachType.TOO_HIGH
        return BreachType.NORMAL

def check_and_alert(alertTarget, batteryChar , temperatureInC):
    message = ""
    breachType = cooling_type_list[batteryChar['CoolingType']].classify_breach(temperatureInC)
    if alertTarget == AlertTarget.TO_CONTROLLER:
        message = send_to_controller(breachType)
    if breachType!=BreachType.NORMAL:
        if alertTarget == AlertTarget.TO_EMAIL: # alerts 
            message = send_to_email(breachType)
    return message
    

def send_to_controller(breachType):
    header = alerter_ref_strings[AlertTarget.TO_CONTROLLER]
    message = f'{header}, {infer_breach(breachType)}'
    # print(message)
    return message


def send_to_email(breachType):
    recepient = "a.b@c.com"
    message = (f'To: {recepient}\n')
    message += f"{alerter_ref_strings[AlertTarget.TO_EMAIL]}{breach_ref_strings[breachType]}"
    # print(message)
    return message

def infer_breach(breach):
    return (BreachType(breach).name)
    
cooling_type_list = []
cooling_type_list.append(Range(lowerlimit = 0, upperlimit = 35)) # PASSIVE_COOLING
cooling_type_list.append(Range(lowerlimit = 0, upperlimit = 45)) # HI_ACTIVE_COOLING
cooling_type_list.append(Range(lowerlimit = 0, upperlimit = 40)) # MED_ACTIVE_COOLING


    
class AlertTarget(enum.IntEnum):
    TO_CONTROLLER = 0
    TO_EMAIL = 1
    AlertTarget_count = 2
    
alerter_ref_strings = ["Header","Hi, the temperature is "]
breach_ref_strings = ["too low","too high"]

CoolingType = {"PASSIVE_COOLING" : 0, "HI_ACTIVE_COOLING" : 1, "MED_ACTIVE_COOLING" : 2 } #look up cooling type


battery = {"CoolingType" : CoolingType["PASSIVE_COOLING"] }

class BreachType(enum.IntEnum):
    TOO_LOW = 0
    TOO_HIGH = 1
    NORMAL = 2
    BreachType_Count = 3
