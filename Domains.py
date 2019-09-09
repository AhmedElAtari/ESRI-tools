import os
import xlrd
import arcpy


dirname = os.path.dirname(__file__)

# Domains Table / Excel file
domainsXLS = os.path.join(dirname, 'Domains_Sample.xlsx')

# Fiels sheet
in_table = domainsXLS+"\Fields_List$"

if __name__ == "__main__": 
	# open excel file 
	workbook = xlrd.open_workbook(domainsXLS)
	# Get sheet by name
	worksheet = workbook.sheet_by_name("Fields_List")
	num_rows = worksheet.ncols - 1
	fields = [t.encode('utf8') for t in worksheet.row_values(0)]
	curr_row = 0
	while curr_row < num_rows:
		curr_row += 1
		# Get Field's name
		field_name = worksheet.col_values(curr_row)[0].strip()

		# Create domain into the Geodatabase
		arcpy.TableToDomain_management(in_table=in_table, code_field=field_name, description_field=field_name, in_workspace="Database Connections\\regis.sde", domain_name=field_name, domain_description=field_name, update_option="REPLACE")

		# Assign domain to the field
		arcpy.AssignDomainToField_management(in_table="Database Connections\\regis.sde\\regis.dbo.Parcelle", field_name=field_name, domain_name=field_name)