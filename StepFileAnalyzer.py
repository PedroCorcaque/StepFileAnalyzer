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

def y_axis_function(z_axis, x_axis):
    return np.cross(z_axis,x_axis)

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

        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        Y_AXIS = y_axis_function(Z_AXIS, X_AXIS)

        features = {
            "location: ":LOCATION,
            "radius: ":RADIUS,
            "sharp: ":"?",
            "type: ":"Circle",
            "vert_indices: ":"?",
            "vert_parameters: ":"?",
            "x_axis: ":X_AXIS,
            "y_axis: ":Y_AXIS,
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
        
        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        Y_AXIS = y_axis_function(Z_AXIS, X_AXIS)

        features = {
            "coefficients: ":"?",
            "face_indices: ":"?",
            "location: ":LOCATION,
            "radius: ":RADIUS,
            "type: ":"Cylinder",
            "vert_indices: ":"?",
            "vert_parameters: ":"?",
            "x_axis: ":X_AXIS,
            "y_axis: ":Y_AXIS,
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
        
        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        Y_AXIS = y_axis_function(Z_AXIS, X_AXIS)

        features = {
            "coefficients: ":"?",
            "face_indices: ":"?",
            "location: ":LOCATION,
            "type: ":"Plane",
            "vert_indices: ":"?",
            "vert_parameters: ":"?",
            "x_axis: ":X_AXIS,
            "y_axis: ":Y_AXIS,
            "z_axis: ":Z_AXIS,
        }

        for item, value in features.items():
            print(item, value)

def cone_type(identifier):
    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        line = str(arquivoStep.__getitem__(identifier))
        values = line[line.find('(')+1:-3].split(',')
        
        AXIS2_PLACEMENT_3D = values[1]
        RADIUS = values[2]
        ANGLE = values[3]

        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        CARTESIAN_POINT = values[1]
        DIRECTION_1 = values[2]
        DIRECTION_2 = values[3]

        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        values = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find('(')+1:-3].split(',(')
        LOCATION = values[1].replace(')','')

        DIRECTION_1_LINE = str(arquivoStep.__getitem__(DIRECTION_1))
        values = DIRECTION_1_LINE[DIRECTION_1_LINE.find('(')+1:-3].split(',(')
        Z_AXIS = values[1].replace(')','').split(',')

        DIRECTION_2_LINE = str(arquivoStep.__getitem__(DIRECTION_2))
        values = DIRECTION_2_LINE[DIRECTION_2_LINE.find('(')+1:-3].split(',(')
        X_AXIS = values[1].replace(')','').split(',')

        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        Y_AXIS = y_axis_function(Z_AXIS, X_AXIS)

        features = {
            'angle: ': ANGLE,
            'apex: ': "?",
            'coefficients: ': "?",
            'face_indices: ': "?",
            'location: ': LOCATION,
            'radius: ': RADIUS,
            'type: ': 'Cone',
            'vert_indices: ': "?",
            'vert_parameters: ': "?",
            'x_axis: ': X_AXIS,
            'y_axis: ': Y_AXIS,
            'z_axis: ': Z_AXIS,
        }

        for item,valor in features.items():
            print(item, valor)

def toroidal_surface(identifier):
    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        line = str(arquivoStep.__getitem__(identifier))
        values = line[line.find('(')+1:-3].split(',')
        
        AXIS2_PLACEMENT_3D = values[1]
        MAX_RADIUS = values[2]
        MIN_RADIUS = values[3]
        
        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        CARTESIAN_POINT = values[1]
        DIRECTION_1 = values[2]
        DIRECTION_2 = values[3]

        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        values = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find(',(')+1:-3].split(',')
        LOCATION = values

        DIRECTION_1_LINE = str(arquivoStep.__getitem__(DIRECTION_1))
        values = DIRECTION_1_LINE[DIRECTION_1_LINE.find('(')+1:-4].split(',(')
        Z_AXIS = values[1].split(',')

        DIRECTION_2_LINE = str(arquivoStep.__getitem__(DIRECTION_2))
        values = DIRECTION_2_LINE[DIRECTION_2_LINE.find('(')+1:-4].split(',(')
        X_AXIS = values[1].split(',')

        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        Y_AXIS = y_axis_function(Z_AXIS, X_AXIS)
        
        features = {
            "face_indices: ": "?",
            "location: ": LOCATION,
            "max_radius: ": MAX_RADIUS,
            "min_radius: ": MIN_RADIUS,
            "type: ": "Torus",
            "vert_indices: ": "?",
            "vert_parameters: ": "?",
            "x_axis: ": X_AXIS,
            "y_axis: ": Y_AXIS,
            "z_axis: ": Z_AXIS,
        }

        for item,value in features.items():
            print(item,value)       

def spherical_surface(identifier):
    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        line = str(arquivoStep.__getitem__(identifier))
        values = line[line.find('(')+1:-3].split(',')
        
        AXIS2_PLACEMENT_3D = values[1]
        RADIUS = values[2]

        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        CARTESIAN_POINT = values[1]
        DIRECTION_1 = values[2]
        DIRECTION_2 = values[3]

        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        LOCATION = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find(',(')+1:-3].split(',')
        
        DIRECTION_1_LINE = str(arquivoStep.__getitem__(DIRECTION_1))
        Z_AXIS = DIRECTION_1_LINE[DIRECTION_1_LINE.find('(')+1:-4].split(',(')
        Z_AXIS = Z_AXIS[1].split(',')

        DIRECTION_2_LINE = str(arquivoStep.__getitem__(DIRECTION_2))
        X_AXIS = DIRECTION_2_LINE[DIRECTION_2_LINE.find('(')+1:-4].split(',(')
        X_AXIS = X_AXIS[1].split(',')

        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        Y_AXIS = y_axis_function(Z_AXIS, X_AXIS)

        features = {
            "coefficients: ": "?",
            "face_indices: ": "?",
            "location: ": LOCATION,
            "radius: ": RADIUS,
            "vert_indices: ": "?",
            "vert_parameters: ": "?",
            "x_axis: ": X_AXIS,
            "y_axis: ": Y_AXIS,
            "z_axis: ": Z_AXIS, 
        }

        for item,value in features.items():
            print(item,value)

