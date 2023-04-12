import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

# Constants and parameters
a_s = 9.539  # AU
e = 0.056 #eccentricity
AofP = 279  # degrees
epsilon = 26.73  # degrees
T = 10.23  # hr
R_se = 60400  # km
R_sp = 56400  # km
S_0 = 0.0213  # cal/(cm^2)
T_s = T * 3600  # Convert Saturn day length to seconds
P_y = 29.46 * 365.25  # Period of Saturn's year in Earth days
P_y_s = P_y * 24 * 3600  # Period of Saturn's year in seconds
P_y_sd = P_y_s / T_s  # Period of Saturn's year in Saturn days

rings_data = [
    (120000, 137000, 0.5),  # Ring A
    (90000, 116000, 1.0),   # Ring B
    (72000, 89000, 0.1),    # Ring C
]

AU_to_km = 1.496e+8  # km

def distance_from_sun(a_s, e, omega):
    return a_s * (1 - e ** 2) / (1 + e * np.cos(np.radians(omega))) * AU_to_km

r = distance_from_sun(a_s, e, AofP)  # km
delta_rad = np.linspace(-np.pi / 2, np.pi / 2, 100)  # rad
h = np.linspace(0, 2 * np.pi, 100)  # rad

def cot(x):
    return 1 / np.tan(x)

def solar_declination(epsilon, lambda_):
    return np.arcsin(np.sin(np.radians(epsilon)) * np.sin(np.radians(lambda_)))

def insolation(h, phi_rad, delta_rad, r, gamma, tau_values):
    cos_Z = np.cos(gamma) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h)) + \
            np.sin(gamma) * (np.tan(phi_rad) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h)) - np.sin(delta_rad) * np.cos(phi_rad))
    cos_Z = np.maximum(cos_Z, 0)
    return S_0 * (a_s * AU_to_km / r)**2 * cos_Z * np.exp(-tau_values) * T_s

def compute_tau(h, delta_rad, rings_data, R_se, R_sp, phi):
    phi_rad = np.radians(phi)
    gamma = np.arctan(((R_se / R_sp)**2) * np.tan(np.radians(phi))) - np.radians(phi)
    cos_Z = np.cos(gamma) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h)) + \
            np.sin(gamma) * (np.tan(phi_rad) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h)) - np.sin(delta_rad) * np.cos(phi_rad))

    plus_x = R_se * (np.tan(phi_rad) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h)) - np.sin(delta_rad) * np.cos(phi_rad)) + R_sp
    minus_x = R_se * (np.tan(phi_rad) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h)) - np.sin(delta_rad) * np.cos(phi_rad)) - R_sp

    plus_z = R_se * np.cos(gamma) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h))
    minus_z = -R_se * np.cos(gamma) * (np.sin(phi_rad) * np.sin(delta_rad) + np.cos(phi_rad) * np.cos(delta_rad) * np.cos(h))

    x_values = np.where(cos_Z >= 0, plus_x, minus_x)
    z_values = np.where(cos_Z >= 0, plus_z, minus_z)

    tau_values = np.zeros_like(x_values)
    for x_start, x_end, tau in rings_data:
        mask = (x_start <= x_values) & (x_values <= x_end) & (z_values >= 0)
        tau_values[mask] += tau

    return tau_values

def true_anomaly(E, e):
    return 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(E / 2))

def mean_anomaly(t, P_y_s):
    return 2 * np.pi * t / P_y_s

def kepler_eq(E, M, e):
    return E - e * np.sin(E) - M

phi_values = np.linspace(0, 90, 100)

mean_annual_daily_insolation = np.zeros(len(phi_values))
num_time_steps = 100

for i, phi in enumerate(phi_values):
    total_insolation = 0
    for t in np.linspace(0, P_y_s, num_time_steps):  # Integrate over Saturn's year
        M = mean_anomaly(t, P_y_s)
        E = fsolve(kepler_eq, M, args=(M, e))[0]
        nu = true_anomaly(E, e)
        r = distance_from_sun(a_s, e, nu)  # r is in km
        lambda_ = nu + AofP
        delta = solar_declination(epsilon, lambda_)
        tau_values = compute_tau(h, delta, rings_data, R_se, R_sp, phi)
        total_insolation += np.trapz(insolation(h, np.radians(phi), delta, r, np.arctan((R_se / R_sp)**2 * np.tan(np.radians(phi)) - np.radians(phi)), tau_values), h) / num_time_steps
    
    mean_annual_daily_insolation[i] = total_insolation / P_y_sd

plt.plot(phi_values, mean_annual_daily_insolation)
plt.xlabel('Latitude (degrees)')
plt.ylabel('Mean Annual Daily Insolation (cal/cm^2/planetary day)')
plt.show()

