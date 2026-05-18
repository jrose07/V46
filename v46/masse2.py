import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dir = "content/plots/"
dir_tab = "content/tables/"

# 1. Datei einlesen (erste Zeile überspringen)
df = pd.read_excel('raw/undotiert.ods', engine='odf', skiprows=1)

# 2. Spalten auslesen, Kommas ersetzen und Fehler in 'NaN' umwandeln
wellenlaenge = pd.to_numeric(df.iloc[:, 1].astype(str).str.replace(',', '.'), errors='coerce')
theta_abs_2 = pd.to_numeric(df.iloc[:, 12].astype(str).str.replace(',', '.'), errors='coerce')

# Filtern! Wir werfen alle Zeilen raus, in denen ein Wert fehlt (NaN)
mask = ~np.isnan(wellenlaenge) & ~np.isnan(theta_abs_2)
w_clean = wellenlaenge[mask]
t_clean = theta_abs_2[mask]

# 3. Lineare Regression mit Gewichten und unskalierter Kovarianzmatrix berechnen
# (Rechnung bleibt in Originalwerten, damit die Prints stimmen!)
params, cov = np.polyfit(w_clean, t_clean, 1, cov=True)
m = params[0] # Steigung
b = params[1] # y-Achsenabschnitt

# Der Fehler ist die Wurzel aus den Diagonaleinträgen der Matrix
m_err = np.sqrt(cov[0, 0])
b_err = np.sqrt(cov[1, 1])

# x-Werte für die durchgehende Linie erzeugen
x_fit = np.linspace(w_clean.min(), w_clean.max(), 100)
y_fit = m * x_fit + b

# Werte inklusive Fehler im Terminal ausgeben (+/-)
print(f"Steigung (m): {m:.2e} +/- {m_err:.2e}")
print(f"y-Achsenabschnitt (b): {b:.2e} +/- {b_err:.2e}")

# --- NEU: Werte NUR für die Optik im Plot auf 10^-4 skalieren ---
t_clean_plot = t_clean * 10**4
y_fit_plot = y_fit * 10**4

# 4. Diagramm plotten
plt.figure(figsize=(8, 5))
plt.plot(w_clean, t_clean_plot, 'go', label='Messwerte (undotiert)')

# Regressionsgerade einzeichnen (rot, gestrichelt)
plt.plot(x_fit, y_fit_plot, 'r--', label='Lineare Regression')

# 5. Achsen passend beschriften (Vorfaktor direkt im Label!)
plt.xlabel(r'Wellenlänge $\lambda$ [$\mu m$]')
plt.ylabel(r'Absoluter Rotationswinkel $\theta_{abs,2}$ [$10^{-4}$ rad/m]')

plt.grid(True)
plt.legend()

# 6. Plot in hoher Auflösung speichern
plt.savefig(dir + 'theta_abs_2_vs_lambda_linreg.png', dpi=300, bbox_inches='tight')