
import xlrd
import os
import arcpy
from arcpy import env


dirname = os.path.dirname(__file__)
domainsXLS = os.path.join(dirname, 'data\domains.xlsx')
in_table = domainsXLS+"\Fields_List$"
if __name__ == "__main__": 
	workbook = xlrd.open_workbook(domainsXLS)
	worksheet = workbook.sheet_by_name("Fields_List")
	num_rows = worksheet.ncols - 1
	
	fields = [t.encode('utf8') for t in worksheet.row_values(0)]

	curr_row = 0
	while curr_row < num_rows:
		curr_row += 1
		field_name = worksheet.col_values(curr_row)[0].strip()
		arcpy.AddMessage(field_name)
		arcpy.TableToDomain_management(in_table=in_table, code_field=field_name, description_field=field_name, in_workspace="Database Connections\\regis.sde", domain_name=field_name, domain_description=field_name, update_option="REPLACE")
		arcpy.AssignDomainToField_management(in_table="Database Connections\\regis.sde\\regis.dbo.Parcelle", field_name=field_name, domain_name=field_name)