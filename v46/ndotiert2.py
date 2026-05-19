import pandas as pd
import matplotlib.pyplot as plt

dir = "content/plots/"
dir_tab = "content/tables/"

# Datei einlesen
df = pd.read_excel('raw/n-dotiert_2.ods', engine='odf', skiprows=1)

# Spalten auslesen
wellenlaenge = df.iloc[:, 1].astype(str).str.replace(',', '.').astype(float)
theta_skaliert = df.iloc[:, 6].astype(str).str.replace(',', '.').astype(float)

# Wellenlänge quadrieren
lambda_sq = wellenlaenge ** 2

# Plot erstellen (wieder mit den originalen, unskalierten Werten)
plt.figure(figsize=(8, 5))
plt.plot(lambda_sq, theta_skaliert, 'bo', label='Messwerte')

# Wissenschaftliche Notation wieder automatisch von Matplotlib machen lassen
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

plt.xlabel(r'Wellenlänge $\lambda^2$ [$\mu m^2$]')
# Die typografisch saubere Formatierung direkt beibehalten
plt.ylabel(r'$\theta_{\mathrm{skaliert}}$ [rad/$\mu$m]')

plt.grid(True)
plt.legend()

# Speichern
plt.savefig(dir + 'theta_vs_lambda_n2.png', dpi=300, bbox_inches='tight')