import frequencyfinder
import unittest

def test_frequency_to_wavelength():
    """
    Test the frequency_to_wavelength function
    """
    # Test with a valid frequency
    frequency = 300.0  # THz
    expected_wavelength = 1000.0  # nm
    result = frequencyfinder.frequency_to_wavelength(frequency)
    assert abs(result - expected_wavelength) < 1e-6, f"Expected {expected_wavelength}, got {result}"
    # Test with an invalid frequency
    try:
        frequencyfinder.frequency_to_wavelength("invalid")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid frequency input"
    userinput = input(":")

