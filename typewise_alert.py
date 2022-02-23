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
    breachType = cooling_type_list[batteryChar['CoolingType']].classify_breach(temperatureInC)
    if alertTarget == AlertTarget.TO_CONTROLLER:
        send_to_controller(breachType)
    elif alertTarget == AlertTarget.TO_EMAIL:
        send_to_email(breachType)


def send_to_controller(breachType):
    header = "Header"
    message = f'{header}, {infer_breach(breachType)}'
    print(message)
    return message


def send_to_email(breachType):
    recepient = "a.b@c.com"
    print(f'To: {recepient}')
    if breachType == BreachType.TOO_LOW:
        message = "Hi, the temperature is too low"
    elif breachType == BreachType.TOO_HIGH:
        message = "Hi, the temperature is too high"
    print(message)
    return message

def infer_breach(breach):
    print (BreachType(breach).name)
    
cooling_type_list = []
cooling_type_list.append(Range(lowerlimit = 0, upperlimit = 35)) # PASSIVE_COOLING
cooling_type_list.append(Range(lowerlimit = 0, upperlimit = 45)) # HI_ACTIVE_COOLING
cooling_type_list.append(Range(lowerlimit = 0, upperlimit = 40)) # MED_ACTIVE_COOLING

class BreachType(enum.IntEnum):
    TOO_LOW = 0
    TOO_HIGH = 1
    NORMAL = 2
    BreachType_Count = 3
    
class AlertTarget(enum.IntEnum):
    TO_CONTROLLER = 0
    TO_EMAIL = 1
    AlertTarget_count = 2

CoolingType = {"PASSIVE_COOLING" : 0, "HI_ACTIVE_COOLING" : 1, "MED_ACTIVE_COOLING" : 2 } #look up cooling type


battery = {"CoolingType" : CoolingType["PASSIVE_COOLING"] }
