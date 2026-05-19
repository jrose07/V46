import pandas as pd
import matplotlib.pyplot as plt

dir = "content/plots/"
dir_tab = "content/tables/"

# Datei einlesen (erste Zeile / Header wird übersprungen)
df = pd.read_excel('raw/undotiert.ods', engine='odf', skiprows=1)

# NEU: Nur Zeilen 2 bis 10 (was im DataFrame Index 0 bis 8 entspricht) auslesen
wellenlaenge = df.iloc[0:9, 1].astype(str).str.replace(',', '.').astype(float)
theta_skaliert = df.iloc[0:9, 6].astype(str).str.replace(',', '.').astype(float)

# Wellenlänge quadrieren
lambda_sq = wellenlaenge ** 2

# Plot erstellen
plt.figure(figsize=(8, 5))
plt.plot(lambda_sq, theta_skaliert, 'bo', label='Messwerte')

# Wissenschaftliche Notation für die y-Achse aktivieren
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

plt.xlabel(r'$\lambda^2$ [$\mu m^2$]')
plt.ylabel(r'$\theta_{\mathrm{skaliert}}$ [rad/$\mu$m]')
plt.grid(True)
plt.legend()

# Speichern
plt.savefig(dir + 'theta_vs_lambda_undotiert.png', dpi=300, bbox_inches='tight')