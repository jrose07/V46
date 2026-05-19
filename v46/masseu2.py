import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties.umath import sqrt

dir = "content/plots/"
dir_tab = "content/tables/"

# --- 1. Naturkonstanten (aus scipy.constants) ---
e = const.e          # Elementarladung [C]
eps0 = const.epsilon_0 # Elektrische Feldkonstante [F/m]
c = const.c          # Lichtgeschwindigkeit [m/s]
m_e = const.m_e      # Elektronenruhemasse [kg] (nur für den relativen Vergleich)

# --- 2. Versuchsspezifische Parameter (HIER ÄNDERN) ---
# Trage hier deine Werte ein!
N_val = 1.2e24       # Dotierungskonzentration [m^-3] (Bsp: 1e18 cm^-3 -> 1e24 m^-3)
n_val = 3.3543          # Brechungsindex (dimensionslos)

# Magnetfeld in Tesla
B_val = 0.411        
B_err = 0.001        
B = ufloat(B_val, B_err)

# Steigung a in µm^-3 eintragen!
a_val = 2.54e-5       # Dein abgelesener Wert
a_err = 0.35e-5       # Dein Fehler
a_ufloat_um3 = ufloat(a_val, a_err)

# NEU: Umrechnung von µm^-3 in die SI-Einheit m^-3 
# (Faktor 10^18)
a = a_ufloat_um3 * 1e18

# --- 3. Berechnung der effektiven Masse nach Formel (11) ---
# m = sqrt( (e^3 * N * B) / (8 * pi^2 * eps0 * c^3 * n * a) )

Zaehler = (e**3) * N_val * B
Nenner = 8 * (np.pi**2) * eps0 * (c**3) * n_val * a

# umath.sqrt kümmert sich automatisch um die Fehlerfortpflanzung!
m_eff_kg = sqrt(Zaehler / Nenner)

# --- 4. Ausgabe ---
# Ausgabe in kg
print(f"Effektive Masse (in kg): {m_eff_kg:.3e}")

# Ausgabe relativ zur Elektronenruhemasse (m*)
m_stern = m_eff_kg / m_e
print(f"Relative effektive Masse (m*): {m_stern:.3f}")