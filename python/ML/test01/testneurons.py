import numpy as np
import random
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

n_punti = 500 

X = np.random.uniform(-10, 10, (n_punti, 2)) 
target = ((X[:, 0] > 0) & (X[:, 1] > 0)).astype(int)

X_solo_x = X[:, 0] 
target_x = (X_solo_x > 5).astype(int)

costi = []

history_w = []
history_b = []

errori = []


w = np.random.randn() # Peso casuale
b = np.random.randn() # Bias casuale
lr = 0.1

for i in range(1000):
    z = w * X_solo_x + b
    
    # 2. Applica la sigmoide (Predizione)
    y_pred = 1 / (1 + np.exp(-z))
    
    
    # 3. Calcola l'errore puntuale
    error = y_pred - target_x

    mse = np.mean(error**2)
    errori.append(mse)
    
    # 4. Calcola i gradienti
    # Nota: la derivata della sigmoide è già "dentro" questa semplificazione
    dw = np.mean(error * X_solo_x)
    db = np.mean(error)
    
    # 5. Aggiorna
    w -= lr * dw
    b -= lr * db

    print(w)
    print(b)

    history_w.append(w)
    history_b.append(b)



plt.scatter(X_solo_x, np.zeros_like(X_solo_x), c=y_pred, cmap='coolwarm')
plt.axvline(0, color='black', linestyle='--')
plt.title("Probabilità calcolata dal neurone (Rosso=1, Blu=0)")
plt.show()