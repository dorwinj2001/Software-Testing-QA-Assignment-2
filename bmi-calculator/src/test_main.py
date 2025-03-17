import unittest
from main import calculate_bmi, bmi_ranges

class TestBMICalculator(unittest.TestCase):

    def test_calculate_bmi(self):
        # Boundary testing for calculate_bmi
        self.assertAlmostEqual(calculate_bmi(100, 60), 19.53, places=2)  # Typical values
        self.assertAlmostEqual(calculate_bmi(200, 72), 27.12, places=2)  # Typical values
        self.assertAlmostEqual(calculate_bmi(50, 48), 15.26, places=2)   # Minimum values
        self.assertAlmostEqual(calculate_bmi(300, 84), 29.89, places=2)  # Maximum values

    def test_bmi_ranges(self):
        # Boundary testing for bmi_ranges
        self.assertEqual(bmi_ranges(18.4), "Underweight")  # Just below normal weight
        self.assertEqual(bmi_ranges(18.5), "Normal weight")  # Boundary of normal weight
        self.assertEqual(bmi_ranges(24.9), "Normal weight")  # Boundary of normal weight
        self.assertEqual(bmi_ranges(25.0), "Overweight")  # Boundary of overweight
        self.assertEqual(bmi_ranges(29.9), "Overweight")  # Boundary of overweight
        self.assertEqual(bmi_ranges(30.0), "Obese")  # Boundary of obese

if __name__ == '__main__':
    unittest.main()