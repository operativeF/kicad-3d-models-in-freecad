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

destination_dir="/generated_cap/"
# destination_dir="./"

# body color
#case_color=(244,164,96,0) # SandyBrown
#case_color=(255, 243, 128,0) # Corn Yellow
#case_color=(227,245,84,0)
case_color = (50, 50, 50)
#pins_color = (230, 230, 230)
pins_color = (205,205,192)
mark_color = (255,255,255) #white
#mark_color = (255,250,250) #snow
#mark_color = (255,255,240) #ivory
#mark_color = (207, 83, 0 ,0) #ghost white
#mark_color = (207, 83, 0 ,0) #rusty orange
#max_cc1 = 1     # maximum size for 1st pin corner chamfer


# Mold angle (degrees) (not specified in datasheet)
ma_deg = 8

Params = namedtuple("Params", [
    'L',    # body overall length (including terminals)
    'W',    # body overall width
    'H',    # body overall height
    'F',    # width of each termination
    'S',    # length of each termination
    'B',    # beveling, measured as horizontal distance from end of cap
    'P',    # height off PCB where cutout begins (anode)
    'R',    # width of cutout (anode)
    'T',    # thickness of termination metal
    'G',    # length of bump underneath body
    'E',    # width of the bump underneath body
    'pml',  # pin mark length
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_poly_tantalum = {
    'A_3216_18': Params( # kemet Polymer Tantalum A 3216 H18
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 3.4,
        W = 1.8,
        H = 1.8,
        F = 1.2,
        S = 0.8,
        B = 0.4,
        P = 0.4,
        R = 0.4,
        T = 0.13,
        G = 1.1,
        E = 1.3,
        pml = 0.6,
        modelName = 'Poly_Polymer_Tantalum_A_3216H18', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'B_3528_21': Params( # kemet Polymer Tantalum B 3528 H21
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 3.7,
        W = 3.0,
        H = 2.1,
        F = 2.2,
        S = 0.8,
        B = 0.4,
        P = 0.5,
        R = 1.0,
        T = 0.13,
        G = 1.1,
        E = 2.3,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_B_3528H21', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'C_6032_28': Params( # kemet Polymer Tantalum C 6032 H28
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 6.3,
        W = 3.5,
        H = 2.8,
        F = 2.2,
        S = 1.3,
        B = 0.5,
        P = 0.9,
        R = 1.0,
        T = 0.13,
        G = 2.8,
        E = 2.4,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_C_6032H28', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'D_7343_31': Params( # kemet Polymer Tantalum D 7343 H31
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 3.1,
        F = 2.4,
        S = 1.3,
        B = 0.5,
        P = 0.9,
        R = 1.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_D_7343H31', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'H_7360_20': Params( # kemet Polymer Tantalum H 7360 H20
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 6.3,
        H = 2.0,
        F = 4.1,
        S = 1.3,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.13,
        G = 3.5,
        E = 4.1,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_H_7360H20', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'I_3216_10': Params( # kemet Polymer Tantalum I 3216 H10
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 3.4,
        W = 1.8,
        H = 1.0,
        F = 1.2,
        S = 1.0,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.02,
        G = 1.1,
        E = 1.3,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_I_3216H10', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
		),
    'L_6032_19': Params( # kemet Polymer Tantalum W 6032 H19
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 6.3,
        W = 3.4,
        H = 1.9,
        F = 2.2,
        S = 1.3,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.13,
        G = 2.8,
        E = 2.4,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_L_6032H19', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'M_3528_15': Params( # kemet Polymer Tantalum M 3528 H15
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 3.7,
        W = 3.0,
        H = 1.5,
        F = 2.2,
        S = 0.8,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.13,
        G = 1.3,
        E = 2.3,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_M_3258H15', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'P_2012_10': Params( # kemet Polymer Tantalum P 2012 H10
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 2.1,
        W = 1.35,
        H = 1.0,
        F = 1.0,
        S = 0.65,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.02,
        G = 0.4,
        E = 0.4,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_P_2012H10', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'Q_7343_12': Params( # kemet Polymer Tantalum Q 7343 H12
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 1.2,
        F = 2.4,
        S = 1.3,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_Q_7343H12', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'T_3528_12': Params( # kemet Polymer Tantalum T 3528 H12
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 3.7,
        W = 3.0,
        H = 1.2,
        F = 2.2,
        S = 0.8,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.13,
        G = 1.1,
        E = 2.3,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_T_3528H12', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'U_6032_15': Params( # kemet Polymer Tantalum U 6032 H15
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 6.3,
        W = 3.5,
        H = 1.5,
        F = 2.2,
        S = 1.3,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.13,
        G = 2.8,
        E = 2.4,
        pml = 0.6,
        modelName = 'Polymer_Tantalum_U_6032H15', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'V_7343_19': Params( # kemet Polymer Tantalum V 7343 H19
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 1.9,
        F = 2.4,
        S = 1.3,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_V_7343H19', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'W_7343_15': Params( # kemet Polymer Tantalum W 7343 H15
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 1.5,
        F = 2.4,
        S = 1.3,
        B = 0.5,
        P = 0.0, # No beveling
        R = 0.0, # No notching
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_W_7343H15', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'X_7343_43': Params( # kemet Polymer Tantalum X 7343 H43
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 4.3,
        F = 2.4,
        S = 1.3,
        B = 0.5,
        P = 1.7,
        R = 1.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_X_7343H17', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'Y_7343_40': Params( # kemet Polymer Tantalum Y 7343 H40
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 4.0,
        F = 2.4,
        S = 1.3,
        B = 0.5,
        P = 1.7,
        R = 1.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_Y_7343H40', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
    'Z_7343_17': Params( # kemet Polymer Tantalum Z 7343 H17
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/641/KEM_T2076_T52X-530.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 1.7,
        F = 3.0,
        S = 1.3,
        B = 0.0, # No beveling
        P = 0.0, # No notching
        R = 0.0,
        T = 0.02,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Polymer_Tantalum_Z_7343H17', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_poly_tantalum'
        ),
}