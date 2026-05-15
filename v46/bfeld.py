
import pandas as pd
import matplotlib.pyplot as plt

dir = "content/plots/"
dir_tab = "content/tables/"

# Datei einlesen
df = pd.read_excel('raw/bfeld.ods', engine='odf')

B_werte = pd.to_numeric(df['B[mT]'])
z_werte = pd.to_numeric(df['x[mm]'])

# Maximum ermitteln
max_idx = B_werte.idxmax()
B_max = B_werte[max_idx]
z_max = z_werte[max_idx]

# Plot erstellen
plt.figure(figsize=(10, 6))

# NEU: Nur Messpunkte zeichnen ('bo' statt 'bo-')
plt.plot(z_werte, B_werte, 'bx', label='Messwerte')

# NEU: Nur Linien durch das Maximum ziehen (vertikal und horizontal)
plt.axvline(z_max, color='r', linestyle='--', label=f'z_max = {z_max} mm')
plt.axhline(B_max, color='r', linestyle=':', alpha=0.7, label=f'B_max = {B_max} mT')
plt.plot(z_max, B_max, 'ro') # Roter Punkt direkt auf dem Maximum

plt.xlabel('Ort z [mm]')
plt.ylabel('Kraftflussdichte B [mT]')
plt.title('Magnetfeldverlauf der Spule')
plt.legend()
plt.grid(True)

# Speichern
plt.savefig(dir + 'Bfeld.png', dpi=300, bbox_inches='tight')