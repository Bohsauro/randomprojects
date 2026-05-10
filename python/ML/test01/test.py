import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

X = np.array([1, 2, 3, 4, 5]) # Esempio: Metri quadri (normalizzati)
y = np.array([2, 4, 6, 8, 10]) # Esempio: Prezzo (il target è y = 2x)
a

w = 0.0
b = 0.0
learning_rate = 0.01 # La lunghezza del tuo passo verso il minimo

costi = []

history_w = []
history_b = []

for i in range(1000):
    n = len(X)
    y_pred = w * X + b
    error = y_pred - y

    mse = np.mean(error**2)
    costi.append(mse)
    print(f"Costo attuale: {mse}")

    # Calcolo dei gradienti (le pendenze)
    dw = (2/n) * np.dot(X, error)
    db = (2/n) * np.sum(error)

    w = w - learning_rate * dw
    b = b - learning_rate * db

    history_w.append(w)
    history_b.append(b)




fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.25) # Spazio per lo slider

# Disegna i punti reali (fissi)
ax.scatter(X, y, color='red', label='Dati reali')
ax.set_xlim(min(X)-1, max(X)+1)
ax.set_ylim(min(y)-1, max(y)+1)

# Crea la linea iniziale (vuota o alla prima epoca)
line, = ax.plot(X, history_w[0] * X + history_b[0], color='blue', label='Modello ML')
ax.legend()

# Aggiungi lo slider
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Epoca', 0, len(history_w)-1, valinit=0, valfmt='%d')

# Funzione di aggiornamento
def update(val):
    idx = int(slider.val)
    current_w = history_w[idx]
    current_b = history_b[idx]
    line.set_ydata(current_w * X + current_b) # Aggiorna i dati della retta
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()