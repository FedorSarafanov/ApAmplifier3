from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 
import numpy as np
#0.1 mm
x = np.array([3, 3.2, 3.4, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.5, 5.7, 5.9, 6.1, 6.4, 6.7, 7.1, 7.6, 9.2, 9.3, 9.39, 9.47, 9.55, 9.6, 9.7, 9.8, 9.9, 10.1, 10.3, 10.5, 10.6, 10.7, 10.8, 10.9, 11, 11.08, 11.16, 11.23, 11.3, 11.35, 11.41, 11.5, 11.5, 11.6, 11.7, 11.78, 11.85, 11.9, 11.98, 12.05, 12.1, 12.15, 12.21])
y = np.array([2.22, 2.74, 3.41, 4.07, 4.81, 5.19, 5.56, 5.74, 6.48, 6.85, 7.41, 7.59, 7.78, 7.96, 8.15, 8.33, 8.33, 8.33, 8.33, 8.7, 9.07, 9.07, 9.07, 9.07, 9.07, 9.07, 9.07, 9.07, 9.07, 8.89, 8.89, 8.89, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7, 8.61, 8.52, 8.52, 8.52, 8.33, 8.33, 8.33, 8.33, 8.33, 8.33, 8.33, 8.15, 7.96, 7.96, 7.96, 7.96, 7.96, 7.78, 7.78, 7.59, 7.59, 7.41, 7.22, 7.22, 7.04])
x2 = np.array([3, 3.2, 3.4, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.5, 5.7, 5.9, 6.1, 6.4, 6.7, 7.1, 7.6, 8, 8.3, 8.5, 8.7, 8.9, 9, 9.1, 9.2, 9.3, 9.39, 9.47, 9.55, 9.6, 9.7, 9.8, 9.9, 10.1, 10.3, 10.5, 10.6, 10.7, 10.8, 10.9, 11, 11.08, 11.16, 11.23, 11.3, 11.35, 11.41, 11.5, 11.5, 11.6, 11.7, 11.78, 11.85, 11.9, 11.98, 12.05, 12.1, 12.15, 12.21])
y2 = np.array([2.22, 2.96, 4.44, 4.44, 5.93, 5.93, 5.93, 6.67, 7.41, 8.89, 9.63, 10.37, 11.85, 11.85, 12.59, 14.07, 14.07, 15.56, 17.78, 18.52, 20.74, 22.96, 23.70, 24.44, 24.44, 28.15, 31.11, 31.11, 31.85, 31.85, 31.85, 31.85, 31.85, 31.85, 31.85, 31.85, 31.85, 31.11, 31.11, 31.85, 31.11, 30.37, 31.85, 31.85, 31.11, 31.11, 30.37, 29.63, 28.89, 28.15, 29.63, 29.63, 29.63, 28.89, 28.89, 27.41, 27.41, 27.41, 27.41, 27.41, 27.41, 26.67, 26.67, 25.19, 25.19, 24.44, 24.44, 23.7, 23.7, 23.52])

plt.plot(x, y, '+',color='crimson')
plt.plot(x2, y2, '+',color='green')
plt.grid(True)
plt.ylabel('$K(F)$, ед')
plt.xlabel(' ln частоты, Гц')
plt.title('Зависимость выходного сигнала от частоты')
plt.legend(( "Без конденсатора", "С конденсатором"))
plt.savefig('z251.pdf',dpi=300)
plt.show()

