"""This file was created by Nico Salamone
"""

import csv

def read_data_set(file_name, delimiter=';', new_line=''):
	"""
	Read a data set.

	:file_name: The file name.
	:delimiter: The character used to delimite the attributes.
	:new_line: The character used for the new lines.
	:return: The data set.
	"""

	data_set = []

	with open(file_name, newline=new_line) as file:
		csv_reader = csv.reader(file, delimiter=delimiter, quotechar='\"')

		for row in csv_reader:
			data_set.append(row)

	return data_set

def write_data_set(data_set, file_name, delimiter=';', new_line='', mode='w'):
	"""
	Write a data set.

	:data_set: A data set.
	:file_name: The file name.
	:delimiter: The character used to delimite the attributes.
	:mode: The mode indicating how the file is to be opened.
	:new_line: The character used for the new lines.
	"""

	with open(file_name, mode, newline=new_line) as file:
		csv_writer = csv.writer(file, delimiter=delimiter, quotechar='\"', quoting=csv.QUOTE_MINIMAL)

		for row in data_set:
			csv_writer.writerow(row)

if __name__ == "__main__":
	file_name = "data/ticeval2000.txt"
	output_file_name = "data/ticeval2000.arff"
	att_list = ["MOSTYPE", "MAANTHUI", "MGEMOMV", "MGEMLEEF", "MOSHOOFD", "MGODRK", "MGODPR", "MGODOV", "MGODGE",
		"MRELGE", "MRELSA", "MRELOV", "MFALLEEN", "MFGEKIND", "MFWEKIND", "MOPLHOOG", "MOPLMIDD", "MOPLLAAG",
		"MBERHOOG", "MBERZELF", "MBERBOER", "MBERMIDD", "MBERARBG", "MBERARBO", "MSKA", "MSKB1", "MSKB2", "MSKC",
		"MSKD", "MHHUUR", "MHKOOP", "MAUT1", "MAUT2", "MAUT0", "MZFONDS", "MZPART", "MINKM30", "MINK3045", "MINK4575",
		"MINK7512", "MINK123M", "MINKGEM", "MKOOPKLA", "PWAPART", "PWABEDR", "PWALAND", "PPERSAUT", "PBESAUT",
		"PMOTSCO", "PVRAAUT", "PAANHANG", "PTRACTOR", "PWERKT", "PBROM", "PLEVEN", "PPERSONG", "PGEZONG", "PWAOREG",
		"PBRAND", "PZEILPL", "PPLEZIER", "PFIETS", "PINBOED", "PBYSTAND", "AWAPART", "AWABEDR", "AWALAND", "APERSAUT",
		"ABESAUT", "AMOTSCO", "AVRAAUT", "AAANHANG", "ATRACTOR", "AWERKT", "ABROM", "ALEVEN", "APERSONG", "AGEZONG",
		"AWAOREG", "ABRAND", "AZEILPL", "APLEZIER", "AFIETS", "AINBOED", "ABYSTAND"]
	att_list.append("CARAVAN")
	#att_type_list = ["NUMERIC"] * 85
	""" For nominal attributes."""
	att_type_list = ["{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26," \
		" 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41}",
		"{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}",
		"{1, 2, 3, 4, 5, 6}",
		"{1, 2, 3, 4, 5, 6}",
		"{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}",
		"{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"]
	att_type_list.extend(["NUMERIC"] * 37)
	att_type_list.append("{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}")
	att_type_list.extend(["NUMERIC"] * 20)
	att_type_list.append("{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}")
	att_type_list.extend(["NUMERIC"] * 20)

	att_type_list.append("{1, 0}")

	data_set = read_data_set(file_name, delimiter='\t')
	data_set = [[int(data) for data in row] for row in data_set]
	for row in data_set:
		row.append('?')

	with open(output_file_name, 'w', newline='') as file:
		file.write("@RELATION caravan\n\n")

		att_string = []
		for att, att_type in zip(att_list, att_type_list):
			att_string.append("@ATTRIBUTE ")
			att_string.append(att)
			att_string.append(' ')
			att_string.append(att_type)
			att_string.append('\n')
		att_string = ''.join(att_string)
		file.write(att_string)

		file.write("\n@DATA\n")

	write_data_set(data_set, output_file_name, delimiter=',', mode='a')
