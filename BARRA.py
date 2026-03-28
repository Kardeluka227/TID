# Simulación Barra de prueba

# Datos
L = 2.0        # Largo (m)
A = 4         # Area (m2)
E = 200e9      # Elasticidad (Pa)
F = 1000       # Fuerza (N)
###################################
#Formulas respectivas
deltaL = (F * L) / (A * E)   # desplazamiento
stress = F / A              # esfuerzo
strain = deltaL / L          # deformacion 
###################################
# Resultados
print("=== RESULTADOS ===")
print(f"Largo: {L} m")
print(f"Fuerza: {F} N")
print(f"Desplazamiento: {deltaL:.6e} m")
print(f"Esfuerzo: {stress:.2f} Pa")
print(f"Deformacion: {strain:.6e}")