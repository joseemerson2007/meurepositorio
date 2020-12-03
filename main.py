# -*- coding: utf-8 -*-

"""
/***************************************************************************
                             --------------------------
        begin                : 2020-07-10
        copyright            : (C) 2020 by Jose Emerson
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
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from interface004 import Bailey004
from interface001 import Bailey001
from interface002 import Bailey002
from interface003 import Bailey003
from interface005 import Bailey005
import sys

  
def valor(lista, PCPi):
    m=[]

    for i in range(len(lista)):
        m.append(np.abs(PCPi - lista[i]))

    M = np.array(m)

    for i in lista:
        if np.abs(PCPi-i) == M.min():
    
            if PCPi-i>0:
                y = PCPi - M.min()
            else:
                y = PCPi + M.min()
    return y

def click_next_bailey004():
    abrir_bailey004.hide()
    abrir_bailey005.show()

def click_next_bailey005():
    abrir_bailey005.hide()
    abrir_bailey001.show()

def click_next_bailey001():
    abrir_bailey001.hide()
    abrir_bailey002.show()
    global lista, PCP, PCS, PCT, PM, DMN
    #DMN dos agregados#
    DMN = float(abrir_bailey001.txtDMN.text())
    lista = [0.075,0.15,0.30,0.60,1.18,2.36,4.75,9.5,12.5,19,25,37.5,50]
    PCPi = DMN*0.22
    PCP=valor(lista, PCPi)

    PCSi = valor(lista, PCP)*0.22
    PCS=valor(lista, PCSi)

    PCTi = valor (lista, PCS)*0.22
    PCT=valor(lista, PCTi)
    """
    if DMN==12.5:   
        PM=6.25
    """
    
    PMi = DMN/2
    PM = valor(lista, PMi)
 
    abrir_bailey002.ValorPCP1.setText(str(PCP))
       
    return lista, PCP, PCS, PCT, PM, DMN

def click_back01():
    abrir_bailey005.hide()
    abrir_bailey004.show()

    
def click_next_bailey002():
    abrir_bailey002.hide()
    abrir_bailey003.show()


def click_Back():
    abrir_bailey002.hide()
    abrir_bailey001.show()

def click_Back001():
    abrir_bailey003.hide()
    abrir_bailey001.show()
    
def click_Back002():
    abrir_bailey003.hide()
    abrir_bailey002.show()    

def click_Back003():
    abrir_bailey003.hide()
    abrir_bailey004.show()

def click_Back002_2():
    abrir_bailey003.hide()
    abrir_bailey005.show()

def click_Back005():
    abrir_bailey001.hide()
    abrir_bailey005.show()

def click_calcular():
    global s, q, w, e, r, t, u, V6, FINALAG1, FINALAG2, FINALAG3, FINALAF1, FINALAF2, FINALAF3, FINALFILER
              ##### INFORMAÇÕES DE ENTRADA E CÁLCULOS #####
    ### AG1 ###
    V1AG1=(float(abrir_bailey004.Pen_50AG1.text()))
    V2AG1=(float(abrir_bailey004.Pen_37AG1.text()))
    V3AG1=(float(abrir_bailey004.Pen_25AG1.text()))
    V4AG1=(float(abrir_bailey004.Pen_19AG1.text()))
    V5AG1=(float(abrir_bailey004.Pen_12AG1.text()))
    V6AG1=(float(abrir_bailey004.Pen_9AG1.text()))
    V7AG1=(float(abrir_bailey004.Pen_4AG1.text()))
    V8AG1=(float(abrir_bailey004.Pen_2AG1.text()))
    V9AG1=(float(abrir_bailey004.Pen_1AG1.text()))
    V10AG1=(float(abrir_bailey004.Pen_06AG1.text()))
    V11AG1=(float(abrir_bailey004.Pen_03AG1.text()))
    V12AG1=(float(abrir_bailey004.Pen_015AG1.text()))
    V13AG1=(float(abrir_bailey004.Pen_0075AG1.text()))
    q = [V13AG1,V12AG1,V11AG1,V10AG1,V9AG1,V8AG1,V7AG1,V6AG1,V5AG1,V4AG1,V3AG1,V2AG1,V1AG1]
    ### AG2 ###
    V1AG2=(float(abrir_bailey004.Pen_50AG2.text()))
    V2AG2=(float(abrir_bailey004.Pen_37AG2.text()))
    V3AG2=(float(abrir_bailey004.Pen_25AG2.text()))
    V4AG2=(float(abrir_bailey004.Pen_19AG2.text()))
    V5AG2=(float(abrir_bailey004.Pen_12AG2.text()))
    V6AG2=(float(abrir_bailey004.Pen_9AG2.text()))
    V7AG2=(float(abrir_bailey004.Pen_4AG2.text()))
    V8AG2=(float(abrir_bailey004.Pen_2AG2.text()))
    V9AG2=(float(abrir_bailey004.Pen_1AG2.text()))
    V10AG2=(float(abrir_bailey004.Pen_06AG2.text()))
    V11AG2=(float(abrir_bailey004.Pen_03AG2.text()))
    V12AG2=(float(abrir_bailey004.Pen_015AG2.text()))
    V13AG2=(float(abrir_bailey004.Pen_0075AG2.text()))
    w = [V13AG2,V12AG2,V11AG1,V10AG2,V9AG2,V8AG2,V7AG2,V6AG2,V5AG2,V4AG2,V3AG2,V2AG2,V1AG2]
    ### AG3 ###
    V1AG3=(float(abrir_bailey004.Pen_50AG3.text()))
    V2AG3=(float(abrir_bailey004.Pen_37AG3.text()))
    V3AG3=(float(abrir_bailey004.Pen_25AG3.text()))
    V4AG3=(float(abrir_bailey004.Pen_19AG3.text()))
    V5AG3=(float(abrir_bailey004.Pen_12AG3.text()))
    V6AG3=(float(abrir_bailey004.Pen_9AG3.text()))
    V7AG3=(float(abrir_bailey004.Pen_4AG3.text()))
    V8AG3=(float(abrir_bailey004.Pen_2AG3.text()))
    V9AG3=(float(abrir_bailey004.Pen_1AG3.text()))
    V10AG3=(float(abrir_bailey004.Pen_06AG3.text()))
    V11AG3=(float(abrir_bailey004.Pen_03AG3.text()))
    V12AG3=(float(abrir_bailey004.Pen_015AG3.text()))
    V13AG3=(float(abrir_bailey004.Pen_0075AG3.text()))
    e = [V13AG3,V12AG3,V11AG3,V10AG3,V9AG3,V8AG3,V7AG3,V6AG3,V5AG3,V4AG3,V3AG3,V2AG3,V1AG3]
    ### AF1 ###
    V1AF1=(float(abrir_bailey004.Pen_50AF1.text()))
    V2AF1=(float(abrir_bailey004.Pen_37AF1.text()))
    V3AF1=(float(abrir_bailey004.Pen_25AF1.text()))
    V4AF1=(float(abrir_bailey004.Pen_19AF1.text()))
    V5AF1=(float(abrir_bailey004.Pen_12AF1.text()))
    V6AF1=(float(abrir_bailey004.Pen_9AF1.text()))
    V7AF1=(float(abrir_bailey004.Pen_4AF1.text()))
    V8AF1=(float(abrir_bailey004.Pen_2AF1.text()))
    V9AF1=(float(abrir_bailey004.Pen_1AF1.text()))
    V10AF1=(float(abrir_bailey004.Pen_06AF1.text()))
    V11AF1=(float(abrir_bailey004.Pen_03AF1.text()))
    V12AF1=(float(abrir_bailey004.Pen_015AF1.text()))
    V13AF1=(float(abrir_bailey004.Pen_0075AF1.text()))
    r = [V13AF1,V12AF1,V11AF1,V10AF1,V9AF1,V8AF1,V7AF1,V6AF1,V5AF1,V4AF1,V3AF1,V2AF1,V1AF1]
    ### AF2 ###
    V1AF2=(float(abrir_bailey004.Pen_50AF2.text()))
    V2AF2=(float(abrir_bailey004.Pen_37AF2.text()))
    V3AF2=(float(abrir_bailey004.Pen_25AF2.text()))
    V4AF2=(float(abrir_bailey004.Pen_19AF2.text()))
    V5AF2=(float(abrir_bailey004.Pen_12AF2.text()))
    V6AF2=(float(abrir_bailey004.Pen_9AF2.text()))
    V7AF2=(float(abrir_bailey004.Pen_4AF2.text()))
    V8AF2=(float(abrir_bailey004.Pen_2AF2.text()))
    V9AF2=(float(abrir_bailey004.Pen_1AF2.text()))
    V10AF2=(float(abrir_bailey004.Pen_06AF2.text()))
    V11AF2=(float(abrir_bailey004.Pen_03AF2.text()))
    V12AF2=(float(abrir_bailey004.Pen_015AF2.text()))
    V13AF2=(float(abrir_bailey004.Pen_0075AF2.text()))
    t = [V13AF2,V12AF2,V11AF2,V10AF2,V9AF2,V8AF2,V7AF2,V6AF2,V5AF2,V4AF2,V3AF2,V2AF2,V1AF2]
    ### AF3 ###
    V1AF3=(float(abrir_bailey004.Pen_50AF3.text()))
    V2AF3=(float(abrir_bailey004.Pen_37AF3.text()))
    V3AF3=(float(abrir_bailey004.Pen_25AF3.text()))
    V4AF3=(float(abrir_bailey004.Pen_19AF3.text()))
    V5AF3=(float(abrir_bailey004.Pen_12AF3.text()))
    V6AF3=(float(abrir_bailey004.Pen_9AF3.text()))
    V7AF3=(float(abrir_bailey004.Pen_4AF3.text()))
    V8AF3=(float(abrir_bailey004.Pen_2AF3.text()))
    V9AF3=(float(abrir_bailey004.Pen_1AF3.text()))
    V10AF3=(float(abrir_bailey004.Pen_06AF3.text()))
    V11AF3=(float(abrir_bailey004.Pen_03AF3.text()))
    V12AF3=(float(abrir_bailey004.Pen_015AF3.text()))
    V13AF3=(float(abrir_bailey004.Pen_0075AF3.text()))
    u = [V13AF3,V12AF3,V11AF3,V10AF3,V9AF3,V8AF3,V7AF3,V6AF3,V5AF3,V4AF3,V3AF3,V2AF3,V1AF3]
    ### FILER ###
    V1F=(float(abrir_bailey004.Pen_50F.text()))
    V2F=(float(abrir_bailey004.Pen_37F.text()))
    V3F=(float(abrir_bailey004.Pen_25F.text()))
    V4F=(float(abrir_bailey004.Pen_19F.text()))
    V5F=(float(abrir_bailey004.Pen_12F.text()))
    V6F=(float(abrir_bailey004.Pen_9F.text()))
    V7F=(float(abrir_bailey004.Pen_4F.text()))
    V8F=(float(abrir_bailey004.Pen_2F.text()))
    V9F=(float(abrir_bailey004.Pen_1F.text()))
    V10F=(float(abrir_bailey004.Pen_06F.text()))
    V11F=(float(abrir_bailey004.Pen_03F.text()))
    V12F=(float(abrir_bailey004.Pen_015F.text()))
    V13F=(float(abrir_bailey004.Pen_0075F.text()))
    
                    #### AGREGADOS GRAÚDOS ####
    #Quantidades Iniciais#
    QiAG1 = float(abrir_bailey001.txtGraudosQI1.text())
    QiAG2 = float(abrir_bailey001.txtGraudosQI2.text())
    QiAG3 = float(abrir_bailey001.txtGraudosQI3.text())
    
    #AG1#
    MESAG1 = float(abrir_bailey001.txtGraudosMES1.text())
    MECAG1 = float(abrir_bailey001.txtGraudosMEC1.text())
    GsbAG1 = float(abrir_bailey001.txtGraudosMEA1.text())
    
    #AG2#
    MESAG2 = float(abrir_bailey001.txtGraudosMES2.text())
    MECAG2 = float(abrir_bailey001.txtGraudosMEC2.text())
    GsbAG2 = float(abrir_bailey001.txtGraudosMEA2.text())
    
    #AG3#
    MESAG3 = float(abrir_bailey001.txtGraudosMES3.text())
    MECAG3 = float(abrir_bailey001.txtGraudosMEC3.text())
    GsbAG3 = float(abrir_bailey001.txtGraudosMEA3.text())
    
    #Porcentagem da MES/MEC para determinar a Massa Específica Escolhida do AG"
    z = float(abrir_bailey001.txtMEE.text())
    if z==0:
        pctMESAG=0
    else:
        pctMESAG = z/100
    
    #Massa Específica Escolhida Mistura Densa (MEEd)#
    MEEAG1 = MESAG1*pctMESAG
    MEEAG2 = MESAG2*pctMESAG
    MEEAG3 = MESAG3*pctMESAG
    
    #Massa Específica Escolhida Mistura SMA (MEEsma)#
    MEEAG1s = MECAG1*pctMESAG
    MEEAG2s = MECAG2*pctMESAG
    MEEAG3s = MECAG3*pctMESAG
    
    #Massa específica contribuinte de cada agregado#
    if abrir_bailey005.checkBox_MD.isChecked() == True:
        if QiAG1==0:
            contAG1=0
        else:
            contAG1 = (QiAG1/100)*MEEAG1
        if QiAG2==0:
            contAG2=0
        else:
            contAG2 = (QiAG2/100)*MEEAG2
        if QiAG3==0:
            contAG3=0
        else:
            contAG3 = (QiAG3/100)*MEEAG3

    if abrir_bailey005.checkBox_SMA.isChecked() == True:
        if QiAG1==0:
            contAG1=0
        else:
            contAG1 = (QiAG1/100)*MEEAG1s
        if QiAG2==0:
            contAG2=0
        else:
            contAG2 = (QiAG2/100)*MEEAG2s
        if QiAG3==0:
            contAG3=0
        else:
            contAG3 = (QiAG3/100)*MEEAG3s
    
    #Volume de vazios dos agregados graúdos#
    if abrir_bailey005.checkBox_MD.isChecked() == True:
        if GsbAG1==0:
            VVAG1=0
        else:
            VVAG1 = 100*((1-(MEEAG1/(GsbAG1*1000)))*(QiAG1/100))
        if GsbAG2==0:
            VVAG2=0
        else:
            VVAG2 = 100*((1-(MEEAG2/(GsbAG2*1000)))*(QiAG2/100))
        if GsbAG3==0:
            VVAG3=0
        else:
            VVAG3 = 100*((1-(MEEAG3/(GsbAG3*1000)))*(QiAG3/100))

    if abrir_bailey005.checkBox_SMA.isChecked() == True:
        if GsbAG1==0:
            VVAG1=0
        else:
            VVAG1 = 100*((1-(MEEAG1s/(GsbAG1*1000)))*(QiAG1/100))
        if GsbAG2==0:
            VVAG2=0
        else:
            VVAG2 = 100*((1-(MEEAG2s/(GsbAG2*1000)))*(QiAG2/100))
        if GsbAG3==0:
            VVAG3=0
        else:
            VVAG3 = 100*((1-(MEEAG3s/(GsbAG3*1000)))*(QiAG3/100))
   
    #Total de vazios dos agregados graúdos#
    TOTALAG = round((VVAG1+VVAG2+VVAG3),2)
    abrir_bailey002.VAG.setText(str(TOTALAG))
                ##### AGREGADOS FINOS #####
    #Quantidades Iniciais#
    QiAF1 = float(abrir_bailey001.txtFinosQI1.text())
    QiAF2 = float(abrir_bailey001.txtFinosQI2.text())
    QiAF3 = float(abrir_bailey001.txtFinosQI3.text())

    #AF1#
    MECAF1 = float(abrir_bailey001.txtFinosMEC1.text())
    MESAF1 = float(abrir_bailey001.txtFinosMES1.text())
    #AF2#
    MECAF2 = float(abrir_bailey001.txtFinosMEC2.text())
    MESAF2 = float(abrir_bailey001.txtFinosMES2.text())
    #AF3#
    MECAF3 = float(abrir_bailey001.txtFinosMEC3.text())
    MESAF3 = float(abrir_bailey001.txtFinosMES3.text())
    
    #Massa Específica Escolhida MISTURA DENSA (MEE)#
    MEEAF1 = MECAF1
    MEEAF2 = MECAF2
    MEEAF3 = MECAF3

    #Massa Específica Escolhida MISTURA SMA (MEE)#
    MEEAF1s = MESAF1
    MEEAF2s = MESAF2
    MEEAF3s = MESAF3

    #Massa específica contribuinte de cada agregado MISTURAS DENSAS#
    if abrir_bailey005.checkBox_MD.isChecked() == True:
        contAF1 = ((QiAF1/100)*MEEAF1*TOTALAG)/100
        contAF2 = ((QiAF2/100)*MEEAF2*TOTALAG)/100
        contAF3 = ((QiAF3/100)*MEEAF3*TOTALAG)/100

    #Massa específica contribuinte de cada agregado MISTURAS SMA#
    if abrir_bailey005.checkBox_SMA.isChecked() == True:
        contAF1 = ((QiAF1/100)*MEEAF1s*TOTALAG)/100
        contAF2 = ((QiAF2/100)*MEEAF2s*TOTALAG)/100
        contAF3 = ((QiAF3/100)*MEEAF3s*TOTALAG)/100

                ##### MASSA ESPECÍFICA DA MISTURA #####
    MEMISTURA = round((contAG1+contAG2+contAG3+contAF1+contAF2+contAF3),2)

        ##### PORCENTAGEM DE FÍLER DESEJADA PARA A MISTURA #####
    FILERDES = float(abrir_bailey001.QuantUtilizada.text())
    
            ##### PORCENTAGEM EM PESO DE CADA AGREGADO #####
    PESOAG1 = (contAG1/MEMISTURA)*100
    PESOAG2 = (contAG2/MEMISTURA)*100
    PESOAG3 = (contAG3/MEMISTURA)*100
    PESOAF1 = (contAF1/MEMISTURA)*100
    PESOAF2 = (contAF2/MEMISTURA)*100
    PESOAF3 = (contAF3/MEMISTURA)*100

            ##### PASSAR O AG E O AF NA PCP E VERIFICAR: #####
    conta1=0
    for b in range(0,len(lista),1):
        if PCP==lista[b]:
            conta1 = conta1+b
            AG1PASS = q[conta1]
            AG2PASS = w[conta1]
            AG3PASS = e[conta1]
            if r[conta1]==0:
                AF1RET=0
            else:
                AF1RET = round((100 - r[conta1]),2)
            if t[conta1]==0:
                AF2RET=0
            else:
                AF2RET = round((100 - t[conta1]),2)
            if u[conta1]==0:
                AF3RET=0
            else:
                AF3RET = round((100 - u[conta1]),2)
    
    abrir_bailey002.PCPAG1.setText(str(AG1PASS))
    abrir_bailey002.PCPAG2.setText(str(AG2PASS))
    abrir_bailey002.PCPAG3.setText(str(AG3PASS))
    abrir_bailey002.PCPAF1.setText(str(AF1RET))
    abrir_bailey002.PCPAF2.setText(str(AF2RET))
    abrir_bailey002.PCPAF3.setText(str(AF3RET))
    
    abrir_bailey002.FilerAG1.setText(str(V13AG1))
    abrir_bailey002.FilerAG2.setText(str(V13AG2))
    abrir_bailey002.FilerAG3.setText(str(V13AG3))
    abrir_bailey002.FilerAF1.setText(str(V13AF1))
    abrir_bailey002.FilerAF2.setText(str(V13AF2))
    abrir_bailey002.FilerAF3.setText(str(V13AF3))
    
    abrir_bailey002.Filer200.setText(str(V13F))
    
        ##### 1) PORCENTAGEM DE CADA AG USADO QUE PASSA NA PCP #####
    PASSAG1 = AG1PASS
    PASSAG2 = AG2PASS
    PASSAG3 = AG3PASS

        ##### 2) PORCENTAGEM DE CADA AF USADO RETIDO NA PCP #####
    RETAF1 = AF1RET
    RETAF2 = AF2RET
    RETAF3 = AF3RET

                ##### PORCENTAGEM DE FINOS NO AG #####
    FINOSAG1 = (PASSAG1*PESOAG1)/100
    FINOSAG2 = (PASSAG2*PESOAG2)/100
    FINOSAG3 = (PASSAG3*PESOAG3)/100
    TOTALFINOSAG = round((FINOSAG1+FINOSAG2+FINOSAG3),2)

                ##### PORCENTAGEM DE GRAÚDOS NO AF #####
    AG1FINOS = (RETAF1*PESOAF1)/100
    AG2FINOS = (RETAF2*PESOAF2)/100
    AG3FINOS = (RETAF3*PESOAF3)/100
    TOTALAGFINOS = round((AG1FINOS+AG2FINOS+AG3FINOS),2)

                ##### AJUSTE DAS PORCENTAGENS #####
    AJUSTEPESOAG1 = round((PESOAG1+FINOSAG1-((PESOAG1*TOTALAGFINOS)/(PESOAG1+PESOAG2+PESOAG3))),2)
    AJUSTEPESOAG2 = round((PESOAG2+FINOSAG2-((PESOAG2*TOTALAGFINOS)/(PESOAG1+PESOAG2+PESOAG3))),2)
    AJUSTEPESOAG3 = round((PESOAG3+FINOSAG3-((PESOAG3*TOTALAGFINOS)/(PESOAG1+PESOAG2+PESOAG3))),2)
    AJUSTEPESOAF1 = round((PESOAF1+AG1FINOS-((PESOAF1*TOTALFINOSAG)/(PESOAF1+PESOAF2+PESOAF3))),2)
    AJUSTEPESOAF2 = round((PESOAF2+AG2FINOS-((PESOAF2*TOTALFINOSAG)/(PESOAF1+PESOAF2+PESOAF3))),2)
    AJUSTEPESOAF3 = round((PESOAF3+AG3FINOS-((PESOAF3*TOTALFINOSAG)/(PESOAF1+PESOAF2+PESOAF3))),2)

                ##### PORCENTAGEM DE FÍLER PARA CADA AGREGADO #####
    FILERAG1 = V13AG1
    FILERAG2 = V13AG2
    FILERAG3 = V13AG3
    FILERAF1 = V13AF1
    FILERAF2 = V13AF2
    FILERAF3 = V13AF3
    FAG1=FILERAG1/100
    FAG2=FILERAG2/100
    FAG3=FILERAG3/100
    FAF1=FILERAF1/100
    FAF2=FILERAF2/100
    FAF3=FILERAF3/100

    ##### PORCENTAGEM CONTRIBUINTE DE FÍLER PARA CADA AGREGADO #####
    PCFILERAG1 = round((FAG1*AJUSTEPESOAG1),2)
    PCFILERAG2 = round((FAG2*AJUSTEPESOAG2),2)
    PCFILERAG3 = round((FAG3*AJUSTEPESOAG3),2)
    PCFILERAF1 = round((FAF1*AJUSTEPESOAF1),2)
    PCFILERAF2 = round((FAF2*AJUSTEPESOAF2),2)
    PCFILERAF3 = round((FAF3*AJUSTEPESOAF3),2)
    TOTALFILER = PCFILERAF1+PCFILERAF2+PCFILERAF3+PCFILERAG1+PCFILERAG2+PCFILERAG3

           ##### PORCENTAGEM DE FILER MINERAL REQUERIDO #####
    FILERREAL=float(abrir_bailey002.Filer200.text())
    if FILERDES == 0:
        FILERREQ = 0
    else:
        FILERREQ = round((((abs(FILERDES-TOTALFILER))/FILERREAL)*100),2)
        AJUSTEAF1 = round((AJUSTEPESOAF1-((AJUSTEPESOAF1*FILERREQ)/(AJUSTEPESOAF1+AJUSTEPESOAF2+AJUSTEPESOAF3))),2)
        AJUSTEAF2 = round((AJUSTEPESOAF2-((AJUSTEPESOAF2*FILERREQ)/(AJUSTEPESOAF1+AJUSTEPESOAF2+AJUSTEPESOAF3))),2)
        AJUSTEAF3 = round((AJUSTEPESOAF3-((AJUSTEPESOAF3*FILERREQ)/(AJUSTEPESOAF1+AJUSTEPESOAF2+AJUSTEPESOAF3))),2)
           ##### AJUSTE DO AF ADICIONANDO O FILER (ACIMA) #####            

           ##### PORCENTAGENS FINAIS DOS AGREGADOS #####
    FINALAG1 = round(AJUSTEPESOAG1,2)
    FINALAG2 = round(AJUSTEPESOAG2,2)
    FINALAG3 = round(AJUSTEPESOAG3,2)
    if FILERREQ == 0:
        FINALAF1 = round(AJUSTEPESOAF1,2)
        FINALAF2 = round(AJUSTEPESOAF2,2)
        FINALAF3 = round(AJUSTEPESOAF3,2)
    else:
        FINALAF1 = round(AJUSTEAF1,2)
        FINALAF2 = round(AJUSTEAF2,2)
        FINALAF3 = round(AJUSTEAF3,2)
    FINALFILER = round(FILERREQ,2)
    
    V50 = round((((V1AG1*FINALAG1)+(V1AG2*FINALAG2)+(V1AG3*FINALAG3)+(V1AF1*FINALAF1)+(V1AF2*FINALAF2)+(V1AF3*FINALAF3)+(V1F*FINALFILER))/100),2)
    V37 = round((((V2AG1*FINALAG1)+(V2AG2*FINALAG2)+(V2AG3*FINALAG3)+(V2AF1*FINALAF1)+(V2AF2*FINALAF2)+(V2AF3*FINALAF3)+(V2F*FINALFILER))/100),2)
    V25 = round((((V3AG1*FINALAG1)+(V3AG2*FINALAG2)+(V3AG3*FINALAG3)+(V3AF1*FINALAF1)+(V3AF2*FINALAF2)+(V3AF3*FINALAF3)+(V3F*FINALFILER))/100),2)
    V19 = round((((V4AG1*FINALAG1)+(V4AG2*FINALAG2)+(V4AG3*FINALAG3)+(V4AF1*FINALAF1)+(V4AF2*FINALAF2)+(V4AF3*FINALAF3)+(V4F*FINALFILER))/100),2)
    V12 = round((((V5AG1*FINALAG1)+(V5AG2*FINALAG2)+(V5AG3*FINALAG3)+(V5AF1*FINALAF1)+(V5AF2*FINALAF2)+(V5AF3*FINALAF3)+(V5F*FINALFILER))/100),2)
    V9 = round((((V6AG1*FINALAG1)+(V6AG2*FINALAG2)+(V6AG3*FINALAG3)+(V6AF1*FINALAF1)+(V6AF2*FINALAF2)+(V6AF3*FINALAF3)+(V6F*FINALFILER))/100),2)
    V4 = round((((V7AG1*FINALAG1)+(V7AG2*FINALAG2)+(V7AG3*FINALAG3)+(V7AF1*FINALAF1)+(V7AF2*FINALAF2)+(V7AF3*FINALAF3)+(V7F*FINALFILER))/100),2)
    V2 = round((((V8AG1*FINALAG1)+(V8AG2*FINALAG2)+(V8AG3*FINALAG3)+(V8AF1*FINALAF1)+(V8AF2*FINALAF2)+(V8AF3*FINALAF3)+(V8F*FINALFILER))/100),2)
    V1 = round((((V9AG1*FINALAG1)+(V9AG2*FINALAG2)+(V9AG3*FINALAG3)+(V9AF1*FINALAF1)+(V9AF2*FINALAF2)+(V9AF3*FINALAF3)+(V9F*FINALFILER))/100),2)
    V06 = round((((V10AG1*FINALAG1)+(V10AG2*FINALAG2)+(V10AG3*FINALAG3)+(V10AF1*FINALAF1)+(V10AF2*FINALAF2)+(V10AF3*FINALAF3)+(V10F*FINALFILER))/100),2)
    V03 = round((((V11AG1*FINALAG1)+(V11AG2*FINALAG2)+(V11AG3*FINALAG3)+(V11AF1*FINALAF1)+(V11AF2*FINALAF2)+(V11AF3*FINALAF3)+(V11F*FINALFILER))/100),2)
    V015 = round((((V12AG1*FINALAG1)+(V12AG2*FINALAG2)+(V12AG3*FINALAG3)+(V12AF1*FINALAF1)+(V12AF2*FINALAF2)+(V12AF3*FINALAF3)+(V12F*FINALFILER))/100),2)
    V0075 = round((((V13AG1*FINALAG1)+(V13AG2*FINALAG2)+(V13AG3*FINALAG3)+(V13AF1*FINALAF1)+(V13AF2*FINALAF2)+(V13AF3*FINALAF3)+(V13F*FINALFILER))/100),2)
    
    V6 = round((V4+(((6.25-4.75)/(9.5-4.75))*(V9-V4))),2)
    
    s=[V0075,V015,V03,V06,V1,V2,V4,V9,V12,V19,V25,V37,V50]
    print(s)
    return s, q, w, e, r, t, u, V6, FINALAG1, FINALAG2, FINALAG3, FINALAF1, FINALAF2, FINALAF3, FINALFILER
    
def click_analisar00():
    abrir_bailey003.ResultadoAG1.setText(str(FINALAG1))
    abrir_bailey003.ResultadoAG2.setText(str(FINALAG2))
    abrir_bailey003.ResultadoAG3.setText(str(FINALAG3))
    abrir_bailey003.ResultadoAF1.setText(str(FINALAF1))
    abrir_bailey003.ResultadoAF2.setText(str(FINALAF2))
    abrir_bailey003.ResultadoAF3.setText(str(FINALAF3))
    abrir_bailey003.ResultadoFiler.setText(str(FINALFILER))

def click_analisar():

        ##### PORCENTAGEM PASSANTE NAS PENEIRAS DE CONTROLE #####
    k=s
    PASSOUPCP=0
    PASSOUPCS=0
    PASSOUPCT=0
    PASSOUPM=0
    cont1=0
    cont2=0
    cont3=0
    cont4=0
    for i in range(0,len(k),1):
        if PCP==lista[i]:
            cont1 = cont1+i
            PASSOUPCP = k[cont1]        
        if PCS==lista[i]:
            cont2 = cont2+i
            PASSOUPCS = k[cont2]
        if PCT==lista[i]:
            cont3 = cont3+i
            PASSOUPCT = k[cont3]
        if PM==6.25:
            PASSOUPM=V6
        else:
            if PM==lista[i]:
                cont4 = cont4+i
                PASSOUPM = k[cont4]

                ##### CRITÉRIOS DO MÉTODO BAILEY #####
    PROPAG = round(((PASSOUPM-PASSOUPCP)/(100-PASSOUPM)),2)
    PROPGAF = round((PASSOUPCS/PASSOUPCP),2)
    PROPFAF = round((PASSOUPCT/PASSOUPCS),2)
    abrir_bailey003.ResPropAG.setText(str(PROPAG))
    abrir_bailey003.ResPropGAF.setText(str(PROPGAF))
    abrir_bailey003.ResPropFAF.setText(str(PROPFAF))

        ##### AVALIAÇÃO FAIXAS RECOMENDADAS PARA OS FATORES #####
    if abrir_bailey005.checkBox_MD.isChecked() == True:
        if DMN==37.5:
            if PROPAG>=0.8 and PROPAG<=0.95:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        if DMN==25:
            if PROPAG>=0.7 and PROPAG<=0.85:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        if DMN==19:
            if PROPAG>=0.6 and PROPAG<=0.75:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        if DMN==12.5:
            if PROPAG>=0.5 and PROPAG<=0.65:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        if DMN==9.5:
            if PROPAG>=0.4 and PROPAG<=0.55:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        if DMN==4.75:
            if PROPAG>=0.3 and PROPAG<=0.45:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
            
        if PROPGAF>=0.35 and PROPGAF<=0.5:
            abrir_bailey003.listAnalise.addItem('Proporção GAF = ATENDE ao critério')
        else:
            abrir_bailey003.listAnalise.addItem('Proporção GAF = NÃO ATENDE ao critério')
        if PROPFAF>=0.35 and PROPFAF<=0.5:
            abrir_bailey003.listAnalise.addItem('Proporção FAF = ATENDE ao critério')
        else:
            abrir_bailey003.listAnalise.addItem('Proporção FAF = NÃO ATENDE ao critério')
        
    if abrir_bailey005.checkBox_SMA.isChecked() == True:
        if DMN==19:
            if PROPAG>=0.35 and PROPAG<=0.50:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        if DMN==12.5:
            if PROPAG>=0.25 and PROPAG<=0.40:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        if DMN==9.5:
            if PROPAG>=0.15 and PROPAG<=0.30:
                abrir_bailey003.listAnalise.addItem('Proporção AG = ATENDE ao critério')
            else:
                abrir_bailey003.listAnalise.addItem('Proporção AG = NÃO ATENDE ao critério')
        
        if PROPGAF>=0.60 and PROPGAF<=0.85:
            abrir_bailey003.listAnalise.addItem('Proporção GAF = ATENDE ao critério')
        else:
            abrir_bailey003.listAnalise.addItem('Proporção GAF = NÃO ATENDE ao critério')
        if PROPFAF>=0.60 and PROPFAF<=0.85:
            abrir_bailey003.listAnalise.addItem('Proporção FAF = ATENDE ao critério')
        else:
            abrir_bailey003.listAnalise.addItem('Proporção FAF = NÃO ATENDE ao critério')
    return k

def click_confirmar1():
    if abrir_bailey005.checkBox_MD.isChecked() == True and abrir_bailey005.checkBox_SMA.isChecked() == True:
        abrir_bailey005.Inform1.addItem("####"
                                        "\nSelecione apenas uma opção e confirme novamente"
                                        "\n####")
    else:
        if abrir_bailey005.checkBox_MD.isChecked() == True:
            abrir_bailey005.Inform1.addItem("####"
                                            "\nINFORMAÇÕES PARA USO DO PROGRAMA"
                                            "\nVocê selecionou a opção de (Mistura Densa)"
                                            "\n+Para os agregados GRAÚDOS, realizar os ensaios:"
                                            "\na) Massa Específica;"
                                            "\nb) Massa Específica Solta;"
                                            "\n+Para os agregados FINOS, realizar os ensaios:"
                                            "\na) Massa Específica Compactada"
                                            "\n+No campo (MEE) da janela seguinte é recomendado"
                                            "\no uso de valores de 95% a 105%;"
                                            "\n+A quantidade de Fíler é função do tipo de mistura,"
                                            "\nconsulte os limites especificados em norma;"
                                            "\n+SIGA FIELMENTE AS INSTRUÇÕES AQUI LISTADAS E"
                                            "\nAS ENCONTRADAS NA TEORIA;"
                                            "\n+EM CASO DE DÚVIDA, CONSULTE A TEORIA OU ENTRE"
                                            "\nEM CONTATO COM O DESENVOLVEDOR PELO ENDEREÇO:"
                                            "\njoseemerson2007@gmail.com"
                                            "\n####")

        if abrir_bailey005.checkBox_SMA.isChecked() == True:
            abrir_bailey005.Inform1.addItem("####"
                                            "\nINFORMAÇÕES PARA USO DO PROGRAMA"
                                            "\nVocê selecionou a opção de (Mistura SMA)"
                                            "\n+Para os agregados GRAÚDOS, realizar os ensaios:"
                                            "\na) Massa Específica;"
                                            "\nb) Massa Específica Compactada;"
                                            "\n+Para os agregados FINOS, realizar os ensaios:"
                                            "\na) Massa Específica Solta"
                                            "\n+No campo (MEE) da janela seguinte é recomendado"
                                            "\no uso de valores de 110% a 125%;"
                                            "\n+A quantidade de Fíler é função do tipo de mistura,"
                                            "\nconsulte os limites especificados em norma;"
                                            "\n+SIGA FIELMENTE AS INSTRUÇÕES AQUI LISTADAS E"
                                            "\nAS ENCONTRADAS NA TEORIA;"
                                            "\n+EM CASO DE DÚVIDA, CONSULTE A TEORIA OU ENTRE"
                                            "\nEM CONTATO COM O DESENVOLVEDOR PELO ENDEREÇO:"
                                            "\njoseemerson2007@gmail.com"
                                            "\n####")

def click_curva():
    h=s
    ### PLOTAGEM GRÁFICO ###
    plt.title('Curva Granulométrica da Mistura Calculada', fontsize=16)    #adicinar título no grafico#
    plt.plot(lista,h, marker='o', label='Curva Granulométrica')  #adicinar curva no grafico#
    plt.legend(loc='up left',prop={'size':10})   #adicinar legenda no grafico#
    plt.grid(True,c='black', linestyle='-')
    plt.grid(which='minor',c='black',linestyle='--')
    plt.xscale('log')
    plt.xticks(lista, ('0.075','0.15','0.30','0.60','1.18','2.36','4.75','9.5','12.5','19.0','25.0','37.5','50.0'),rotation=35, fontsize=8)
    
    if DMN==37.5:
        plt.plot([50,37.5,37.5,25,2.36,2.36,0.075,0.075],[100,90,100,90,15,41,0,6], 'ro', label='Pontos de Controle')
        plt.plot([0.3,0.6,1.18,2.36,4.75],[10,11.7,15.5,23.3,34.7],marker='*',label='Zona de Restrição',c='g')
        plt.plot([0.3,0.6,1.18,2.36,4.75],[10,15.7,21.5,27.3,34.7],marker='*',c='g')
        plt.legend(loc='up left',prop={'size':10})
    if DMN==25:
        plt.plot([37.5,25,25,19,2.36,2.36,0.075,0.075],[100,90,100,90,19,45,1,7], 'ro', label='Pontos de Controle')
        plt.plot([0.3,0.6,1.18,2.36,4.75],[11.4,13.6,18.1,26.8,39.5],marker='*',label='Zona de Restrição',c='g')
        plt.plot([0.3,0.6,1.18,2.36,4.75],[11.4,17.6,24.1,30.8,39.5],marker='*',c='g')
        plt.legend(loc='up left',prop={'size':10})
    if DMN==19:
        plt.plot([25,19,19,12.5,2.36,2.36,0.075,0.075],[100,90,100,90,23,49,2,8], 'ro', label='Pontos de Controle')
        plt.plot([0.3,0.6,1.18,2.36],[13.7,16.7,22.3,34.6],marker='*',label='Zona de Restrição',c='g')
        plt.plot([0.3,0.6,1.18,2.36],[13.7,20.7,28.3,34.6],marker='*',c='g')
        plt.legend(loc='up left',prop={'size':10})
    if DMN==12.5:
        plt.plot([19,12.5,12.5,9.5,2.36,2.36,0.075,0.075],[100,90,100,90,28,58,2,10], 'ro', label='Pontos de Controle')
        plt.plot([0.3,0.6,1.18,2.36],[15.5,19.1,25.6,39.1],marker='*',label='Zona de Restrição',c='g')
        plt.plot([0.3,0.6,1.18,2.36],[15.5,23.1,31.6,39.1],marker='*',c='g')
        plt.legend(loc='up left',prop={'size':10})
    if DMN==9.5:
        plt.plot([12.5,9.5,9.5,4.75,2.36,2.36,0.075,0.075],[100,90,100,90,32,67,2,10], 'ro', label='Pontos de Controle')
        plt.plot([0.3,0.6,1.18,2.36],[18.7,23.5,31.6,47.2],marker='*',label='Zona de Restrição',c='g')
        plt.plot([0.3,0.6,1.18,2.36],[18.7,27.5,37.6,47.2],marker='*',c='g')
        plt.legend(loc='up left',prop={'size':10})
    

    if abrir_bailey003.DMN25.isChecked() == True:
        plt.plot([37.5,25,19,12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,100,86,63,52,28,24,21,18,15,10],marker="+", c="black", label='Limites SMA (DMN=25 mm) - AASHTO')
        plt.plot([37.5,25,19,12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,90,30,26,24,20,16,13,12,12,8], marker="+", c="black")
        plt.legend(loc='up left',prop={'size':10})
    if abrir_bailey003.DMN19.isChecked() == True:
        plt.plot([25,19,12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,100,74,60,28,24,21,18,15,10],marker="+", c="r", label='Limites SMA (DMN=19 mm) - AASHTO')
        plt.plot([25,19,12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,90,50,25,20,16,13,12,12,8], marker="+", c="r")
        plt.legend(loc='up left',prop={'size':10})
    if abrir_bailey003.DMN12.isChecked() == True:
        plt.plot([19,12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,100,78,28,24,21,18,15,10],marker="+", c="y", label='Limites SMA (DMN=12.5 mm) - AASHTO')
        plt.plot([19,12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,90,26,20,16,13,12,12,8], marker="+", c="y")
        plt.legend(loc='up left',prop={'size':10})
    if abrir_bailey003.DMN9.isChecked() == True:
        plt.plot([12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,100,60,28,21,18,15,10],marker="+", c="orange", label='Limites SMA (DMN=9.5 mm) - AASHTO')
        plt.plot([12.5,9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,90,26,20,13,12,12,8], marker="+", c="orange")
        plt.legend(loc='up left',prop={'size':10})
    if abrir_bailey003.DMN4.isChecked() == True:
        plt.plot([9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,100,65,36,28,22,15],marker="+", c="brown", label='Limites SMA (DMN=4.75 mm) - AASHTO')
        plt.plot([9.5,4.75,2.36,1.18,0.6,0.3,0.075],[100,90,28,22,18,15,12], marker="+", c="brown")
        plt.legend(loc='up left',prop={'size':10})
    
    if abrir_bailey003.FaixaA.isChecked() == True:
        plt.plot([50,37.5,25,19,9.5,4.75,2,0.42,0.18,0.075],[100,100,100,90,65,50,40,30,20,8],marker="+", c="black", label='Limites Faixa A - DNIT')
        plt.plot([50,37.5,25,19,9.5,4.75,2,0.42,0.18,0.075],[100,95,75,60,35,25,20,10,5,1], marker="+", c="black")
        plt.legend(loc='up left',prop={'size':10})
    if abrir_bailey003.FaixaB.isChecked() == True:
        plt.plot([37.5,25,19,9.5,4.75,2,0.42,0.18,0.075],[100,100,100,80,60,45,32,20,8],marker="+", c="r", label='Limites Faixa B - DNIT')
        plt.plot([37.5,25,19,9.5,4.75,2,0.42,0.18,0.075],[100,95,80,45,28,20,10,8,3], marker="+", c="r")
        plt.legend(loc='up left',prop={'size':10})
    if abrir_bailey003.FaixaC.isChecked() == True:
        plt.plot([19,12.5,9.5,4.75,2,0.42,0.18,0.075],[100,100,90,72,50,26,16,10],marker="+", c="orange", label='Limites Faixa C - DNIT')
        plt.plot([19,12.5,9.5,4.75,2,0.42,0.18,0.075],[100,80,70,44,22,8,4,2], marker="+", c="orange")
        plt.legend(loc='up left',prop={'size':10})

        
    plt.margins(0.05)
    plt.ylabel('Porcentagem Passante', fontsize=10)
    plt.xlabel('Abertura das Peneiras (mm)', fontsize=10)
    plt.show()  #plotar grafico#


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    abrir_bailey004 = Bailey004()
    abrir_bailey004.show()
    abrir_bailey004.btnNext_G.clicked.connect(click_next_bailey004)
    
    abrir_bailey005 = Bailey005()
    abrir_bailey005.btnconfirm.clicked.connect(click_confirmar1)
    abrir_bailey005.btnNext1_1.clicked.connect(click_next_bailey005)
    abrir_bailey005.btnBack1_2.clicked.connect(click_back01)
    
    abrir_bailey001 = Bailey001()
    abrir_bailey001.btnNext.clicked.connect(click_next_bailey001)
    abrir_bailey001.btnNext.clicked.connect(click_calcular)
    abrir_bailey001.btnBack.clicked.connect(click_Back005)
    
    abrir_bailey002 = Bailey002()
    abrir_bailey002.btnNext2.clicked.connect(click_next_bailey002)
    abrir_bailey002.btnBack1.clicked.connect(click_Back)
    
    abrir_bailey003 = Bailey003()
    abrir_bailey003.btnAnalisar.clicked.connect(click_analisar)
    abrir_bailey003.btnCurva.clicked.connect(click_curva)
    abrir_bailey003.btnCalcular.clicked.connect(click_analisar00)
    abrir_bailey003.btnBack001.clicked.connect(click_Back001)
    abrir_bailey003.btnBack002.clicked.connect(click_Back002)
    abrir_bailey003.btnBack003.clicked.connect(click_Back003)
    abrir_bailey003.btnBack002_2.clicked.connect(click_Back002_2)
        
    sys.exit(app.exec_())

