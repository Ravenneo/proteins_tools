#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Jorge Camarero Vera, Jose Jesus Gallego-Parrilla'

__license__ = "GPL"

__maintainer__ = "Jose Jesus Gallego-Parrilla"

__email__ = "J.J.Gallego-Parrilla2@newcastle.ac.uk"
"""

from ProteinHtml import ProteinHtml 

if __name__ == "__main__":
    protein = ProteinHtml("chandra.html") #name of the file you want check
    name = protein.getFileName()
    print(name)

    count = protein.searchProtein("Acidobacterium ailaaui")
    print(count)

    found = protein.findAllProteinNames()
    print(found)