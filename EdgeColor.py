def EdgeColor(PathTempArray, EdgeColors, EdgeWidths):
    if PathTempArray == ["TIJ", "CJS"] or PathTempArray == ["CJS", "TIJ"]:
        EdgeColors[0] = 'red'
        EdgeWidths[0] = 2
    if PathTempArray == ["TIJ", "HMO"] or PathTempArray == ["HMO", "TIJ"]:
        EdgeColors[1] = 'red'
        EdgeWidths[1] = 2
    if PathTempArray == ["TIJ", "SJD"] or PathTempArray == ["SJD", "TIJ"]:
        EdgeColors[2] = 'red'
        EdgeWidths[2] = 2
    if PathTempArray == ["CJS", "HMO"] or PathTempArray == ["HMO", "CJS"]:
        EdgeColors[3] = 'red'
        EdgeWidths[3] = 2
    if PathTempArray == ["CJS", "MTY"] or PathTempArray == ["MTY", "CJS"]:
        EdgeColors[4] = 'red'
        EdgeWidths[4] = 2
    if PathTempArray == ["CJS", "CUU"] or PathTempArray == ["CUU", "CJS"]:
        EdgeColors[5] = 'red'
        EdgeWidths[5] = 2
    if PathTempArray == ["HMO", "CUU"] or PathTempArray == ["CUU", "HMO"]:
        EdgeColors[6] = 'red'
        EdgeWidths[6] = 2
    if PathTempArray == ["CUL", "HMO"] or PathTempArray == ["HMO", "CUL"]:
        EdgeColors[7] = 'red'
        EdgeWidths[7] = 2  
    if PathTempArray == ["HMO", "SJD"] or PathTempArray == ["SJD", "HMO"]:
        EdgeColors[8] = 'red'
        EdgeWidths[8] = 2
    if PathTempArray == ["SJD", "CUL"] or PathTempArray == ["CUL", "SJD"]:
        EdgeColors[9] = 'red'
        EdgeWidths[9] = 2
    if PathTempArray == ["SJD", "PVR"] or PathTempArray == ["PVR", "SJD"]:
        EdgeColors[10] = 'red'
        EdgeWidths[10] = 2
    if PathTempArray == ["CUU", "MTY"] or PathTempArray == ["MTY", "CUU"]:
        EdgeColors[11] = 'red'
        EdgeWidths[11] = 2
    if PathTempArray == ["CUU", "BJX"] or PathTempArray == ["BJX", "CUU"]:
        EdgeColors[12] = 'red'
        EdgeWidths[12] = 2
    if PathTempArray == ["CUU", "CUL"] or PathTempArray == ["CUL", "CUU"]:
        EdgeColors[13] = 'red'
        EdgeWidths[13] = 2
    if PathTempArray == ["CUL", "PVR"] or PathTempArray == ["PVR", "CUL"]:
        EdgeColors[14] = 'red'
        EdgeWidths[14] = 2
    if PathTempArray == ["CUL", "GDL"] or PathTempArray == ["GDL", "CUL"]:
        EdgeColors[15] = 'red'
        EdgeWidths[15] = 2    
    if PathTempArray == ["CUL", "BJX"] or PathTempArray == ["BJX", "CUL"]:
        EdgeColors[16] = 'red'
        EdgeWidths[16] = 2
    if PathTempArray == ["BJX", "MTY"] or PathTempArray == ["MTY", "BJX"]:
        EdgeColors[17] = 'red'
        EdgeWidths[17] = 2
    if PathTempArray == ["MTY", "MEX"] or PathTempArray == ["MEX", "MTY"]:
        EdgeColors[18] = 'red'
        EdgeWidths[18] = 2
    if PathTempArray == ["MTY", "VER"] or PathTempArray == ["VER", "MTY"]:
        EdgeColors[19] = 'red'
        EdgeWidths[19] = 2
    if PathTempArray == ["MTY", "MID"] or PathTempArray == ["MID", "MTY"]:
        EdgeColors[20] = 'red'
        EdgeWidths[20] = 2
    if PathTempArray == ["GDL", "BJX"] or PathTempArray == ["BJX", "GDL"]:
        EdgeColors[21] = 'red'
        EdgeWidths[21] = 2
    if PathTempArray == ["BJX", "MEX"] or PathTempArray == ["MEX", "BJX"]:
        EdgeColors[22] = 'red'
        EdgeWidths[22] = 2
    if PathTempArray == ["GDL", "PVR"] or PathTempArray == ["PVR", "GDL"]:
        EdgeColors[23] = 'red'
        EdgeWidths[23] = 2  
    if PathTempArray == ["GDL", "MEX"] or PathTempArray == ["MEX", "GDL"]:
        EdgeColors[24] = 'red'
        EdgeWidths[24] = 2
    if PathTempArray == ["MEX", "VER"] or PathTempArray == ["VER", "MEX"]:
        EdgeColors[25] = 'red'
        EdgeWidths[25] = 2
    if PathTempArray == ["VER", "MID"] or PathTempArray == ["MID", "VER"]:
        EdgeColors[26] = 'red'
        EdgeWidths[26] = 2
    if PathTempArray == ["VER", "TGZ"] or PathTempArray == ["TGZ", "VER"]:
        EdgeColors[27] = 'red'
        EdgeWidths[27] = 2
    if PathTempArray == ["TGZ", "MID"] or PathTempArray == ["MID", "TGZ"]:
        EdgeColors[28] = 'red'
        EdgeWidths[28] = 2
    if PathTempArray == ["MID", "CUN"] or PathTempArray == ["CUN", "MID"]:
        EdgeColors[29] = 'red'
        EdgeWidths[29] = 2
    if PathTempArray == ["CUN", "TGZ"] or PathTempArray == ["TGZ", "CUN"]:
        EdgeColors[30] = 'red'
        EdgeWidths[30] = 2    