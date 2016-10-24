# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Analog Devices (follows JEDEC standards)

## file of parametric definitions

from collections import namedtuple
import cq_params_gw_soic  # modules parameters
from cq_params_gw_soic import *


# destination_dir="./generated_gw/"
# destination_dir="./"
# case_color = (0.1, 0.1, 0.1)
# pins_color = (0.9, 0.9, 0.9)

all_params_lqfp = {
    'BBA': Params( # 7x7, pitch 0.80 32pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.37,  # pin width
        e = 0.80,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 8,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_32_7x7mm_Pitch08mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BBC': Params( # 7x7, pitch 0.50 48pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 12,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_48_7x7mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BBD': Params( # 7x7, pitch 0.40 64pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.40,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 16,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_64_7x7mm_Pitch04mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BCB': Params( # 10x10, pitch 0.80 44pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.37,  # pin width
        e = 0.80,  # pin (center-to-center) distance
        npx = 11,   # number of pins along X axis (width)
        npy = 11,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_44_10x10mm_Pitch08mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BCC': Params( # 10x10, pitch 0.65 52pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,   # number of pins along X axis (width)
        npy = 13,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_52_10x10mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BCD': Params( # 10x10, pitch 0.50 64pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 16,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_64_10x10mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BDD': Params( # 12x12, pitch 0.50 80pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 14.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 20,   # number of pins along X axis (width)
        npy = 20,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_80_12x12mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BEA': Params( # 14x14, pitch 1.00 44pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.42,  # pin width
        e = 1.00,  # pin (center-to-center) distance
        npx = 11,   # number of pins along X axis (width)
        npy = 11,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_44_14x14mm_Pitch1mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BEB': Params( # 14x14, pitch 0.80 64pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.37,  # pin width
        e = 0.80,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 16,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_64_14x14mm_Pitch08mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BEC': Params( # 14x14, pitch 0.65 80pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 20,   # number of pins along X axis (width)
        npy = 20,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_80_14x14mm_Pitch065mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BED': Params( # 12x12, pitch 0.5 100pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 25,   # number of pins along X axis (width)
        npy = 25,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_100_12x12mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BEE': Params( # 14x14, pitch 0.4 120pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.40,  # pin (center-to-center) distance
        npx = 30,   # number of pins along X axis (width)
        npy = 30,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_120_14x14mm_Pitch04mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BHB': Params( # 14x20, pitch 0.5 128pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 14.0,       # body width
        E = 16.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 38,   # number of pins along X axis (width)
        npy = 25,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_128_14x20mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BFB': Params( # 20x20, pitch 0.5 144pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 36,   # number of pins along X axis (width)
        npy = 36,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_144_20x20mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'BGA': Params( # 24x24, pitch 0.5 176pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 24.0,       # body length
        E1 = 24.0,       # body width
        E = 26.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 44,   # number of pins along X axis (width)
        npy = 44,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_176_24x24mm_Pitch05mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-128': Params( # 14x14, pitch 0.4 128pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.40,  # pin (center-to-center) distance
        npx = 32,   # number of pins along X axis (width)
        npy = 32,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_128_14x14mm_Pitch04mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
    'LQFP-184': Params( # 20x20, pitch 0.4 184pin 1.4mm height
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
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.00,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.40,  # pin (center-to-center) distance
        npx = 46,   # number of pins along X axis (width)
        npy = 46,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP_184_20x20mm_Pitch04mm', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'lqfp'
        ),
}