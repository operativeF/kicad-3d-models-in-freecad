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
import cq_params_gw_soic  # modules parameters
from cq_params_gw_soic import *


# destination_dir="./generated_gw/"
# destination_dir="./"
# case_color = (0.1, 0.1, 0.1)
# pins_color = (0.9, 0.9, 0.9)


all_params_tssop = {
    'TSSOP_8': Params( # 3.0x4.4, pitch 0.65 8pin 1.1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 3.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_8_3x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_14': Params( # 5.0x4.4, pitch 0.65 14pin 1.1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 7,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_14_5x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_16': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_16_5x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_16_EP_1_3x3mm': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = [3.0, 3.0], # e Pad
        modelName = 'TSSOP_16_EP_1_3x3mm_5x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_20_EP_1_3x42mm': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 6.5,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = [4.2, 3.0], # e Pad
        modelName = 'TSSOP_20_EP_1_3x42mm_5x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_20': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 6.5,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_20_65x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_24': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.8,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_24_78x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_24_EP_1_32x5mm': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.8,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = [5.00, 3.20], # e Pad
        modelName = 'TSSOP_24_EP_1_32x5mm_78x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_28': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_28_97x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_28_W': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.7,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_28_W_97x61mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_28_EP_1_3x35mm': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = [3.5, 3.0], # e Pad
        modelName = 'TSSOP_28_EP_1_3x35mm_97x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_28_EP_1_3x55mm': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = [5.5, 3.0], # e Pad
        modelName = 'TSSOP_28_EP_1_3x55mm_97x44mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_38': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 17,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_38_97x44mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_48_W': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.5,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 24,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_48_W_125x61mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
    'TSSOP_100': Params( # 20.80x8.10, pitch 0.40 100pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.80,       # body length
        E1 = 6.10,       # body width
        E = 8.20,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.20,  # body height
        b = 0.18,  # pin width
        e = 0.40,  # pin (center-to-center) distance
        npx = 50,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TSSOP_100_208x81mm_Pitch040mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'TSSOP'
        ),
}

