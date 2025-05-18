import math

def calculate_max_voltage_spike(V_c0, V_d, I_0, L, C):
    """
    Calculate the maximum voltage spike across the inductor considering the diode voltage drop.

    Parameters:
    V_c0 (float): Initial voltage of the capacitor in volts.
    V_d (float): Diode voltage drop in volts.
    I_0 (float): Initial current through the inductor in amperes.
    L (float): Inductance in henries.
    C (float): Capacitance in farads.

    Returns:
    float: Maximum voltage spike in volts.
    """
    term1 = (V_c0 + V_d) ** 2
    term2 = (I_0 ** 2 * L) / C
    V_spike_max = math.sqrt(term1 + term2)
    return V_spike_max

# Sample values
V_c0 = 0.0  # Initial capacitor voltage in volts
V_d = 0.7   # Diode voltage drop in volts (typical for silicon diode)
I_0 = 1.0   # Initial inductor current in amperes
L = 0.001   # Inductance in henries (1 mH)
C = 1e-6    # Capacitance in farads (1 μF)

# Calculate the maximum voltage spike
V_spike_max = calculate_max_voltage_spike(V_c0, V_d, I_0, L, C)

# Print the result
print(f"The maximum voltage spike is {V_spike_max:.2f} V")
