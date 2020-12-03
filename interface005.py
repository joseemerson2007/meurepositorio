# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:24:48 2020

@author: josee
"""


import os

from PyQt5 import uic, QtWidgets

# Isso carrega o arquivo .ui para que o PyQt possa preencher o plug-in com os elementos do Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'interface005.ui'))


class Bailey005(QtWidgets.QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Bailey005, self).__init__(parent)
        self.setupUi(self)