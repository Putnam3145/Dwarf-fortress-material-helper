__author__ = 'Putnam'

import math,json

class Material:
    def __init__(self,dict):
        self.name=dict['name']
        self.young_modulus=dict["young's modulus"]
        self.bulk_modulus=dict["bulk modulus"]
        self.shear_modulus=dict["shear modulus"]
        self.tensile_yield=int(dict['ultimate tensile strength']*1000)
        self.tensile_elasticity=self.get_elasticity(self.young_modulus,'young')
        self.compressive_elasticity=self.get_elasticity(self.bulk_modulus,'bulk')
        self.shear_elasticity=self.get_elasticity(self.shear_modulus)
        self.spec_heat=int(dict['spec heat']*1000)
        self.melting_point=self.uristize(dict['melting point'])
        self.boiling_point=self.uristize(dict['boiling point'])
        self.color=dict['color']
        self.value=dict['value']
        self.solid_density=int(dict['solid density']*1000)
        self.liquid_density=int(dict['liquid density']*1000)
        self.molar_mass=int(dict['molar mass']*1000)
    def get_elasticity(self,num,type='shear'):
        if type=='young':
            return int((self.tensile_yield)/(self.young_modulus*10)) # Ratio in constant multiplicands entirely based on arbitrary DF stuff 
        elif type=='bulk':
            return int((self.tensile_yield*3.5)/(self.bulk_modulus*10))
        else:
            return int((self.tensile_yield)/(self.shear_modulus*10))
    def uristize(self,temp):
        return temp+9968
    def temp_name(self,state):
        if state=='solid':
            if self.melting_point<10032:
                return 'frozen ' + self.name
            else:
                return self.name
        elif state=='liquid':
            if self.melting_point>10032:
                return 'molten ' + self.name
            else:
                return self.name
        else:
            if self.boiling_point<10032:
                return self.name
            else:
                return 'boiling ' + self.name
    def color_string(self):
        return "0:7:1" #probably something better later
    def rawify(self):
        return ("[INORGANIC:"+self.name.upper()+"]\n"
                "    [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE\n"
                "    [STATE_NAME_ADJ:ALL_SOLID:"+self.temp_name('solid')+"]\n"
                "    [STATE_NAME_ADJ:LIQUID:"+self.temp_name('liquid')+"]\n"
                "    [STATE_NAME_ADJ:GAS:"+self.temp_name('gas')+"]\n"
                "    [DISPLAY_COLOR:"+self.color_string()+"]\n"
                "    [BUILD_COLOR:"+self.color_string()+"]\n"
                "    [MATERIAL_VALUE:"+str(self.value)+"]\n"
                "    [SPEC_HEAT:"+str(self.spec_heat)+"]\n"
                "    [MELTING_POINT:"+str(self.melting_point)+"]\n"
                "    [BOILING_POINT:"+str(self.boiling_point)+"]\n"
                "    [SOLID_DENSITY:"+str(self.solid_density)+"]\n"
                "    [LIQUID_DENSITY:"+str(self.liquid_density)+"]\n"
                "    [MOLAR_MASS:"+str(self.molar_mass)+"]\n"
                "    [IMPACT_YIELD:"+str(int(self.tensile_yield*3.5))+"]\n"
	            "    [IMPACT_FRACTURE:"+str(self.tensile_yield*7)+"]\n"
	            "    [IMPACT_STRAIN_AT_YIELD:"+str(self.compressive_elasticity)+"]\n"
	            "    [COMPRESSIVE_YIELD:"+str(int(self.tensile_yield*3.5))+"]\n"
	            "    [COMPRESSIVE_FRACTURE:"+str(self.tensile_yield*7)+"]\n"
	            "    [COMPRESSIVE_STRAIN_AT_YIELD:"+str(self.compressive_elasticity)+"] bulk modulus "+ str(self.bulk_modulus) + " GPa\n"
	            "    [TENSILE_YIELD:"+str(self.tensile_yield)+"]\n"
	            "    [TENSILE_FRACTURE:"+str(self.tensile_yield*2)+"]\n"
	            "    [TENSILE_STRAIN_AT_YIELD:"+str(self.tensile_elasticity)+"] young's modulus "+ str(self.young_modulus) + " GPa\n"
	            "    [TORSION_YIELD:"+str(self.tensile_yield)+"]\n"
	            "    [TORSION_FRACTURE:"+str(self.tensile_yield*2)+"]\n"
                "    [TORSION_STRAIN_AT_YIELD:"+str(self.tensile_elasticity)+"]\n"
	            "    [SHEAR_YIELD:"+str(self.tensile_yield)+"]\n"
	            "    [SHEAR_FRACTURE:"+str(self.tensile_yield*2)+"]\n"
	            "    [SHEAR_STRAIN_AT_YIELD:"+str(self.shear_elasticity)+"] shear modulus " +str(self.shear_modulus)+ " GPa\n"
	            "    [BENDING_YIELD:"+str(self.tensile_yield)+"]\n"
	            "    [BENDING_FRACTURE:"+str(self.tensile_yield*2)+"]\n"
	            "    [BENDING_STRAIN_AT_YIELD:"+str(self.shear_elasticity)+"]\n"
	            "    [MAX_EDGE:10000]\n"
                "    [STATE_COLOR:ALL:"+self.color+"]")
				
def decode_json_file(json_file_name):
    json_file = open(json_file_name,'r')
    return json.load(json_file)

JSONMats = decode_json_file('mats.json')

output=open('materials.txt','a')

for mat in JSONMats:
        output.write(Material(JSONMats[mat]).rawify()+'\n\n')
