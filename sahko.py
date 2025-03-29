import matplotlib.pyplot as plt
import datetime
import random

# Luodaan esimerkkidata
tunnit = [datetime.time(h).strftime("%H:%M") for h in range(24)]
hinnat = [round(random.uniform(3, 15), 2) for _ in range(24)]

# Piirretään kuvaaja
plt.figure(figsize=(10, 5))
plt.plot(tunnit, hinnat, marker='o')
plt.title("Sähkön hinta / tunti")
plt.xlabel("Kellonaika")
plt.ylabel("Hinta (snt/kWh)")
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)

# Tallennetaan kuva tiedostoksi
plt.savefig("kuvaaja.png")
print("✅ Kuvaaja tallennettu tiedostoon: kuvaaja.png")
