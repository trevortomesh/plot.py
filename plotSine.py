from numpy import *
import matplotlib.pyplot as plot

# Get x values of the sine wave

x = arange(0, 100, 0.1)

# Amplitude of the sine wave is sine of a variable like time
y = sin(x)+sin(x/3)+sin(x/5)

# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(x, y)

# Give a title for the sine wave plot
plot.title("Custom Plot")

# Give x axis label for the sine wave plot
plot.xlabel('Time')

# Give y axis label for the sine wave plot
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()

# Display the sine wave
plot.show()
