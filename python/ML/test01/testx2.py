import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

X = np.linspace(-3, 3, 100)
y = 2 * X**2 + 0.5 * X + 3 #+ np.random.randn(100) * 0.5


w1 = 0.0 # Per X^2
w2 = 0.0 # Per X
b = 0.0  # Intercetta
learning_rate = 0.01 # La lunghezza del tuo passo verso il minimo

costi = []

history_w1 = []
history_w2 = []
history_b = []

for i in range(1000):
    n = len(X)
    

    # 1. Calcolo della predizione parabolica
    # y_pred = w1*x^2 + w2*x + b
    y_pred = w1 * (X**2) + w2 * X + b
    
    # 2. Calcolo dell'errore e del costo
    error = y_pred - y
    mse = np.mean(error**2)
    costi.append(mse)
    
    # 3. Calcolo dei gradienti (Derivate parziali)
    # Per w1 (moltiplichiamo per X^2)
    dw1 = (2/n) * np.dot(X**2, error)
    # Per w2 (moltiplichiamo per X)
    dw2 = (2/n) * np.dot(X, error)
    # Per b (intercetta)
    db = (2/n) * np.sum(error)

    # 4. Aggiornamento dei pesi
    w1 = w1 - learning_rate * dw1
    w2 = w2 - learning_rate * dw2
    b = b - learning_rate * db

    # 5. Salvataggio storia (per lo slider)
    history_w1.append(w1)
    history_w2.append(w2)
    history_b.append(b)




fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.25) 

# 1. Disegna i punti reali
ax.scatter(X, y, color='red', label='Dati reali', alpha=0.5)
ax.set_xlim(min(X)-1, max(X)+1)
ax.set_ylim(min(y)-10, max(y)+10) # Un po' di margine in più per la parabola

# 2. Crea la curva iniziale usando la formula della parabola
# history_w1, history_w2 e history_b sono le liste dove hai salvato i pesi nel loop
curva_iniziale = history_w1[0] * (X**2) + history_w2[0] * X + history_b[0]
line, = ax.plot(X, curva_iniziale, color='blue', lw=2, label='Modello ML (Parabola)')
ax.legend()

# 3. Aggiungi lo slider
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Epoca', 0, len(history_w1)-1, valinit=0, valfmt='%d')

# 4. Funzione di aggiornamento con la logica quadratica
def update(val):
    idx = int(slider.val)
    # Recupero i tre parametri all'istante idx
    w1_corr = history_w1[idx]
    w2_corr = history_w2[idx]
    b_corr = history_b[idx]
    
    # Ricalcolo la parabola
    nuovi_y = w1_corr * (X**2) + w2_corr * X + b_corr
    
    line.set_ydata(nuovi_y) # Aggiorna la curva sul grafico
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()