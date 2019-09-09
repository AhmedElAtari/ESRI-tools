
import xlrd
import arcpy
import os

dirname = os.path.dirname(__file__)
alisXLS = os.path.join(dirname, 'data\\alias_parcelle.xlsx')

if __name__ == "__main__": 
	workbook = xlrd.open_workbook(alisXLS)
	worksheet = workbook.sheet_by_name("a")
	num_rows = worksheet.nrows - 1
	arcpy.AddMessage(num_rows)
	fields = [t.encode('utf8') for t in worksheet.row_values(0)]

	curr_row = 0
	while curr_row < num_rows:
		curr_row += 1
        # Field's Name
		field_name = worksheet.row_values(curr_row)[0]

        # Field's Alias
		field_alias = worksheet.row_values(curr_row)[1]

        # Assign Field Alias
		arcpy.AlterField_management(in_table="Database Connections\\regis.sde\\regis.dbo.Parcelle",field=field_name,new_field_alias=field_alias)