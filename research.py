import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the Henderson-Hasselbalch equation
def henderson_hasselbalch(pH, pKa):
    return 1 / (1 + 10**(pH - pKa))

# Provided titration data (observed protonated fractions with pH values)
pH_values = np.array([3.6, 3.7, 3.8, 4.1, 4.4, 4.5, 5.5])
protonated_fraction = np.array([0.80, 0.70, 0.60, 0.50, 0.30, 0.20, 0.00])

# Fit the data to the Henderson-Hasselbalch equation using nonlinear regression to determine the pKa value
initial_guess = [4.0]  # Initial guess for pKa
params, covariance = curve_fit(henderson_hasselbalch, pH_values, protonated_fraction, absolute_sigma=True, p0=initial_guess)
pKa_fit = params[0]
pKa_error = np.sqrt(np.diag(covariance))[0]

# Calculate fitted curve
pH_smooth = np.linspace(3.5, 5.5, 500)
fitted_curve = henderson_hasselbalch(pH_smooth, pKa_fit)

# Plot the data and the fitted curve
plt.figure(figsize=(5, 4))
plt.errorbar(pH_values, protonated_fraction, fmt='o', color='blue', label='Observed Data')
plt.plot(pH_smooth, fitted_curve, color='green', label='Fitted Curve')

# Add the equation and pKa text
plt.text(4.0, 0.8, r"$f(pH) = \frac{1}{1 + 10^{pH - pK_a}}$", fontsize=12, color='green')
plt.text(4.0, 0.7, f"$pK_a = {pKa_fit:.2f} \pm {pKa_error:.2f}$", fontsize=12, color='green')

# Label axes
plt.xlabel('pH', fontsize=10)
plt.ylabel('Protonated Fraction, f', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(0, 1)
plt.xlim(3.5, 5.5)

# Add legend
plt.legend(fontsize=10, loc='upper right')

# Adjust layout
plt.tight_layout()
plt.grid()
plt.show()

# Print the fitted parameters with errors
print(f"Fitted pKa: {pKa_fit:.2f} ± {pKa_error:.2f}")

