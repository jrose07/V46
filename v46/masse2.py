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

# Umwandlung in Numpy-Arrays, um das Löschen einfacher zu machen
w_clean = wellenlaenge[mask].to_numpy()
t_clean = theta_abs_2[mask].to_numpy()

# --- NEU: Vorletzten Messwert (Index -2) entfernen ---
w_clean = np.delete(w_clean, -2)
t_clean = np.delete(t_clean, -2)

# 3. Lineare Regression mit Gewichten und unskalierter Kovarianzmatrix berechnen
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

# 4. Diagramm plotten (wieder mit den originalen, unskalierten Werten)
plt.figure(figsize=(8, 5))
plt.plot(w_clean, t_clean, 'go', label='Messwerte (undotiert)')

# Regressionsgerade einzeichnen (rot, gestrichelt)
plt.plot(x_fit, y_fit, 'r--', label='Lineare Regression')

# Wissenschaftliche Notation wieder automatisch von Matplotlib machen lassen
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

# 5. Achsen passend beschriften (ohne manuellen Vorfaktor, dafür mit schönem Index)
plt.xlabel(r'Wellenlänge $\lambda$ [$\mu m$]')
plt.ylabel(r'$\theta_{\mathrm{skaliert}}$ [rad/$\mu$m]')

plt.grid(True)
plt.legend()

# 6. Plot in hoher Auflösung speichern
plt.savefig(dir + 'theta_abs_2_vs_lambda_linreg.png', dpi=300, bbox_inches='tight')