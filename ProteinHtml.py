#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Jorge Camarero Vera, Jose Jesus Gallego-Parrilla'

__license__ = "GPL"

__maintainer__ = "Jose Jesus Gallego-Parrilla"

__email__ = "J.J.Gallego-Parrilla2@newcastle.ac.uk"
"""


import re

class ProteinHtml:
  __fileName = None
  __contentFile = None

  def __init__(self, fileName):
    self.__fileName = fileName
    with open(fileName) as f:
      self.__contentFile = f.read()

  def getFileName(self):
    return self.__fileName

  def searchProtein(self, proteinName):
    regexBegin = "<tr style = \"background:#[\w\d]+\"><td>WP_[\d]+\.1<\/td><td colspan = 5>(.*"
    regexEnd = ".*)<\/td><\/tr>"
    regex = regexBegin + proteinName + regexEnd
    count = sum(1 for match in re.finditer(r"{}".format(regex),
      self.__contentFile))
    return count

  def findAllProteinNames(self):
    allProteins = {}
    regex = "<tr style = \"background:#[\w\d]+\"><td>WP_[\d]+\.1<\/td><td colspan = 5>(.*)\[(.*)\]<\/td><\/tr>"
    for match in re.finditer(r"{}".format(regex), self.__contentFile):
      protein = match.group(1)
      if (protein in allProteins):
        allProteins[protein] += 1
      else:
        allProteins.update({protein: 1})
    return allProteins