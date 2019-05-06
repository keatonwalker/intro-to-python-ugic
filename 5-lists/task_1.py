import arcpy
import csv
# You will need one more import here. Use the code to find out what it is.

check_feature_file = 'features-to-check.txt'
output_feature_file = 'feature-with-values.txt'
feature_values = [] # list to store output list. [[Schools, 'nebo|name|k12'], ...]
with open(check_feature_file, 'r') as features_to_check:
   
    headers = next(features_to_check) # Get the field headers
    print('Here are the field headers as a list: {}'.format(headers.split(',')))
    # loop through the lines of features-to-check.txt
    for line in features_to_check:
        split_line = None # Split the line to get path, fields
        
        path = None # Get the path and assign it to a variable
        feature_name = os.path.basename(path) # Use os.path.basename to get feature class name
        value_row = [feature_name]

        # Get the pipe (|) delimited fields and split them into a list. Assign the list to a variable
        fields = None
        fields[-1] = fields[-1].strip()
        
        # Use a SearchCursor to get the value of each field in the fields list
        with arcpy.da.SearchCursor(path, fields) as cursor:
            for row in cursor:
                #print(row)
                row = [str(v) for v in row]
                value_piped_string = None # join row to create a pipe (|) delimited string.
                value_row.append(value_piped_string)
                #print(value_row)
        
        feature_values.append(None)  # append value_row to feature_values list
                
with open(output_feature_file, 'w') as feature_with_values:
    output_header = 'feature,values'
    feature_with_values.write(output_header + '\n')
    for out_row in feature_values:
        out_string = None.join(out_row) # join the rows of feature_values into a comma delimited string
        feature_with_values.write(out_string + '\n') # write the headers to a new file as comma delimited string