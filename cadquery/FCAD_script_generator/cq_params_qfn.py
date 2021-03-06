# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

from collections import namedtuple

destination_dir="generated_qfn"
# destination_dir="./"


Params = namedtuple("Params", [
    'c',    # pin thickness, body center part height
#    'K',    # Fillet radius for pin edges
    'L',    # pin top flat part length (including fillet radius)
    'fp_r', # first pin indicator radius
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges
    'cce',  # chamfer of the epad 1st pin corner
    'D',    # body overall lenght
    'E',    # body overall width
    'A1',   # body-board separation
    'A2',   # body height
    'b',    # pin width
    'e',    # pin (center-to-center) distance

    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'epad',  # exposed pad, None or the dimensions as tuple: (width, length)
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_qfn = {
    'LGA1633': Params( #3x3mm, 16-pin LGA package, 1.0mm height
        #example - http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00250937.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 1.0,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 5,  # number of pins along X axis (width)
        npy = 3,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        modelName = 'lga16_3x3mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    'DFN622': Params( # 2x2mm, 0.65 pitch, 6 pins, 0.75mm height  DFN (DD / LTC)
        #Example - http://www.onsemi.com/pub_link/Collateral/NCP308-D.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.6,1.0), # e Pad #epad = None, # e Pad
        modelName = 'DFN6_2x2mm_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN8-33-50': Params( # 3x3mm, 0.5 pitch, 8 pins, 0.75mm height  DFN (DD / LTC)
        #Example - http://cds.linear.com/docs/en/datasheet/2875f.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7 - 0.25,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.38,1.65), # e Pad #epad = None, # e Pad
        modelName = 'DFN8_3x3mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),

    'DFN8-33-65': Params( # 3x3mm, 0.65 pitch, 8 pins, 1.0mm height  DFN (DD / LTC)
        #Example - http://www.st.com/web/en/resource/technical/document/datasheet/CD00001508.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 1.0,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.5,1.5), # e Pad #epad = None, # e Pad
        modelName = 'DFN8_3x3mm_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN823': Params( # 2x3mm, 0.5 pitch, 8 pins, 0.75mm height  DFN (DD / LTC)
        #Example - http://cds.linear.com/docs/en/datasheet/4365fa.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7 - 0.25,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.2,0.61), # e Pad #epad = None, # e Pad
        modelName = 'DFN8_2x3mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN865': Params( # 6x5mm, 1.27mm pitch, 8 pins, 1.0mm height  DFN
        #Example - https://www.everspin.com/file/217/download
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7 - 0.25,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 1,  # body height
        b = 0.4,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2,2), # e Pad #epad = None, # e Pad
        modelName = 'DFN8_6x5mm_p127', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN1023': Params( # 2x3mm, 0.5mm pitch, 10 pins, 0.75mm height  DFN
        #Example - http://www.ti.com.cn/general/cn/docs/lit/getliterature.tsp?genericPartNumber=tps62177&fileType=pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3 - 0.15,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 5,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.4,0.84), # e Pad #epad = None, # e Pad
        modelName = 'DFN10_2x3mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN16': Params( # 3x3mm, 0.5 pitch, 16 pins, 1.0mm height  QFN16 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (1.7,1.7), # e Pad #epad = None, # e Pad
        modelName = 'QFN16_3x3mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN24': Params( # 4.15x4.15mm, 0.5 pitch, 24 pins, 1.0mm height  QFN24 p05 texas
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.15,       # body overall length
        E = 4.15,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = (2.45,2.45), # e Pad #epad = None, # e Pad
        modelName = 'QFN24_415x415mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN28': Params( # 6x6mm, 0.65 pitch, 28 pins, 0.9mm height QFN28 Microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 6,       # body overall length
        E = 6,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.38,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 7,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (3.7,3.7), # e Pad #epad = None, # e Pad
        modelName = 'QFN28_6x6mm_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN32': Params( # 5x5mm, 0.5 pitch, 32 pins, 1.0mm height  QFN32 p05 ATMEL
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.3,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 8,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = (3.6,3.6), # e Pad #epad = None, # e Pad
        modelName = 'QFN32_5x5mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN40': Params( # 6x6mm, 0.5 pitch, 40 pins, 1.0mm height  QFN44 p005
        #datasheet example - http://www.ti.com/lit/ds/symlink/drv8308.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        epad = (3.52,2.62), # e Pad #epad = None, # e Pad
        modelName = 'QFN40_6x6mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN44': Params( # 8x8mm, 0.65 pitch, 44 pins, 1.0mm height  QFN44 p065 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (6.45,6.45), # e Pad #epad = None, # e Pad
        modelName = 'QFN44_8x8mm_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN64': Params( # 9x9mm, 0.5 pitch, 64 pins, 0.9mm height  QFN64 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
        D = 9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.88,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (4.7,4.7), # e Pad #epad = None, # e Pad
        modelName = 'QFN64_9x9mm_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
}
