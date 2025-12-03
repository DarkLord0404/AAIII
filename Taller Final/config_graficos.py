"""
Configuraciones y utilidades para análisis de series de tiempo
Autor: [Tu nombre]
Fecha: Diciembre 2025

Este módulo contiene configuraciones globales, funciones de utilidad y 
configuraciones de gráficos para el análisis de series de tiempo.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error


def configurar_entorno():
    """
    Configura el entorno de trabajo con todas las configuraciones necesarias
    """
    # Suprimir warnings
    warnings.filterwarnings('ignore')
    
    # Configuración de matplotlib
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['axes.facecolor'] = '#f8f9fa'
    plt.rcParams['figure.facecolor'] = 'white'
    
    # Configuración de seaborn
    sns.set_palette("husl")
    
    print("Entorno configurado correctamente")
    print(f"Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


def configurar_grafico_serie_tiempo(ax, titulo, xlabel="Tiempo", ylabel="Valores", 
                                   agregar_grid=True, color_fondo='#f8f9fa'):
    """
    Aplica configuración estándar para gráficos de series de tiempo
    
    Parameters:
    -----------
    ax : matplotlib.axes
        Eje del gráfico
    titulo : str
        Título del gráfico
    xlabel : str
        Etiqueta del eje X
    ylabel : str
        Etiqueta del eje Y
    agregar_grid : bool
        Si agregar grilla
    color_fondo : str
        Color de fondo del gráfico
    """
    ax.set_title(titulo, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    
    if agregar_grid:
        ax.grid(True, alpha=0.3)
    
    ax.set_facecolor(color_fondo)
    

def plot_serie_tiempo_comparacion(datos1, datos2, labels, titulo, 
                                 colores=['steelblue', 'coral'], 
                                 figsize=(14, 8), alpha=0.8):
    """
    Crea gráfico comparativo de dos series de tiempo
    
    Parameters:
    -----------
    datos1, datos2 : pd.Series
        Series de tiempo a comparar
    labels : list
        Etiquetas para la leyenda
    titulo : str
        Título del gráfico
    colores : list
        Colores para las líneas
    figsize : tuple
        Tamaño de la figura
    alpha : float
        Transparencia de las líneas
    
    Returns:
    --------
    fig, ax : matplotlib figure y axes
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(datos1.index, datos1.values, linewidth=2.5, label=labels[0], 
            color=colores[0], alpha=alpha)
    ax.plot(datos2.index, datos2.values, linewidth=2.5, label=labels[1], 
            color=colores[1], alpha=alpha)
    
    configurar_grafico_serie_tiempo(ax, titulo)
    ax.legend(loc='upper right', fontsize=12)
    
    plt.tight_layout()
    return fig, ax


def plot_distribucion_comparativa(datos1, datos2, labels, titulo_base, 
                                 colores=['steelblue', 'coral'], figsize=(15, 6)):
    """
    Crea histogramas comparativos de dos series
    
    Parameters:
    -----------
    datos1, datos2 : pd.Series
        Series a comparar
    labels : list
        Etiquetas para los productos
    titulo_base : str
        Título base para los histogramas
    colores : list
        Colores para los histogramas
    figsize : tuple
        Tamaño de la figura
        
    Returns:
    --------
    fig, axes : matplotlib figure y axes
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Histograma 1
    ax1.hist(datos1, bins=25, color=colores[0], alpha=0.7, edgecolor='black')
    ax1.axvline(datos1.mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Media: {datos1.mean():.2f}')
    ax1.axvline(datos1.median(), color='orange', linestyle='--', linewidth=2, 
                label=f'Mediana: {datos1.median():.2f}')
    ax1.set_title(f'{titulo_base} - {labels[0]}', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Valores')
    ax1.set_ylabel('Frecuencia')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Histograma 2
    ax2.hist(datos2, bins=25, color=colores[1], alpha=0.7, edgecolor='black')
    ax2.axvline(datos2.mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Media: {datos2.mean():.2f}')
    ax2.axvline(datos2.median(), color='orange', linestyle='--', linewidth=2, 
                label=f'Mediana: {datos2.median():.2f}')
    ax2.set_title(f'{titulo_base} - {labels[1]}', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Valores')
    ax2.set_ylabel('Frecuencia')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig, (ax1, ax2)


def plot_boxplots_comparativos(datos1, datos2, labels, colores=['steelblue', 'coral'], 
                              figsize=(12, 6)):
    """
    Crea boxplots comparativos para detectar outliers
    
    Parameters:
    -----------
    datos1, datos2 : pd.Series
        Series a comparar
    labels : list
        Etiquetas para los productos
    colores : list
        Colores para los boxplots
    figsize : tuple
        Tamaño de la figura
        
    Returns:
    --------
    fig, axes : matplotlib figure y axes
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Boxplot 1
    box1 = ax1.boxplot(datos1, patch_artist=True)
    box1['boxes'][0].set_facecolor(colores[0])
    box1['boxes'][0].set_alpha(0.7)
    ax1.set_title(f'Boxplot - {labels[0]}', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Valores')
    ax1.grid(True, alpha=0.3)
    
    # Boxplot 2
    box2 = ax2.boxplot(datos2, patch_artist=True)
    box2['boxes'][0].set_facecolor(colores[1])
    box2['boxes'][0].set_alpha(0.7)
    ax2.set_title(f'Boxplot - {labels[1]}', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Valores')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig, (ax1, ax2)


def detectar_outliers_iqr(serie, nombre):
    """
    Detecta outliers usando el método IQR
    
    Parameters:
    -----------
    serie : pd.Series
        Serie a analizar
    nombre : str
        Nombre de la serie para el reporte
        
    Returns:
    --------
    dict : Información sobre outliers detectados
    """
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = serie[(serie < lower) | (serie > upper)]
    
    resultado = {
        'nombre': nombre,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'limite_inferior': lower,
        'limite_superior': upper,
        'outliers': outliers,
        'num_outliers': len(outliers)
    }
    
    return resultado


def imprimir_resumen_outliers(resultado_outliers):
    """
    Imprime resumen de detección de outliers
    
    Parameters:
    -----------
    resultado_outliers : dict
        Resultado de detectar_outliers_iqr()
    """
    print(f"Análisis de outliers - {resultado_outliers['nombre']}:")
    print(f"   • Q1: {resultado_outliers['Q1']:.2f}, Q3: {resultado_outliers['Q3']:.2f}, IQR: {resultado_outliers['IQR']:.2f}")
    print(f"   • Límites: [{resultado_outliers['limite_inferior']:.2f}, {resultado_outliers['limite_superior']:.2f}]")
    print(f"   • Outliers detectados: {resultado_outliers['num_outliers']}")
    if resultado_outliers['num_outliers'] > 0:
        print(f"   • Valores outliers: {resultado_outliers['outliers'].values}")
    print()


def plot_matriz_correlacion(datos, titulo="Matriz de Correlación", 
                           figsize=(8, 6), cmap='coolwarm'):
    """
    Crea matriz de correlación con heatmap
    
    Parameters:
    -----------
    datos : pd.DataFrame
        DataFrame con los datos
    titulo : str
        Título del gráfico
    figsize : tuple
        Tamaño de la figura
    cmap : str
        Mapa de colores
        
    Returns:
    --------
    fig, ax : matplotlib figure y axes
    correlacion : pd.DataFrame
        Matriz de correlación
    """
    correlacion = datos.corr()
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(correlacion, 
                annot=True, 
                cmap=cmap, 
                center=0, 
                square=True,
                linewidths=0.5,
                fmt='.3f',
                cbar_kws={"shrink": .8},
                ax=ax)
    
    ax.set_title(titulo, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    
    return fig, ax, correlacion


def plot_dispersion_con_tendencia(x, y, titulo, xlabel, ylabel, 
                                 figsize=(10, 8), color='purple'):
    """
    Crea gráfico de dispersión con línea de tendencia
    
    Parameters:
    -----------
    x, y : array-like
        Datos para los ejes X e Y
    titulo : str
        Título del gráfico
    xlabel, ylabel : str
        Etiquetas de los ejes
    figsize : tuple
        Tamaño de la figura
    color : str
        Color de los puntos
        
    Returns:
    --------
    fig, ax : matplotlib figure y axes
    correlacion : float
        Coeficiente de correlación
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calcular correlación
    correlacion = np.corrcoef(x, y)[0, 1]
    
    # Gráfico de dispersión
    ax.scatter(x, y, alpha=0.6, s=50, color=color, edgecolors='black', linewidth=0.5)
    
    # Línea de tendencia
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    ax.plot(x, p(x), "r--", alpha=0.8, linewidth=2, 
            label=f'Tendencia (r={correlacion:.3f})')
    
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(titulo, fontsize=14, fontweight='bold', pad=20)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f8f9fa')
    
    plt.tight_layout()
    return fig, ax, correlacion


def plot_division_train_test(datos_train, datos_test, nombre_serie, 
                            train_len, figsize=(14, 8)):
    """
    Visualiza la división entre datos de entrenamiento y prueba
    
    Parameters:
    -----------
    datos_train : pd.Series
        Datos de entrenamiento
    datos_test : pd.Series
        Datos de prueba
    nombre_serie : str
        Nombre de la serie
    train_len : int
        Longitud del conjunto de entrenamiento
    figsize : tuple
        Tamaño de la figura
        
    Returns:
    --------
    fig, ax : matplotlib figure y axes
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(datos_train.index, datos_train.values, label='Entrenamiento', 
            color='steelblue', linewidth=2, alpha=0.8)
    ax.plot(datos_test.index, datos_test.values, label='Prueba', 
            color='red', linewidth=2, alpha=0.8)
    ax.axvline(x=train_len-1, color='black', linestyle='--', alpha=0.7, linewidth=2)
    
    configurar_grafico_serie_tiempo(ax, f'División Train/Test - {nombre_serie}')
    ax.legend()
    
    plt.tight_layout()
    return fig, ax


def calcular_metricas_basicas(serie, nombre):
    """
    Calcula métricas estadísticas básicas de una serie
    
    Parameters:
    -----------
    serie : pd.Series
        Serie a analizar
    nombre : str
        Nombre de la serie
        
    Returns:
    --------
    dict : Diccionario con las métricas
    """
    return {
        'nombre': nombre,
        'minimo': serie.min(),
        'maximo': serie.max(),
        'media': serie.mean(),
        'mediana': serie.median(),
        'desv_std': serie.std(),
        'cv': (serie.std() / serie.mean()) * 100,
        'rango': serie.max() - serie.min()
    }


def imprimir_metricas_basicas(metricas):
    """
    Imprime métricas básicas de forma formateada
    
    Parameters:
    -----------
    metricas : dict
        Resultado de calcular_metricas_basicas()
    """
    print(f"{metricas['nombre'].upper()}:")
    print(f"  • Mínimo: {metricas['minimo']:.2f}")
    print(f"  • Máximo: {metricas['maximo']:.2f}")
    print(f"  • Media: {metricas['media']:.2f}")
    print(f"  • Mediana: {metricas['mediana']:.2f}")
    print(f"  • Desv. Estándar: {metricas['desv_std']:.2f}")
    print(f"  • CV: {metricas['cv']:.2f}%")
    print(f"  • Rango: {metricas['rango']:.2f}")


def interpretar_correlacion(valor_correlacion):
    """
    Interpreta el valor de correlación
    
    Parameters:
    -----------
    valor_correlacion : float
        Valor de correlación entre -1 y 1
        
    Returns:
    --------
    str : Interpretación de la correlación
    """
    abs_corr = abs(valor_correlacion)
    
    if abs_corr < 0.3:
        intensidad = "débil"
    elif abs_corr < 0.7:
        intensidad = "moderada"
    else:
        intensidad = "fuerte"
    
    direccion = "positiva" if valor_correlacion > 0 else "negativa"
    
    return f"Correlación {intensidad} {direccion}"


# Colores estándar para gráficos
COLORES = {
    'azul': 'steelblue',
    'coral': 'coral', 
    'verde': 'green',
    'naranja': 'orange',
    'rojo': 'red',
    'purpura': 'purple',
    'gris': 'gray'
}

# Configuración de estilos para diferentes tipos de gráficos
ESTILOS_GRAFICOS = {
    'serie_tiempo': {
        'linewidth': 2,
        'alpha': 0.8
    },
    'histograma': {
        'bins': 25,
        'alpha': 0.7,
        'edgecolor': 'black'
    },
    'dispersion': {
        'alpha': 0.6,
        's': 50,
        'edgecolors': 'black',
        'linewidth': 0.5
    }
}

def save_datasets(datasets_dict, filename):
    """Guardar datasets en formato pickle."""
    import pickle
    
    with open(filename, 'wb') as f:
        pickle.dump(datasets_dict, f)
    
    print(f"Datasets guardados en: {filename}")
    
    return True


def plot_correlation_matrix(correlation_matrix, title='Matriz de Correlación'):
    """Plotear matriz de correlación con estilo personalizado."""
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, 
                annot=True, 
                cmap='coolwarm', 
                center=0, 
                square=True,
                linewidths=0.5,
                fmt='.3f',
                cbar_kws={"shrink": .8})

    plt.title(title, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()


def plot_train_test_split(train1, test1, train2, test2, split_point, title='División Train/Test'):
    """Visualizar división de train/test para ambos productos."""
    import matplotlib.pyplot as plt
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

    # Producto 1
    ax1.plot(train1.index, train1.iloc[:, 0], label='Entrenamiento', color='steelblue', linewidth=2, alpha=0.8)
    ax1.plot(test1.index, test1.iloc[:, 0], label='Prueba', color='red', linewidth=2, alpha=0.8)
    ax1.axvline(x=split_point-1, color='black', linestyle='--', alpha=0.7, linewidth=2)
    ax1.set_title(f'{title} - Producto 1', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Valores')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_facecolor('#f8f9fa')

    # Producto 2
    ax2.plot(train2.index, train2.iloc[:, 0], label='Entrenamiento', color='steelblue', linewidth=2, alpha=0.8)
    ax2.plot(test2.index, test2.iloc[:, 0], label='Prueba', color='red', linewidth=2, alpha=0.8)
    ax2.axvline(x=split_point-1, color='black', linestyle='--', alpha=0.7, linewidth=2)
    ax2.set_title(f'{title} - Producto 2', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Valores')
    ax2.set_xlabel('Tiempo')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_facecolor('#f8f9fa')

    plt.tight_layout()
    plt.show()