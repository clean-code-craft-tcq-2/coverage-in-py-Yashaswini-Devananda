import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
  def generate_controller_message(self,alertTarget, breachType):
    message = f'{typewise_alert.alerter_ref_strings[typewise_alert.AlertTarget.TO_CONTROLLER]}, {typewise_alert.infer_breach(breachType)}'
    return message
    
  def generate_email_message(self,alertTarget, breachType):
    message = ""
    if breachType!=typewise_alert.BreachType.NORMAL:
      recepient = "a.b@c.com"
      message = (f'To: {recepient}\n')
      message += f"{typewise_alert.alerter_ref_strings[typewise_alert.AlertTarget.TO_EMAIL]}{typewise_alert.breach_ref_strings[breachType]}"
    return message
  
  def generate_expected_message(self,alertTarget, breachType):
    message = ""
    if alertTarget == typewise_alert.AlertTarget.TO_CONTROLLER:
        message = self.generate_controller_message(alertTarget, breachType)
        return message
    if alertTarget == typewise_alert.AlertTarget.TO_EMAIL:
        message = self.generate_email_message(alertTarget, breachType)
    return message
  
#   def test_condition(alertTarget, battery):
#     temperatureInC = typewise_alert.cooling_type_list[coolingType].lowerlimit-0.1
#     actual_message = typewise_alert.check_and_alert(alertTarget, battery, temperatureInC)
#     self.assertTrue(self.generate_expected_message(alertTarget, typewise_alert.BreachType.TOO_LOW)==actual_message)

#   def run_test_cases(self, alertTarget, coolingType, battery):
#     test_cases = [
#               {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].lowerlimit-0.1, "BreachType": typewise_alert.BreachType.TOO_LOW},
#               {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].lowerlimit+0.1, "BreachType": typewise_alert.BreachType.NORMAL},
#               {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].lowerlimit, "BreachType": typewise_alert.BreachType.NORMAL},
#               {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].upperlimit-0.1, "BreachType": typewise_alert.BreachType.NORMAL},
#               {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].upperlimit+0.1, "BreachType": typewise_alert.BreachType.TOO_HIGH},
#               {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].upperlimit, "BreachType": typewise_alert.BreachType.NORMAL},
#              ]
#     for test_case in test_cases:
#       actual_message = typewise_alert.check_and_alert(alertTarget, battery, test_case["temperatureInC"])
#       self.assertTrue(self.generate_expected_message(alertTarget, test_case["BreachType"]) == actual_message)
#       print (actual_message)
#       print (self.generate_expected_message(alertTarget, test_case["BreachType"]))
#       print ("$")
    
  def test_infers_breach_as_per_limits(self):
    for alertTarget in range (typewise_alert.AlertTarget.AlertTarget_count):
        for coolingType in range (len(typewise_alert.CoolingType)):
            typewise_alert.battery["CoolingType"] = coolingType
#             self.run_test_cases(alertTarget, coolingType, typewise_alert.battery)                            
            test_cases = [
              {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].lowerlimit-0.1, "BreachType": typewise_alert.BreachType.TOO_LOW},
              {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].lowerlimit+0.1, "BreachType": typewise_alert.BreachType.NORMAL},
              {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].lowerlimit, "BreachType": typewise_alert.BreachType.NORMAL},
              {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].upperlimit-0.1, "BreachType": typewise_alert.BreachType.NORMAL},
              {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].upperlimit+0.1, "BreachType": typewise_alert.BreachType.TOO_HIGH},
              {"temperatureInC" : typewise_alert.cooling_type_list[coolingType].upperlimit, "BreachType": typewise_alert.BreachType.NORMAL},
             ]
            for test_case in test_cases:
              actual_message = typewise_alert.check_and_alert(alertTarget, battery, test_case["temperatureInC"])
              self.assertTrue(self.generate_expected_message(alertTarget, test_case["BreachType"]) == actual_message)
              print (actual_message)
              print (self.generate_expected_message(alertTarget, test_case["BreachType"]))
              print ("$")
                   
            
#             print (typewise_alert.check_and_alert(alertTarget, typewise_alert.battery, temperatureInC))
#             print (self.generate_expected_message(alertTarget, typewise_alert.BreachType.TOO_LOW))


if __name__ == '__main__':
  unittest.main()
  
  
  
