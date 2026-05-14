import pandas as pd
import matplotlib.pyplot as plt

# Datei einlesen
df = pd.read_excel('raw/n-dotiert_1.ods', engine='odf', skiprows=1)

# Spalten auslesen
wellenlaenge = df.iloc[:, 1].astype(str).str.replace(',', '.').astype(float)
theta_skaliert = df.iloc[:, 6].astype(str).str.replace(',', '.').astype(float)

# Wellenlänge quadrieren
lambda_sq = wellenlaenge ** 2

# Plot erstellen
plt.figure(figsize=(8, 5))
plt.plot(lambda_sq, theta_skaliert, 'bo', label='Messwerte')

# NEU: Wissenschaftliche Notation für die y-Achse aktivieren
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

plt.xlabel(r'Wellenlänge $\lambda^2$ [$\mu m^2$]')
plt.ylabel(r'Normierter Rotationswinkel $\theta_{skaliert}$ [rad/m]')
plt.title(r'Faraday-Rotation: $\theta_{skaliert}$ gegen $\lambda^2$ (n-dotiert 1)')

plt.grid(True)
plt.legend()

# Speichern
plt.savefig('theta_vs_lambda_n1.png', dpi=300, bbox_inches='tight')