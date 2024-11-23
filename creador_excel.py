import pandas as pd

data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centímetros": [23,50,60,123,80]  
}
df = pd.DataFrame(data)
df.to_excel("muebles_medidas.xlsx", index=False)


