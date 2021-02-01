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

        
line_type("#1029")
