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
    Exports: colour (string)
    Description: Determines the colour produced by a given frequency and returns the colour.

    get_frequency_range_from_colour
    Imports: colour_name (string)
    Exports: lower (int), upper (int), colour_name (string)
    Description: Determines the frequency produced by a given colour and returns the lower and upper bounds of said colour.

    compare_frequencies
    Imports: freq1, freq2
    Exports: colour1 (string), colour2 (string)
    Description: Compares two frequencies to determine if they represent the same colour or different colours and returns a message saying either that they represent the same colour or different colours.

    userinterface1
    Imports: userinput (string)
    Exports: 
    Description: User interface for figure 1. Asks the user for an input of either the name of a colour, or a frequency or wavelength with the words "nm" or "THz" to annotate as to which value the user is referring to. If neither "nm" nor "THz" is present, then the program assumes a colour and will produce a message if the input is an invalid colour, otherwise it will give the associated frequency with the colour. In the case that the words "THz" is present in the user's input; the program will execute frequency_to_wavelength to calculate the wavelength, check_frequency_range to find whether the frequency is within the visible light range, the IR range or the UV range, and get_colour_from_frequency to find the associated colour with the frequency. However, in the case that the words "nm" is present in the user's input; the program will execute wavelength_to_frequency to calculate the frequency, check_frequency_range to find whether the frequency that was calculated is within the visible light range, the IR range or the UV range, and get_colour_from_frequency to find the associated colour with the calculated frequency. When 2 frequencies are given, it returns the colours associated with them and a unique message pops up if both represent the same colour.

    userinterface2
    Imports: userinput (string)
    Exports: 
    Description: User interface for figure 2. Asks the user for an input of the name of a colour and when given a colour that matches one found in the program's list, it will print out the; stone associated with the colour, the musical note associated with the colour and the emotion associated with the colour.

    main
    Imports:
    Exports:
    Description: The main module.

Design Decisions
    The program was separated into functions and modules to better organise the structure. This is a good example a modularity as it provides high cohesion from having small chunks that contribute to a larger bloc of code and low coupling as only 2 modules rely on other modules. Each module only provides the information that the module is mean't for and each module shares functionality within each other. This allows for easy mistake fixing as any mistakes only needs to be addressed within the module and not overall.

Review Checklist:
    1. Are the calulations for frequencies to wavelength and wavelength to frequencies accurate enough?  | Yes
    2. Does the check_frequency_range module correctly finds the radiation range for the imported value?    | Yes
    3. Does the get_colour_from_frequency module export a colour that corresponds to the ranges in the colours.items list?  | Yes
    4. Does the get_frequency_range_from_colour module export 2 frequencies that are the upper and lower bounds of the imported colour?     | Yes
    5. Can the program accept 2 frequencies and process them into 2 separate colours?   | Yes
    6. Does the second figure part give the associated stone, musical note and emotion with the imported colour?    | Yes
    7. Does the program check for value errors in the userinput?    | Yes
    8. Is the code structure organised into function/module blocks?     | Yes
    9. Have the majority of the modules been commented properly?     | Yes
    10. Are there no typos for the emotions for the colours?    | No    | Reason: Figure 2 which this was referenced off of contained the typo and thus doesn't count as a mistake on this end.

Black Box Test Cases:
    frequency_to_wavelength
    Imports: frequency
    Exports: wavelength
    Description: Converts frequency (in THz) to wavelength (in nm) and returns the wavelength.
    ________________________________________________________________________________________________
    |                 Category                   |     Test Data       |       Expected Result     |
    |wavelength = c / (frequency * 10**12)       |frequency = 500      |      600                  |
    |                                            |                     |                           |
    |____________________________________________|_____________________|___________________________|

    check_frequency_range
    Imports: frequency
    Exports: radiation_range (string)
    Description: Checks if the frequency is within visible, IR, or UV ranges. If the frequency is between 400 and 790, then "Visible Light" is returned. If the frequency is between 791 and 30000, then "UV Radiation" is returned. If the frequency is between 1 and 399, then "IR Radiation" is returned.
    ________________________________________________________________
    |      Boundary        |  Test Data     |   Expected Result    |
    | Between 400 and 790  | frequency = 500| "Visible Light"      |
    | Between 791 and 30000| frequency = 800| "UV Radiation"       |
    | Between 1 and 399    | frequency = 200| "IR Radiation"       |
    | Between 1 and 399    | frequency = 0  | "Out of Range"       |
    |______________________|________________|______________________|

    get_colour_from_frequency
    Imports: frequency
    Exports: colour (string)
    Description: Determines the colour produced by a given frequency and returns the colour.
    ____________________________________________________________________________
    |    Category                      |  Test Data     |   Expected Result    |
    | frequency is within colour range | frequency = 300| Invalid              |
    | frequency is within colour range | frequency = 500| Orange               |
    | frequency is within colour range | frequency = 700| Violet               |
    |__________________________________|________________|______________________|

    get_frequency_range_from_colour
    Imports: colour_name (string)
    Exports: lower (int), upper (int), colour_name (string)
    Description: Determines the frequency produced by a given colour and returns the lower and upper bounds of said colour.
    ___________________________________________________________________________
    |    Category              |  Test Data            |   Expected Result    |
    | colour_name is in colours|colour_name == "violet"|670, 790              |
    | colour_name is in colours|colour_name == "garlic"|Invalid               |
    | colour_name is in colours|colour_name == "red"   |400, 479              |
    |__________________________|_______________________|______________________|

White Box Test Cases
    check_frequency_range
    Imports: frequency
    Exports: radiation_range (string)
    Description: Checks if the frequency is within visible, IR, or UV ranges. If the frequency is between 400 and 790, then "Visible Light" is returned. If the frequency is between 791 and 30000, then "UV Radiation" is returned. If the frequency is between 1 and 399, then "IR Radiation" is returned.
    _________________________________________________________________________
    |      Path              |  Test Data            |   Expected Result    |
    | Enter the if part      | frequency = 500       | "Visible Light"      |
    | Enter the elif part    | frequency = 800       | "UV Radiation"       |
    | Enter the 2nd elif part| frequency = 200       | "IR Radiation"       |
    | Enter the else part    | frequency = 23180228  | "Out of Range"       |
    |________________________|_______________________|______________________|

    get_colour_from_frequency
    Imports: frequency
    Exports: colour (string)
    Description: Determines the colour produced by a given frequency and returns the colour.
    ____________________________________________________________________________
    |           Path                   |  Test Data     |   Expected Result    |
    | Enter the if part                | frequency = 300| Invalid              |
    | Enter the if part                | frequency = 500| Orange               |
    | Enter the if part                | frequency = 700| Violet               |
    |__________________________________|________________|______________________|

    get_frequency_range_from_colour
    Imports: colour_name (string)
    Exports: lower (int), upper (int), colour_name (string)
    Description: Determines the frequency produced by a given colour and returns the lower and upper bounds of said colour.
    ___________________________________________________________________________
    |    Path                  |  Test Data            |   Expected Result    |
    | Enter the if part        |colour_name == "violet"|670, 790              |
    | Enter the else part      |colour_name == "garlic"|Invalid               |
    |__________________________|_______________________|______________________|

    compare_frequencies
    Imports: freq1, freq2
    Exports: colour1 (string), colour2 (string)
    Description: Compares two frequencies to determine if they represent the same colour or different colours and returns a message saying either that they represent the same colour or different colours.
    ______________________________________________________________________________________________________________________
    |        Path              |  Test Data             |                           Expected Result                      |
    | Enter the 3rd if part    |freq1 = 400, freq2 = 400|"Both frequencies represent the same colour: red."              |
    | Enter the else part      |freq1 = 400, freq2 = 700|"Frequency 1 represents red, and Frequency 2 represents violet."|
    |__________________________|________________________|________________________________________________________________|

Summary Table:
    __________________________________________________________________________________________________________________________________________________
    |________________________________|    Design of test cases                                           |   test code implementation and execution  |
    |   Module name                  |  BB (EP) |BB (BVA)|WB      |    Data Types   |Form of input/output|    EP  |   BVA    |    White-Box          |
    |frequency_to_wavelength         |done      |not done|not done|any              |frequency           |done    |done      |done                   |
    |check_frequency_range           |not done  |done    |not done|any, string      |frequency           |done    |done      |done                   |
    |get_colour_from_frequency       |done      |not done|not done|any, string      |frequency           |done    |done      |done                   |
    |get_frequency_range_from_colour |done      |not done|not done|string, integer  |colour              |done    |done      |done                   |
    |compare_frequencies             |not done  |not done|done    |any, string      |frequency, frequency|done    |done      |done                   |
    |________________________________|__________|________|________|_________________|____________________|________|__________|_______________________|