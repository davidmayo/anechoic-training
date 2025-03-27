"""
This script demonstrates how to use the SpectrumAnalyzerHP8563E class.
"""

# Import the SpectrumAnalyzerHP8563E class.
# The `msu_anechoic` package is one of the things that you `pip install` in the previous step.
from msu_anechoic.spec_an import SpectrumAnalyzerHP8563E

# Create a spec an object.
# This will look for attached GPIB device(s) and
# make sure that the device is a spectrum analyzer
spec_an = SpectrumAnalyzerHP8563E.find()

# Make sure the spec_an object exists.
if not spec_an:
    # Print an error message
    print("No spectrum analyzer found.")
    
    # Quit the program
    exit()


# There are built in methods on the spec_an class to do common things,
# like setting the center frequency.
# 
# (A "method" is just a function that applies to a specific instance of an object.
# Don't worry if that doesn't mean anything to you.)

# Set the center frequency to 8.4 GHz.
# 
# NOTE: "8_400_000_000" is the same as "8400000000". Python ignores the underscores.
# This is just a way to make the number easier to read.
spec_an.set_center_frequency(8_400_000_000)

# Set the span to 1 MHz.
spec_an.set_span(1_000_000)

# Set the reference level to -10 dBm.
spec_an.set_reference_level(-10)

# Get the center frequency and print it on screen
center_frequency = spec_an.get_center_frequency()
print(f"The center frequency is {center_frequency} Hz.")

# Get the span and print it on screen
span = spec_an.get_span()
print(f"The span is {span} Hz.")

# Get the reference level and print it on screen
reference_level = spec_an.get_reference_level()
print(f"The reference level is {reference_level} dBm.")

# Get the center frequency amplitude and print it on screen
center_frequency_amplitude = spec_an.get_center_frequency_amplitude()
print(f"The center frequency amplitude is {center_frequency_amplitude} dBm at {center_frequency} Hz.")

# Get the maximumum amplitude and print it on screen
# 
# Note that this method is returning TWO values, and we're assigning the first one to `peak_frequency`
# and the second one to `peak_amplitude`. You can do this in Python, but generally not in C/C++.
peak_frequency, peak_amplitude = spec_an.get_peak_frequency_and_amplitude()
print(f"The peak amplitude is {peak_amplitude} dBm at {peak_frequency} Hz.")


# Let's do something more complicated! We'll Get the trace data and graph it.
# This will give us a graph that looks basically like the spectrum analyzer screen.
#
# Get the trace data from the spectrum analyzer.
trace_frequencies, trace_amplitudes = spec_an.get_trace_frequencies_and_amplitudes()

# Import the matplotlib library. This is a very common graphing library in Python.
# This will have been installed when you installed the `msu_anechoic` package.
import matplotlib.pyplot as plt

# Create a figure and axis.
# (This is just dumb matplotlib stuff you have to do.)
fig, ax = plt.subplots()

# Plot the trace data.
ax.plot(trace_frequencies, trace_amplitudes)

# Set the x-axis label.
ax.set_xlabel('Frequency (Hz)')

# Set the y-axis label.
ax.set_ylabel('Amplitude (dBm)')

# Set the title.
ax.set_title('Spectrum Analyzer Trace Data')

# Display the plot.
plt.show()
