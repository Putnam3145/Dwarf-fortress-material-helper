This is a program that takes json raws with real-life data values and outputs them into DF values. Here's an example file, commented:

{
	"Lithium": {
		"name": "Lithium",
		"young's modulus": 4.9, # This is in GPa
		"bulk modulus": 11,
		"shear modulus": 4.2,
		"ultimate tensile strength": 15, # In MPa
		"spec heat": 3.560, # Joules per grams*Celsius
		"melting point": 357, #fahrenheit
		"boiling point": 2447,
		"color": "GRAY", #DF colors, must be uppercase
		"value": 1,
		"solid density": 0.534, #g/ml
		"liquid density": 0.512,
		"molar mass": 6.941 #g/mole
	}
}

Without comments, that json outputs these raws:

[INORGANIC:LITHIUM]
    [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE
    [STATE_NAME_ADJ:ALL_SOLID:lithium]
    [STATE_NAME_ADJ:LIQUID:molten lithium]
    [STATE_NAME_ADJ:GAS:boiling lithium]
    [DISPLAY_COLOR:0:7:1]
    [BUILD_COLOR:0:7:1]
    [MATERIAL_VALUE:1]
    [SPEC_HEAT:3560.0]
    [MELTING_POINT:10325]
    [BOILING_POINT:12415]
    [SOLID_DENSITY:534]
    [LIQUID_DENSITY:512]
    [MOLAR_MASS:6941]
    [IMPACT_YIELD:52500]
    [IMPACT_FRACTURE:105000]
    [IMPACT_STRAIN_AT_YIELD:4930]
    [COMPRESSIVE_YIELD:52500]
    [COMPRESSIVE_FRACTURE:105000]
    [COMPRESSIVE_STRAIN_AT_YIELD:4930] bulk modulus 11 GPa
    [TENSILE_YIELD:15000]
    [TENSILE_FRACTURE:30000]
    [TENSILE_STRAIN_AT_YIELD:3143] young's modulus 4.9 GPa
    [TORSION_YIELD:15000]
    [TORSION_FRACTURE:30000]
    [TORSION_STRAIN_AT_YIELD:3143]
    [SHEAR_YIELD:15000]
    [SHEAR_FRACTURE:30000]
    [SHEAR_STRAIN_AT_YIELD:3690] shear modulus 4.2 GPa
    [BENDING_YIELD:15000]
    [BENDING_FRACTURE:30000]
    [BENDING_STRAIN_AT_YIELD:3690]
    [MAX_EDGE:10000]
    [STATE_COLOR:ALL:GRAY]

