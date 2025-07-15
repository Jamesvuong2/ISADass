import frequencyfinder
import unittest


class TestFrequencyFinder(unittest.TestCase):
    """
    Test class for testing frequencyfinder module functions
    """

    def test_frequency_to_wavelength_valid_input(self):
        """
        Test the frequency_to_wavelength function with valid input
        """
        # Test with a valid frequency
        frequency = 300.0  # THz
        expected_wavelength = 1000.0  # nm
        result = frequencyfinder.frequency_to_wavelength(frequency)
        self.assertAlmostEqual(result, expected_wavelength, places=6,
                               msg=f"Expected {expected_wavelength}, got {result}")

    def test_frequency_to_wavelength_invalid_input(self):
        """
        Test the frequency_to_wavelength function with invalid input
        """
        # Test with an invalid frequency (string)
        with self.assertRaises(TypeError):
            frequencyfinder.frequency_to_wavelength("invalid")
        
        # Test with zero frequency
        with self.assertRaises(ZeroDivisionError):
            frequencyfinder.frequency_to_wavelength(0)

    def test_wavelength_to_frequency_valid_input(self):
        """
        Test the wavelength_to_frequency function with valid input
        """
        wavelength = 1000.0  # nm
        expected_frequency = 300.0  # THz
        result = frequencyfinder.wavelength_to_frequency(wavelength)
        self.assertAlmostEqual(result, expected_frequency, places=6,
                               msg=f"Expected {expected_frequency}, got {result}")

    def test_wavelength_to_frequency_invalid_input(self):
        """
        Test the wavelength_to_frequency function with invalid input
        """
        # Test with an invalid wavelength (string)
        with self.assertRaises(TypeError):
            frequencyfinder.wavelength_to_frequency("invalid")
        
        # Test with zero wavelength
        with self.assertRaises(ZeroDivisionError):
            frequencyfinder.wavelength_to_frequency(0)

    def test_check_frequency_range(self):
        """
        Test the check_frequency_range function
        """
        # Test visible light range
        self.assertEqual(frequencyfinder.check_frequency_range(500), "Visible Light")
        
        # Test UV radiation range
        self.assertEqual(frequencyfinder.check_frequency_range(1000), "UV Radiation")
        
        # Test IR radiation range
        self.assertEqual(frequencyfinder.check_frequency_range(200), "IR Radiation")
        
        # Test out of range
        self.assertEqual(frequencyfinder.check_frequency_range(50000), "Out of Range")

    def test_get_colour_from_frequency(self):
        """
        Test the get_colour_from_frequency function
        """
        # Test with a frequency in violet range
        result = frequencyfinder.get_colour_from_frequency(700)
        self.assertIn("violet", result.lower())
        
        # Test with a frequency outside visible range
        result = frequencyfinder.get_colour_from_frequency(1000)
        self.assertIn("outside", result.lower())

    def test_compare_frequencies(self):
        """
        Test the compare_frequencies function
        """
        # Test with two different frequencies
        result = frequencyfinder.compare_frequencies(500, 600)
        self.assertIsNotNone(result)
        
        # Test with same frequencies
        result = frequencyfinder.compare_frequencies(500, 500)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()

