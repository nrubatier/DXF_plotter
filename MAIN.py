import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter

# ============================================================
# Données
# ============================================================
import numpy as np

points_init = np.array([
    # Droite 1
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0],
    [8, 0],
    [9, 0],
    [10, 0],

    # Arc de cercle (centre (10,5), rayon 5)
    [11.55, 0.24],
    [12.94, 0.95],
    [14.05, 2.06],
    [14.76, 3.45],
    [15.00, 5.00],

    # Droite 2
    [15.7, 5.7],
    [16.4, 6.4],
    [17.1, 7.1],
    [17.8, 7.8],
    [18.5, 8.5],
    [19.2, 9.2],
    [19.9, 9.9],
    [20.6, 10.6],
    [21.3, 11.3],
    [22.0, 12.0],
])

x = points_init[:, 0]
y = points_init[:, 1]

# Interpolation dense (pas de 0
# .05)
f = interp1d(x, y, kind='linear')
x_dense = np.arange(0, 22.0 + 0.2, 0.2)
y_dense = f(x_dense)

y_smooth = savgol_filter(y_dense, window_length=2, polyorder=1)

# calculer la courbure pour chaque point avec les X points au voisinage. Si changement trop brusque de courbure, regarder la courbures de dx points avant et après pour voir si c'est vraiment
# un changement de forme ou si c'est juste un bruit.
