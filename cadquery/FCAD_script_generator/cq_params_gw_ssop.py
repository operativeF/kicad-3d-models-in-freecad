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


all_params_ssop = {
    'SSOP_8': Params( # 3.15x4.25, pitch 0.65mm 8pin 2.0mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 3.15,       # body length
        E1 = 2.90,       # body width
        E = 4.25,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.001,  # body-board separation
        A2 = 1.30,  # body height
        b = 0.30,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = None,
        modelName = 'SSOP_8_315x425mm_pad_065mmPitch', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP_16': Params( # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 6.20,       # body length
        E1 = 5.30,       # body width
        E = 7.80,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.05,  # body-board separation
        A2 = 1.75,  # body height
        b = 0.30,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = None,
        modelName = 'SSOP_14_56x72mm_065mmPitch', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'ssop'
        ),
    'SSOP_20': Params( # 5.3x7.2, pitch 0.65 20pin 2.0mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.75,  # body height
        b = 0.30,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'SSOP_20_53x72mm_065mmPitch', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'ssop'
        ),
    'SSOP_24': Params( # 5.3x7.2, pitch 0.65 20pin 2.0mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 8.20,       # body length
        E1 = 5.30,       # body width
        E = 7.80,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.05,  # body-board separation
        A2 = 1.75,  # body height
        b = 0.30,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = None,
        modelName = 'SSOP_24_105x76mm_065mmPitch', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'ssop'
        ),
    'SSOP_28': Params( # 5.6x11.0, pitch 0.50 44pin 1.15mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.20,       # body length
        E1 = 5.30,       # body width
        E = 7.80,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.05,  # body-board separation
        A2 = 2.00,  # body height
        b = 0.30,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = None,
        modelName = 'SSOP_28_110xmm_065mmPitch', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'ssop'
        ),
}