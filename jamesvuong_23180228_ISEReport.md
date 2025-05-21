                                                                    ISE Assignment
Student name: James An Vuong
ID: 23180228
Class: ISAD1000
Date/Time: 21/05/2025 2:14 PM

Summary
    This report entails the file; "frequencyfinder.py" which asks the user an input for either a number or a colour and if the input is a number; then looks for whether the number has "nm" or "THz" next to it to determine whether the input is a wavelength or frequency and then calculates either the frequency or wavelength for it and prints it out as well as the associated colour in the spectrum and which radiation range the frequency lies in. If the input is a colour, the program prints the associated frequencies to that colour. 

Modules:

    frequency_to_wavelength
    Imports: frequency
    Exports: wavelength
    Description: Converts frequency (in THz) to wavelength (in nm) and returns the wavelength.

    wavelength_to_frequency
    Imports: wavelength
    Exports: frequency
    Description: Converts wavelength (in nm) to frequency (in THz) and returns the frequency.

    check_frequency_range
    Imports: frequency
    Exports: radiation_range (string)
    Description: Checks if the frequency is within visible, IR, or UV ranges. If the frequency is between 400 and 790, then "Visible Light" is returned. If the frequency is between 791 and 30000, then "UV Radiation" is returned. If the frequency is between 1 and 399, then "IR Radiation" is returned.

    get_colour_from_frequency
    Imports: frequency
    Exports: colour (string), lower (string), upper(string)
    Description: Determines the colour produced by a given frequency and returns the upper and lower bounds of said colour. 

    get_frequency_range_from_colour
    Imports: colour_name (string)
    Exports: lower (int), upper (int), colour_name (string)
    Description: Determines the frequency produced by a given colour.

    compare_frequencies
    Imports: freq1, freq2
    Exports: colour1 (string), colour2 (string)
    Description: Compares two frequencies to determine if they represent the same colour or different colours and returns a message saying either that they represent the same colour or different colours.

    userinterface1
    Imports: userinput (string)
    Exports: 
    Description: User interface for figure 1. Asks the user for an input of either the name of a colour, or a frequency or wavelength with the words "nm" or "THz" to annotate as to which value the user is referring to. If neither "nm" nor "THz" is present, then the program assumes a colour and will produce a message if the input is an invalid colour, otherwise it will give the associated frequency with the colour. In the case that the words "THz" is present in the user's input; the program will execute frequency_to_wavelength to calculate the wavelength, check_frequency_range to find whether the frequency is within the visible light range, the IR range or the UV range, and get_colour_from_frequency to find the associated colour with the frequency. However, in the case that the words "nm" is present in the user's input; the program will execute wavelength_to_frequency to calculate the frequency, check_frequency_range to find whether the frequency that was calculated is within the visible light range, the IR range or the UV range, and get_colour_from_frequency to find the associated colour with the calculated frequency.

    userinterface2
    Imports: userinput (string)
    Exports: 
    Description: User interface for figure 2. Asks the user for an input of the name of a colour and when given a colour that matches one found in the program's list, it will print out the; stone associated with the colour, the musical note associated with the colour and the emotion associated with the colour.

    main
    Imports:
    Exports:
    Description: The main module.