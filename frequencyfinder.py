# Created 20/05/2025
# Author: James Vuong
# ID: 23180228

def frequency_to_wavelength(frequency):
    """
    Converts frequency (in THz) to wavelength (in nm).
    """
    c = 3 * 10**8  # Speed of light in m/s
    wavelength = c / (frequency * 10**12)  # Convert THz to Hz
    return wavelength * 10**9  # Convert meters to nanometers


def wavelength_to_frequency(wavelength):
    """
    Converts wavelength (in nm) to frequency (in THz).
    """
    c = 3 * 10**8  # Speed of light (m/s)
    frequency = c / (wavelength * 10**-9)  # Convert nm to meters
    return frequency / 10**12  # Convert Hz to THz


def check_frequency_range(frequency):
    """
    Checks if the frequency is within visible, IR, or UV ranges.
    """
    visible_light_range = (400, 790)  # in THz
    uv_radiation_frequency_range = (791, 30000)  # in THz
    ir_radiation_frequency_range = (1, 399)  # in THz

    if visible_light_range[0] <= frequency <= visible_light_range[1]:
        return "Visible Light"
    elif uv_radiation_frequency_range[0] <= frequency <= uv_radiation_frequency_range[1]:
        return "UV Radiation"
    elif ir_radiation_frequency_range[0] <= frequency <= ir_radiation_frequency_range[1]:
        return "IR Radiation"
    else:
        return "Out of Range"


def get_colour_from_frequency(frequency):
    """
    Determines the colour produced by a given frequency.
    """
    colours = {
        "violet": (670, 790),
        "blue": (620, 669),
        "cyan": (600, 619),
        "green": (530, 599),
        "yellow": (510, 529),
        "orange": (480, 509),
        "red": (400, 479),
    }

    # Checks the bounds of the frequency
    for colour, (lower, upper) in colours.items():
        if lower <= frequency <= upper:
            return colour

    if frequency > 790:
        return "Frequency is higher than violet."
    elif frequency < 400:
        return "Frequency is lower than red."
    else:
        return "Out of Range"


def compare_frequencies(freq1, freq2):
    """
    Compares two frequencies to determine if they represent the same colour or different colours.
    """
    colour1 = get_colour_from_frequency(freq1)
    colour2 = get_colour_from_frequency(freq2)

    if "higher than violet" in colour1 or "lower than red" in colour1:
        return f"Frequency 1 ({freq1} THz) is not in the visible range: {colour1}"
    if "higher than violet" in colour2 or "lower than red" in colour2:
        return f"Frequency 2 ({freq2} THz) is not in the visible range: {colour2}"

    if colour1 == colour2:
        return f"Both frequencies represent the same colour: {colour1}."
    else:
        return f"Frequency 1 represents {colour1}, and Frequency 2 represents {colour2}."


def main():
    """
    Entry point of the application.
    """
    # Example usage
    frequency = 500  # Example frequency in THz
    wavelength = frequency_to_wavelength(frequency)
    print(f"Frequency {frequency} THz corresponds to wavelength {wavelength:.2f} nm.")

    wavelength = 600  # Example wavelength in nm
    frequency = wavelength_to_frequency(wavelength)
    print(f"Wavelength {wavelength} nm corresponds to frequency {frequency:.2f} THz.")

    frequency = 500  # Example frequency in THz
    range_check = check_frequency_range(frequency)
    print(f"Frequency {frequency} THz is in the range: {range_check}.")

    frequency = 450  # Example frequency in THz
    colour = get_colour_from_frequency(frequency)
    print(f"Frequency {frequency} THz produces the colour: {colour}.")

    freq1, freq2 = 450, 700  # Example frequencies in THz
    comparison = compare_frequencies(freq1, freq2)
    print(comparison)



if __name__ == "__main__":
    main()