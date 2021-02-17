#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Jorge Camarero Vera, Jose Jesus Gallego-Parrilla'

__license__ = "GPL"

__maintainer__ = "Jose Jesus Gallego-Parrilla"

__email__ = "J.J.Gallego-Parrilla2@newcastle.ac.uk"
"""

import pandas as pd
from ProteinHtml import ProteinHtml 

protein = ProteinHtml("chandra.html")

found = protein.findAllProteinNames()

names = []
places = []

for elem in found:
  names.append(elem)
  places.append(found[elem])

data = {'Name' : names, 'Place' : places}
dataframe = pd.DataFrame(data)
df = pd.DataFrame(data)
df.to_csv('all_proteins.csv', index=False)
print(dataframe)