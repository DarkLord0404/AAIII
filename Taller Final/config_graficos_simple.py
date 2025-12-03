# Configuración de gráficos
# Autor: Alexander Torres
# Objetivo: Dar parámetros visuales a los gráficos que se generen

import matplotlib.pyplot as plt

# Configuración matplotlib para el proyecto
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Montserrat', 'Arial', 'DejaVu Sans', 'Liberation Sans'],
    'figure.figsize': (12, 6),
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'legend.fontsize': 8,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'lines.linewidth': 0.75,
    'grid.alpha': 0.3,
    'axes.facecolor': '#fafcff',  # Azul hielo muy suave (Alice Blue)
    'axes.edgecolor': "#2E86AB",  # Azul océano principal
    'axes.prop_cycle': plt.cycler(color=[
        '#1F77B4',  # Azul matplotlib
        '#FF7F0E',  # Naranja matplotlib
        '#2CA02C',  # Verde matplotlib
        '#D62728',  # Rojo matplotlib
        '#9467BD',  # Púrpura matplotlib
        '#8C564B'   # Marrón matplotlib
    ])
})