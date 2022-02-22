import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(49, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(101, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(51, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(99, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(50, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(100, 50, 100) == 'NORMAL')
    
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", -1) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 36) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 0) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 35) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 1) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 34) == 'NORMAL')


if __name__ == '__main__':
  unittest.main()
