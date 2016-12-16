
from collections import namedtuple
import cq_params_gw_soic  # modules parameters
from cq_params_gw_soic import *

# destination_dir="./generated_gw/"
# destination_dir="./"
# case_color = (0.1, 0.1, 0.1)
# pins_color = (0.9, 0.9, 0.9)

all_params_msop = {
    'MSOP_8': Params( # 3x3mm, pitch 0.65mm 8pin 2.0mm height
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
        D1 = 3.00,       # body length
        E1 = 3.00,       # body width
        E = 4.90,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.33,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = None,
        modelName = 'MSOP_8_3x3_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'MSOP'
        ),
    'MSOP_8_1EP': Params( # 3x3mm, epad 2.16x1.73mm, pitch 0.65mm 8pin 2.0mm height
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
        D1 = 3.00,       # body length
        E1 = 3.00,       # body width
        E = 4.90,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.33,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = [2.16, 1.73],
        modelName = 'MSOP_8_1EP_2d16x1d73_3x3_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'MSOP'
        ),
    'MSOP_10': Params( # 3x3mm, pitch 0.5mm 10pin 2.0mm height
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
        D1 = 3.00,       # body length
        E1 = 3.00,       # body width
        E = 4.90,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.23,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 5,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = None,
        modelName = 'MSOP_10_3x3_p05', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP_10_1EP': Params( # 3x3mm, epad 2.17x1.73mm, pitch 0.5mm 10pin 2.0mm height
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
        D1 = 3.00,       # body length
        E1 = 3.00,       # body width
        E = 4.90,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.10,  # body height
        b = 0.25,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        npx = 5,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
		epad = [2.17, 1.73],
        modelName = 'MSOP_10_1EP_2d17x1d73_3x3_p05', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
}