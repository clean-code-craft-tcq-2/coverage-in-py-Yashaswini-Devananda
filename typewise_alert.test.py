import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def generate_expected_message(alertTarget, breachType):
    message = ""
    if alertTarget == AlertTarget.TO_CONTROLLER:
        message = f'{alerter_ref_strings[AlertTarget.TO_CONTROLLER]}, {infer_breach(breachType)}'
    elif breachType!=BreachType.NORMAL and alertTarget == AlertTarget.TO_EMAIL:
        message = f"{alerter_ref_strings[AlertTarget.TO_EMAIL]}{breach_ref_strings[breachType]}"
    return message
  
  def test_infers_breach_as_per_limits(self):
    for alertTarget in range (typewise_alert.AlertTarget.AlertTarget_count):
        for coolingType in range (len(typewise_alert.CoolingType)):
            typewise_alert.battery["CoolingType"] = coolingType

            temperatureInC = typewise_alert.cooling_type_list[coolingType].lowerlimit-0.1
            self.assertTrue(typewise_alert.check_and_alert(alertTarget, typewise_alert.battery, temperatureInC) == generate_expected_message(alertTarget, typewise_alert.BreachType.TOO_LOW))


if __name__ == '__main__':
  unittest.main()
