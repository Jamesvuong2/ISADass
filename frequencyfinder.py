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

def get_frequency_range_from_colour(colour_name):
    """
    Determines the frequency produced by a given colour.
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

    colour_name = colour_name.lower()
    if colour_name in colours:
        lower, upper = colours[colour_name]
        return f"The frequency range for {colour_name} is {lower} THz to {upper} THz."
    else:
        return f"'{colour_name}' is not a valid colour in the visible spectrum."

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

def userinterface1():
    """
    Entry point of the application.
    """

    userinput = input(":")

    # Check if userinput contains "THz" or "nm"
    if "THz" in userinput:
        try:
            frequency = float(userinput.replace("THz", "").strip())
            wavelength = frequency_to_wavelength(frequency)
            print(f"Frequency {frequency} THz corresponds to wavelength {wavelength:.2f} nm.")
            range_check = check_frequency_range(frequency)
            print(f"Frequency {frequency} THz is in the range: {range_check}.")
            colour = get_colour_from_frequency(frequency)
            print(f"Frequency {frequency} THz produces the colour: {colour}.")
        except ValueError:
            print("Invalid frequency input. Please enter a valid number followed by 'THz'.")

    elif "nm" in userinput:
        try:
            wavelength = float(userinput.replace("nm", "").strip())
            frequency = wavelength_to_frequency(wavelength)
            print(f"Wavelength {wavelength} nm corresponds to frequency {frequency:.2f} THz.")
            range_check = check_frequency_range(frequency)
            print(f"Wavelength {wavelength} nm corresponds to a frequency in the range: {range_check}.")
            colour = get_colour_from_frequency(frequency)
            print(f"Wavelength {wavelength} nm produces the colour: {colour}.")
        except ValueError:
            print("Invalid wavelength input. Please enter a valid number followed by 'nm'.")

    else:
        # Assume the input is a colour name
        try:
            colour_range = get_frequency_range_from_colour(userinput)
            print(colour_range)
        except ValueError:
            print("Invalid colour input. Please enter a valid colour name.")

def userinterface2():
    """
    User interface for figure 2
    """
    colours = {
        "violet": ["Amethyst", "B", "Bravery"],
        "blue": ["Opal", "A", "Clam"],
        "cyan": ["Turquoise", "G", "Clam"],
        "green": ["Emerald", "F", "Peaceful"],
        "yellow": ["Topaz", "E", "Happy"],
        "orange": ["Moonstone", "D", "Happy"],
        "red": ["Garnet", "C", "Confidence"],
    }

    userinput = input("Enter a colour name (e.g., red, blue, green): ").lower()

    if userinput in colours:
        stone, note, emotion = colours[userinput]
        print(f"The stone associated with {userinput} is {stone}.")
        print(f"The musical note associated with {userinput} is {note}.")
        print(f"The emotion associated with {userinput} is {emotion}.")
    else:
        print(f"'{userinput}' is not a valid colour in the list.")

def main():
    """
    Entry point of the application.
    """

    print("Enter a frequency in THz, a wavelength in nm, or a colour:")
    userinterface1()
    userinterface2()

if __name__ == "__main__":
    main()