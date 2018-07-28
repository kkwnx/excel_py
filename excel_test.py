#!python3
import openpyxl

config_file = open('./configfile.txt','a',)

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
config_file.write('FILE=' + sheet['B4'].value)
config_file.close