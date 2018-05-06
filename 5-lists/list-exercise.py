import arcpy

with open('features-to-check.txt', 'r') as features_to_check:
    for line in features_to_check:
        line_fields = line.split(',')
        path = line_fields[0]
        field_names = line_fields[1].split('|')
        print(field_names)
