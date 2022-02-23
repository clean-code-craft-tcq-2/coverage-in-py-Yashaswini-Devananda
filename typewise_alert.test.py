import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    for alertTarget in range (typewise_alert.AlertTarget.AlertTarget_count):
        for coolingType in range (len(typewise_alert.CoolingType)):
            typewise_alert.battery["CoolingType"] = coolingType

            temperatureInC = typewise_alert.cooling_type_list[coolingType].lowerlimit-0.1
            typewise_alert.check_and_alert(alertTarget, battery, temperatureInC)

#             temperatureInC = cooling_type_list[coolingType].lowerlimit+0.1
#             typewise_alert.check_and_alert(alertTarget, battery, temperatureInC)

#             temperatureInC = cooling_type_list[coolingType].lowerlimit
#             typewise_alert.check_and_alert(alertTarget, battery, temperatureInC)

if __name__ == '__main__':
  unittest.main()
