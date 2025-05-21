                                                                    ISE Assignment
Student name: James An Vuong
ID: 23180228
Class: ISAD1000
Date/Time: 21/05/2025 2:14 PM

Summary
    This report entails the file; "frequencyfinder.py" which asks the user an input for either a number or a colour and if the input is a number; then looks for whether the number has "nm" or "THz" next to it to determine whether the input is a wavelength or frequency and then calculates either the frequency or wavelength for it and prints it out as well as the associated colour in the spectrum and which radiation range the frequency lies in. If the input is a colour, the program prints the associated frequencies to that colour. 

Modules:

    frequency_to_wavelength(frequency)
    Description: Converts frequency (in THz) to wavelength (in nm).

    wavelength_to_frequency(wavelength)
    Description: Converts wavelength (in nm) to frequency (in THz).

    check_frequency_range(frequency)
    Description: Checks if the frequency is within visible, IR, or UV ranges.

    get_colour_from_frequency(frequency)
    Description: Determines the colour produced by a given frequency.

    get_frequency_range_from_colour(colour_name)
    Description: Determines the frequency produced by a given colour.

    compare_frequencies(freq1, freq2)
    Description: Compares two frequencies to determine if they represent the same colour or different colours.

    userinterface1()
    Description: User interface for figure 1

    userinterface2()
    Description: User interface for figure 2

    main()
    Description: The main starting function that is executed.