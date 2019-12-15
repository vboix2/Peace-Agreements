# Importem les llibreries
import numpy as np
import pandas as pd

# Llegim les dades
dades = pd.read_csv('data.csv', sep=";")

# Afegim l'atribut nombre d'acords
dades['N_acords'] = 1

# Transformem les variables quantitatives per als acords de més d'un país
atribut = ['','','Loc2ISO','Loc3ISO','Loc4ISO','Loc5ISO','Loc6ISO','Loc7ISO','Loc8ISO','Loc9ISO']
for i in range(2,9):
    idx = np.logical_and(pd.notna(dades[atribut[i]]), pd.isna(dades[atribut[i+1]]))
    dades.loc[idx,['DevSoc','DevHum','DevInfra','IntFu','N_acords']] = \
    dades.loc[idx,['DevSoc','DevHum','DevInfra','IntFu','N_acords']] / i  
# Acords amb 9 països
idx = pd.notna(dades['Loc9ISO'])
dades.loc[idx,['DevSoc','DevHum','DevInfra','IntFu','N_acords']] = \
dades.loc[idx,['DevSoc','DevHum','DevInfra','IntFu','N_acords']] / 9

# Transformem les dades al format llarg
dades_long = pd.melt(dades, id_vars=['Con', 'Dev','DevSoc','DevHum','DevInfra','IntFu','N_acords'],
        value_vars=['Loc1ISO','Loc2ISO','Loc3ISO','Loc4ISO','Loc5ISO','Loc6ISO','Loc7ISO','Loc8ISO','Loc9ISO'],
        value_name='Loc')
        
# Eliminem la columna variable
dades_long = dades_long.drop(['variable'], axis=1)

# Agreguem les dades per país i Dev
dades_long = dades_long.groupby(['Loc','Dev']).sum()

# Guardem les dades en un fitxer CSV
dades_long.to_csv('data_transformed.csv', sep=';', decimal=',')
