import os
import openpyxl as xl
import pandas as pd 
import xlrd
import xlwt
import xlsxwriter
import pathlib


rootpath = 'E:\\College\\Semester 6\\Files\\python\\files iterate\\Test Data'
header = []
folders = []
files =[]

for r, d, f in os.walk(rootpath):
	for folder in d:
		folders.append(os.path.join(r,folder))

for _ in folders:
	for r, d, f in os.walk(_):
		data = []
		for file in f:
			if '.xlsx' in file:
					print("[+] " + os.path.join(r,file) + " --> Done!")
					# print(pathlib.PurePath(os.path.join(r,file)).parent.name)
					
					wb = xlrd.open_workbook(os.path.join(r,file)) 
					sheet = wb.sheet_by_index(0) 
					n_row = sheet.nrows-1
					n_column = sheet.ncols-1
					header = sheet.row_values(0)
					data.insert(len(data)+1,sheet.row_values(n_row))
					#Writing !!
					wb_write = xl.Workbook()
					
					### set file name as foldername.xlsx!!
					f_path = pathlib.PurePath(os.path.join(r,file)).parent.name+ ".xlsx"
					sheet_write = wb_write.active
					sheet_write.append(header)
					for row_data in data:
						sheet_write.append(row_data)
					
					wb_write.save(f_path)
		# for folder in d:
		# 	# folders.append(os.path.join(r,folder))
		# 	print(os.path.join(r,folder))



###---------------------for single directory
# wb = xlrd.open_workbook(rootdir) 
# sheet = wb.sheet_by_index(0) 

# n_row = sheet.nrows-1
# n_column = sheet.ncols-1
# header = sheet.row_values(0)
# data.insert(len(data)+1,sheet.row_values(n_row))
# data.insert(len(data)+1,sheet.row_values(n_row-1))


# #### Writing into file!!!

# wb_write = xl.Workbook()

# path = os.getcwd()

# f_path = path + "\\demo.xlsx"
# sheet_write = wb_write.active

# sheet_write.append(header)
# for row_data in data:
# 	sheet_write.append(row_data)

# wb_write.save(f_path)

###---------------------------------
