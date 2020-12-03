# -*- coding: utf-8 -*-
"""
/***************************************************************************
                             --------------------------
        begin                : 2020-07-02
        copyright            : (C) 2020 by Jonas Daniel
                             --------------------------
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic, QtWidgets

# Isso carrega o arquivo .ui para que o PyQt possa preencher o plug-in com os elementos do Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'interface004.ui'))


class Bailey004(QtWidgets.QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Bailey004, self).__init__(parent)
        self.setupUi(self)