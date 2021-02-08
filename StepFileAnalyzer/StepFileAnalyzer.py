import sys, io, argparse, re
from steputils import p21
import numpy as np 


argumentos = argparse.ArgumentParser(
    formatter_class=argparse.MetavarTypeHelpFormatter,
    description="Features recognition of the step files",
    )
argumentos.add_argument("-f", "--file", required=True, help="path of the input step file")
args = vars(argumentos.parse_args())
arquivo = args["file"]

def circle_type(identifier): # identifier = "#id"
    
    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        line = str(arquivoStep.__getitem__(identifier))
        values = line[line.find('(')+1:-3].split(',')
        
        # name = values[0]
        AXIS2_PLACEMENT_3D = values[1]
        RADIUS = values[2]
        
        # Finds axis2_placement_3d line
        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        # name = values[0]
        LOCATION, Z_AXIS, X_AXIS = values[1], values[2], values[3]

        # Finds location value
        LOCATION_LINE = str(arquivoStep.__getitem__(LOCATION))
        values = LOCATION_LINE[LOCATION_LINE.find('(')+1:-4].split(',(')
        
        # name = values[0]
        LOCATION = values[1].split(',')
        
        # Finds axis values
        AXIS_LINE = str(arquivoStep.__getitem__(Z_AXIS))
        values = AXIS_LINE[AXIS_LINE.find('(')+1:-4].split(',(') 

        # name = values[0]
        Z_AXIS = values[1].split(',')
        
        AXIS_LINE = str(arquivoStep.__getitem__(X_AXIS))
        values = AXIS_LINE[AXIS_LINE.find('(')+1:-4].split(',(')

        # name = values[0]
        X_AXIS = values[1].split(',')

        features = {
            "location: ":LOCATION,
            "radius: ":RADIUS,
            "sharp: ":"?",
            "type: ":"Circle",
            "vert_indices: ":"?",
            "vert_parameters: ":"?",
            "x_axis: ":X_AXIS,
            "y_axis: ":"?",
            "z_axis: ":Z_AXIS,
        }
        
        for item, value in features.items():
            print(item, value)
                   

def cylinder_type(identifier): # identifier = "#id"

    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        # Finds cylinder line
        line = str(arquivoStep.__getitem__(identifier))
        values = line[line.find('(')+1:-3].split(',')
        
        # name = values[0]
        AXIS2_PLACEMENT_3D = values[1]
        RADIUS = values[2]

        # Finds axis2_placement_3d line
        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')

        # name = values[0]
        LOCATION, Z_AXIS, X_AXIS = values[1], values[2], values[3]

        # Finds location value
        LOCATION_LINE = str(arquivoStep.__getitem__(LOCATION))
        values = LOCATION_LINE[LOCATION_LINE.find('(')+1:-4].split(',(')

        # name = values[0]
        LOCATION = values[1].split(',')
        
        # Finds axis values
        AXIS_LINE = str(arquivoStep.__getitem__(Z_AXIS))
        values = AXIS_LINE[AXIS_LINE.find('(')+1:-4].split(',(') # Z axis
        
        # name = values[0]
        Z_AXIS = values[1].split(',')
        
        AXIS_LINE = str(arquivoStep.__getitem__(X_AXIS))
        values = AXIS_LINE[AXIS_LINE.find('(')+1:-4].split(',(')

        # name = values[0]
        X_AXIS = values[1].split(',')
        
        features = {
            "coefficients: ":"?",
            "face_indices: ":"?",
            "location: ":LOCATION,
            "radius: ":RADIUS,
            "type: ":"Cylinder",
            "vert_indices: ":"?",
            "vert_parameters: ":"?",
            "x_axis: ":X_AXIS,
            "y_axis: ":"?",
            "z_axis: ":Z_AXIS,
        }

        for item,value in features.items():
            print(item, value)
        
def line_type(identifier): # identifier = "#id"

    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        line = str(arquivoStep.__getitem__(identifier))
        values = line[line.find('(')+1:-3].split(',')
        
        # name = values[0]
        CARTESIAN_POINT, VECTOR = values[1], values[2]
        
        # Finds cartesian_point line
        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        values = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find('(')+1:-4].split(',(')
        
        # name = values[0]
        LOCATION = values[1].split(',')
        
        # Finds vector line
        VECTOR_LINE = str(arquivoStep.__getitem__(VECTOR))
        values = VECTOR_LINE[VECTOR_LINE.find('(')+1:-4].split(',')
        
        # name = values[0]
        DIRECTION = values[1]

        # Finds direction line
        DIRECTION_LINE = str(arquivoStep.__getitem__(DIRECTION))
        values = DIRECTION_LINE[DIRECTION_LINE.find('(')+1:-4].split(',(')

        # name = values[0]
        DIRECTION = values[1].split(',')
        
        features = {
            "direction: ":DIRECTION,
            "location: ":LOCATION,
            "sharp: ":"?",
            "type: ":"Line",
            "vert_indices: ":"?",
            "vert_parameters: ":"?",
        }

        for item, value in features.items():
            print(item, value)

def plane_type(identifier): # identifier = "#id"

    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        line = str(arquivoStep.__getitem__(identifier))
        values = line[line.find('(')+1:-3].split(',')
        
        # name = values[0]
        AXIS2_PLACEMENT_3D = values[1]

        # Finds axis2_placement_3d line
        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        # name = values[0]
        CARTESIAN_POINT, DIRECTION_1, DIRECTION_2 = values[1], values[2], values[3]
        
        # Finds cartesian_point line
        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        values = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find('(')+1:-4].split(',(')
        
        # name = values[0]
        LOCATION = values[1].split(',')
        
        # Finds direction_1 line
        DIRECTION_1_LINE = str(arquivoStep.__getitem__(DIRECTION_1))
        values = DIRECTION_1_LINE[DIRECTION_1_LINE.find('(')+1:-4].split(',(')
        
        # name = values[0]
        Z_AXIS = values[1].split(',')
        
        # Finds direction_2 line
        DIRECTION_2_LINE = str(arquivoStep.__getitem__(DIRECTION_2))
        values = DIRECTION_2_LINE[DIRECTION_2_LINE.find('(')+1:-4].split(',(')
        
        # name = values[0]
        X_AXIS = values[1].split(',')
        
        features = {
            "coefficients: ":"?",
            "face_indices: ":"?",
            "location: ":LOCATION,
            "type: ":"Plane",
            "vert_indices: ":"?",
            "vert_parameters: ":"?",
            "x_axis: ":X_AXIS,
            "y_axis: ":"?",
            "z_axis: ":Z_AXIS,
        }

        for item, value in features.items():
            print(item, value)


def main():

    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        line_one = str(arquivoStep.__getitem__("#1"))
        values = line_one[line_one.find('(')+1:-3].split(',(')
        values = values[1].split('),')
        
        STYLED_ITEMS = values[0].split(',')

        count_plane = 1
        count_cylinder = 1
        count_circle = 1
        count_line = 1
        for items in STYLED_ITEMS: # percorre os ids de faces
            
            line = str(arquivoStep.__getitem__(items))
            values = line[line.find('(')+1:-3].split(',')
            
            ADVANCED_FACE = values[2]

            ADVANCED_FACE_LINE = str(arquivoStep.__getitem__(ADVANCED_FACE))
            values = ADVANCED_FACE_LINE[ADVANCED_FACE_LINE.find('(')+1:-3].split(',')
            
            FACE_OUTER_BOUND = values[1].replace("(","").replace(")","")
            SURFACE_TYPE = values[2]
            
            # Curves
            
            FACE_OUTER_BOUND_LINE = str(arquivoStep.__getitem__(FACE_OUTER_BOUND))
            values = FACE_OUTER_BOUND_LINE[FACE_OUTER_BOUND_LINE.find('(')+1:-3].split(',')
            
            EDGE_LOOP = values[1]
            EDGE_LOOP_LINE = str(arquivoStep.__getitem__(EDGE_LOOP))
            values = EDGE_LOOP_LINE[EDGE_LOOP_LINE.find('(')+1:-3].split(',')
            
            ORIENTED_EDGES = values[1:5] 

            for EDGE_CURVE in ORIENTED_EDGES:
                ORIENTED_EDGES_LINE = str(arquivoStep.__getitem__(EDGE_CURVE.replace('(','').replace(')','')))
                values = ORIENTED_EDGES_LINE[ORIENTED_EDGES_LINE.find('(')+1:-3].split(',')
                
                EDGE_CURVE = values[3]
                EDGE_CURVE_LINE = str(arquivoStep.__getitem__(EDGE_CURVE))
                values = EDGE_CURVE_LINE[EDGE_CURVE_LINE.find('(')+1:-3].split(',')

                START_POINT = values[1]
                END_POINT = values[2]
                CURVE_TYPE = values[3]

                CURVE_LINE = str(arquivoStep.__getitem__(CURVE_TYPE))
                
                if 'CIRCLE' in CURVE_LINE:
                    print(f'\n------------------CIRCULO {count_circle}----------------')
                    count_circle+=1
                    circle_type(CURVE_TYPE)
                
                if 'LINE' in CURVE_LINE:
                    print(f'\n------------------LINHA {count_line}----------------')
                    count_line+=1
                    line_type(CURVE_TYPE)
        
            
            SURFACE_LINE = str(arquivoStep.__getitem__(SURFACE_TYPE))

            # Surfaces - *Conical and Toroidal

            if 'CYLINDRICAL' in SURFACE_LINE:
                print(f'\n------------------CILINDRO {count_cylinder}----------------')
                count_cylinder+=1
                cylinder_type(SURFACE_TYPE)
            
            if 'PLANE' in SURFACE_LINE:
                print(f'\n------------------PLANO {count_plane}----------------')
                count_plane+=1
                plane_type(SURFACE_TYPE)


            

main()