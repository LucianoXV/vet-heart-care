import math

def weightcalc(iweight):
    return iweight * 1000

# -----------------------------------------------
# BSA

def BSA (weight):
    result = (10.1 * (weight ** (2 / 3))) / (10 ** 4)
    return result

# -----------------------------------------------
# Septo

def refSeptoY(vBSA):
    result = (5.28 + 5.6 * vBSA)
    return result

def refSeptoSY(vBSA):
    result = (1.762) * ((0.016 + (((vBSA - 0.75) ** 2) / 5.054)) ** 0.5)
    return result

def refSeptoMin(iSeptoY,iSeptoSY):
    result = iSeptoY - (1.999 * iSeptoSY)
    return round(result,1)

def refSeptoMax(iSeptoY,iSeptoSY):
    result = iSeptoY + (1.999 * iSeptoSY)
    return round(result,1)

def checkSepto(iweight, iSepto):
    iweight = weightcalc(iweight)
    iBSA = BSA(iweight)
    irefSeptoY = refSeptoY(iBSA)
    irefSeptoSY = refSeptoSY(iBSA)
    irefSeptoMin = refSeptoMin(irefSeptoY,irefSeptoSY)
    irefSeptoMax = refSeptoMax(irefSeptoY,irefSeptoSY)

    if iSepto < irefSeptoMin:        
        return 'Diminuido'
    elif iSepto > irefSeptoMin and iSepto < irefSeptoMax:
        return 'Normal'
    elif iSepto > irefSeptoMax:
        return 'Aumentado'

# -----------------------------------------------
# LV Chamber - d

def refLVChamber_d_Y(weight):
    result = 5.66 + 9.416 * math.log(weight)
    return result

def refLVChamber_d_SY(weight):
    result = 2 * (2.9 * (math.sqrt(1.015 + ((weight - 27.4) ** 2) / 25947.2)))
    return result

def LVChamber_d_Min(iLVChamberY, iLVChamberSY):
    result = iLVChamberY - iLVChamberSY
    return result

def LVChamber_d_Max(iLVChamberY, iLVChamberSY):
    result = iLVChamberY + iLVChamberSY
    return result

def checkLVChamber_d(iweight, iLVChamber_d):
    #print (f'iweight before calc: "{iweight}"')
    #iweight = weightcalc(iweight)
    print (f'iweight: "{iweight}"')
    irefLVChamber_d_Y = refLVChamber_d_Y(iweight)
    print (f'irefLVChamber_d_Y: "{irefLVChamber_d_Y}"')
    irefLVChamber_d_SY = refLVChamber_d_SY(iweight)
    print (f'irefLVChamber_d_SY: "{irefLVChamber_d_SY}"')
    iLVChamber_d_Min = LVChamber_d_Min(irefLVChamber_d_Y,irefLVChamber_d_SY)
    print (f'iLVChamber_d_Min: "{iLVChamber_d_Min}"')
    iLVChamber_d_Max = LVChamber_d_Max(irefLVChamber_d_Y,irefLVChamber_d_SY)
    print (f'iLVChamber_d_Max: "{iLVChamber_d_Max}"')
    if iLVChamber_d < iLVChamber_d_Min:        
        return 'Diminuido'
    elif iLVChamber_d > iLVChamber_d_Min and iLVChamber_d < iLVChamber_d_Max:
        return 'Normal'
    elif iLVChamber_d > iLVChamber_d_Max:
        return 'Aumentado'

#------------------------------------------------
# LV Wall - Parede Livre Espessura

def lvwallY(vBSA):
    result = 4.18 +4.61 * vBSA
    return result

def lvwallSY(vBSA):
    result = 1.48 * ((0.016 + (((vBSA - 0.74) ** 2) / 5.147)) ** 0.5)
    return result

def LVWallMin(ilvwallY, ilvwallSY):
    result = ilvwallY - (1.999 * ilvwallSY)
    return result

def LVWallMax(ilvwallY, ilvwallSY):
    result = ilvwallY + (1.999 * ilvwallSY)
    return result

def checkLVWall(iweight, iLVWall):
    iweight = weightcalc(iweight)
    iBSA = BSA(iweight)
    ilvwallY = lvwallY(iBSA)
    ilvwallSY = lvwallSY(iBSA)
    iLVWallMin = LVWallMin(ilvwallY,ilvwallSY)
    iLVWallMax = LVWallMax(ilvwallY,ilvwallSY)
    if iLVWall < iLVWallMin:        
        return 'Diminuido'
    elif iLVWall > iLVWallMin and iLVWall < iLVWallMax:
        return 'Normal'
    elif iLVWall > iLVWallMax:
        return 'Aumentado'

# -----------------------------------------------
# LV Chamber - s

def lvchamber_s_y(weight):
    result = 1.59 + 6.525 * math.log(weight)
    return result

def lvchamber_s_sy(weight):
    result = 2 * (2.53 * (math.sqrt(1.015 + ((weight - 27.4) ** 2) / 25947.2)))
    return result

def lvchamber_s_min(ilvchamber_s_y, ilvchamber_s_sy):
    result = ilvchamber_s_y - ilvchamber_s_sy
    return result

def lvchamber_s_max(ilvchamber_s_y, ilvchamber_s_sy):
    result = ilvchamber_s_y + ilvchamber_s_sy
    return result

def checkLVChamber_s(iweight, iLVChamber_s):
    #iweight = weightcalc(iweight)
    ilvchamber_s_y = lvchamber_s_y(iweight)
    ilvchamber_s_sy = lvchamber_s_sy(iweight)
    ilvchamber_s_min = lvchamber_s_min(ilvchamber_s_y,ilvchamber_s_sy)
    ilvchamber_s_max = lvchamber_s_max(ilvchamber_s_y,ilvchamber_s_sy)
    if iLVChamber_s < ilvchamber_s_min:        
        return 'Diminuido'
    elif iLVChamber_s > ilvchamber_s_min and iLVChamber_s < ilvchamber_s_max:
        return 'Normal'
    elif iLVChamber_s > ilvchamber_s_max:
        return 'Aumentado'

# -----------------------------------------------
# Aorta

def aortaY(vBSA):
    result = 8.96 +17.44 * vBSA
    return result

def aortaSY(vBSA):
    result = 2.301 * ((0.017 + (((vBSA - 0.72) ** 2) / 4.529)) ** 0.5)
    return result

def aortaMin(iaortaY, iaortaSY):
    result = iaortaY - (2.002 * iaortaSY)
    return result

def aortaMax(iaortaY, iaortaSY):
    result = iaortaY + (2.002 * iaortaSY)
    return result

def checkAorta(iweight, iAorta):
    iweight = weightcalc(iweight)
    iBSA = BSA(iweight)
    iaortaY = aortaY(iBSA)
    iaortaSY = aortaSY(iBSA)
    iaortaMin = aortaMin(iaortaY,iaortaSY)
    iaortaMax = aortaMax(iaortaY,iaortaSY)
    if iAorta < iaortaMin:        
        return 'Diminuido'
    elif iAorta > iaortaMin and iAorta < iaortaMax:
        return 'Normal'
    elif iAorta > iaortaMax:
        return 'Aumentado'

# -----------------------------------------------
# Left Atrium

def leftatriumY(vBSA):
    result = 9.95 +15.35 * vBSA
    return result

def leftatriumSY(vBSA):
    result = 2.889 * ((0.017 + (((vBSA - 0.72) ** 2) / 4.522)) ** 0.5)
    return result

def leftatriumMin(ileftatriumY, ileftatriumSY):
    result = ileftatriumY - (2.003 * ileftatriumSY)
    return result

def leftatriumMax(ileftatriumY, ileftatriumSY):
    result = ileftatriumY + (2.003 * ileftatriumSY)
    return result

def checkLeftAtrium(iweight, ileftatrium):
    iweight = weightcalc(iweight)
    iBSA = BSA(iweight)
    ileftatriumY = leftatriumY(iBSA)
    ileftatriumSY = leftatriumSY(iBSA)
    ileftatriumMin = leftatriumMin(ileftatriumY,ileftatriumSY)
    ileftatriumMax = leftatriumMax(ileftatriumY,ileftatriumSY)
    if ileftatrium < ileftatriumMin:   
        return 'Diminuido'
    elif ileftatrium > ileftatriumMin and ileftatrium < ileftatriumMax:
        return 'Normal'
    elif ileftatrium > ileftatriumMax:
        return 'Aumentado'
