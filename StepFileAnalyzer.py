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
        RADIUS = float(values[2])*1000
        
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
        LOCATION = [float(i)*1000 for i in LOCATION]
        
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
        Z_AXIS = np.array(Z_AXIS) # type numpy.ndarray
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        X_AXIS = np.array(X_AXIS) # type numpy.ndarray
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
        RADIUS = float(values[2])*1000 # type float 

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
        LOCATION = [float(i)*1000 for i in LOCATION] # type float in location list

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
        Z_AXIS = np.array(Z_AXIS) # type numpy.ndarray
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        X_AXIS = np.array(X_AXIS) # type numpy.ndarray
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
        LOCATION = [float(i)*1000 for i in LOCATION]
        
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
        DIRECTION = [float(i) for i in DIRECTION]
        
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
        LOCATION = [float(i)*1000 for i in LOCATION]
        
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
        Z_AXIS = np.array(Z_AXIS) # type numpy.ndarray
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        X_AXIS = np.array(X_AXIS) # type numpy.ndarray
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
        RADIUS = float(values[2])*1000
        ANGLE = values[3]

        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        CARTESIAN_POINT = values[1]
        DIRECTION_1 = values[2]
        DIRECTION_2 = values[3]

        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        values = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find('(')+1:-4].split(',(')
        LOCATION = values[1].split(',')
        LOCATION = [float(i)*1000 for i in LOCATION]

        DIRECTION_1_LINE = str(arquivoStep.__getitem__(DIRECTION_1))
        values = DIRECTION_1_LINE[DIRECTION_1_LINE.find('(')+1:-3].split(',(')
        Z_AXIS = values[1].replace(')','').split(',')

        DIRECTION_2_LINE = str(arquivoStep.__getitem__(DIRECTION_2))
        values = DIRECTION_2_LINE[DIRECTION_2_LINE.find('(')+1:-3].split(',(')
        X_AXIS = values[1].replace(')','').split(',')

        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        Z_AXIS = np.array(Z_AXIS) # type numpy.ndarray
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        X_AXIS = np.array(X_AXIS) # type numpy.ndarray
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
        MAX_RADIUS = float(values[2])*1000
        MIN_RADIUS = float(values[3])*1000
        
        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        CARTESIAN_POINT = values[1]
        DIRECTION_1 = values[2]
        DIRECTION_2 = values[3]

        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        values = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find('(')+1:-4].split(',(')
        LOCATION = values[1].split(',')
        LOCATION = [float(i)*1000 for i in LOCATION]

        DIRECTION_1_LINE = str(arquivoStep.__getitem__(DIRECTION_1))
        values = DIRECTION_1_LINE[DIRECTION_1_LINE.find('(')+1:-4].split(',(')
        Z_AXIS = values[1].split(',')

        DIRECTION_2_LINE = str(arquivoStep.__getitem__(DIRECTION_2))
        values = DIRECTION_2_LINE[DIRECTION_2_LINE.find('(')+1:-4].split(',(')
        X_AXIS = values[1].split(',')

        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        Z_AXIS = np.array(Z_AXIS) # type numpy.ndarray
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        X_AXIS = np.array(X_AXIS) # type numpy.ndarray
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
        RADIUS = float(values[2])*1000

        AXIS2_PLACEMENT_3D_LINE = str(arquivoStep.__getitem__(AXIS2_PLACEMENT_3D))
        values = AXIS2_PLACEMENT_3D_LINE[AXIS2_PLACEMENT_3D_LINE.find('(')+1:-3].split(',')
        
        CARTESIAN_POINT = values[1]
        DIRECTION_1 = values[2]
        DIRECTION_2 = values[3]

        CARTESIAN_POINT_LINE = str(arquivoStep.__getitem__(CARTESIAN_POINT))
        values = CARTESIAN_POINT_LINE[CARTESIAN_POINT_LINE.find('(')+1:-4].split(',(')
        LOCATION = values[1].split(',')
        LOCATION = [float(i)*1000 for i in LOCATION]
        
        DIRECTION_1_LINE = str(arquivoStep.__getitem__(DIRECTION_1))
        Z_AXIS = DIRECTION_1_LINE[DIRECTION_1_LINE.find('(')+1:-4].split(',(')
        Z_AXIS = Z_AXIS[1].split(',')

        DIRECTION_2_LINE = str(arquivoStep.__getitem__(DIRECTION_2))
        X_AXIS = DIRECTION_2_LINE[DIRECTION_2_LINE.find('(')+1:-4].split(',(')
        X_AXIS = X_AXIS[1].split(',')

        Z_AXIS = [float(Z_AXIS[0]),float(Z_AXIS[1]),float(Z_AXIS[2])]
        Z_AXIS = np.array(Z_AXIS) # type numpy.ndarray
        X_AXIS = [float(X_AXIS[0]),float(X_AXIS[1]),float(X_AXIS[2])]
        X_AXIS = np.array(X_AXIS) # type numpy.ndarray
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

surfaces_list = ['CYLINDRICAL_SURFACE','PLANE','CIRCLE','SPHERICAL_SURFACE','TOROIDAL_SURFACE','LINE','CONICAL_SURFACE']

def main_for_tests():
    # open file
    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        data = arquivoStep.data[0]
        line_ids_list = list(data.references()) 

        for line_id in line_ids_list:
            line = (arquivoStep.__getitem__(line_id))

            try: # find surfaces lines
                reference_name = line.entity.name
                if reference_name in surfaces_list:
                    if reference_name == 'CYLINDRICAL_SURFACE':
                        cylinder_type(line_id)
                    elif reference_name == 'PLANE':
                        plane_type(line_id)
                    elif reference_name == 'CIRCLE':
                        circle_type(line_id)
                    elif reference_name == 'SPHERICAL_SURFACE':
                        spherical_surface(line_id)
                    elif reference_name == 'TOROIDAL_SURFACE':
                        toroidal_surface(line_id)
                    elif reference_name == 'LINE':
                        line_type(line_id)
                    elif reference_name == 'CONICAL_SURFACE':
                        cone_type(line_id)
                    else:
                        print("Just debug")

            except AttributeError as e: # ComplexEntityInstance has no attribute entity
                print(str(e))

'''
reference_name_comparar is a function used to compare the type of curve with what already exists. It also calls the function to find the features.
@params: reference name received from the reference_name_finder function
@return: None
'''
def reference_name_comparer(reference_name, line_id):
    if reference_name in surfaces_list:
        if reference_name == 'CYLINDRICAL_SURFACE':
            cylinder_type(line_id)
        elif reference_name == 'PLANE':
            plane_type(line_id)
        elif reference_name == 'CIRCLE':
            circle_type(line_id)
        elif reference_name == 'SPHERICAL_SURFACE':
            spherical_surface(line_id)
        elif reference_name == 'TOROIDAL_SURFACE':
            toroidal_surface(line_id)
        elif reference_name == 'LINE':
            line_type(line_id)
        elif reference_name == 'CONICAL_SURFACE':
            cone_type(line_id)
        else:
            print("Just debug")
            
'''
reference_name_finder is a function used to find the name of the curves and surfaces.
@params: None
@return: retorna o nome para ser usada na função 'reference_name_comparer'
'''
def reference_name_finder(): 
    # open file
    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # uploaded file
        data = arquivoStep.data[0]
        line_ids_list = list(data.references())

        for line_id in line_ids_list:
            line = arquivoStep.__getitem__(line_id)
            try:
                reference_name = line.entity.name 
                if reference_name == 'MECHANICAL_DESIGN_GEOMETRIC_PRESENTATION_REPRESENTATION':
                    styled_items_list = list(line.entity.params[1])
                    for styled_items_id in styled_items_list:
                        styled_items_line = arquivoStep.__getitem__(styled_items_id)
                        styled_items_line_param = styled_items_line.entity.params
                        
                        advanced_face_id = styled_items_line_param[2]
                        advanced_face_line = arquivoStep.__getitem__(advanced_face_id)
                        advanced_face_line_param = advanced_face_line.entity.params

                        face_bound_list = list(advanced_face_line_param[1]) 
                        surfaces_id = advanced_face_line_param[2]

                        reference_name = arquivoStep.__getitem__(surfaces_id).entity.name # REFERENCE NAME USED IN MAIN FUNCTION
                        reference_name_comparer(reference_name, surfaces_id)

                        for face_bound_ids in face_bound_list: # busca as linhas face_outer_bounds e face_bounds
                            face_bound_line = arquivoStep.__getitem__(face_bound_ids)
                            face_bound_line_param = face_bound_line.entity.params
                            edge_loop_ids = face_bound_line_param[1]
                            edge_loop_line = arquivoStep.__getitem__(edge_loop_ids)
                            edge_loop_line_params = edge_loop_line.entity.params

                            oriented_edge_ids_list = list(edge_loop_line_params[1])
                            for oriented_edge_ids in oriented_edge_ids_list:
                                oriented_edge_line = arquivoStep.__getitem__(oriented_edge_ids)
                                oriented_edge_line_params = oriented_edge_line.entity.params
                                edge_curve_id = oriented_edge_line_params[3]                  
                                edge_curve_line = arquivoStep.__getitem__(edge_curve_id)
                                edge_curve_line_params = edge_curve_line.entity.params
                                
                                start_point_id = edge_curve_line_params[1] # not yet used
                                end_point_id = edge_curve_line_params[2] # not yet used
                                type_id = edge_curve_line_params[3] 

                                reference_name = arquivoStep.__getitem__(type_id).entity.name # REFERENCE NAME USED IN MAIN FUNCTION
                                reference_name_comparer(reference_name, type_id)
                        
            except AttributeError as e:
                pass
            
def main():
    reference_name_finder()

main()