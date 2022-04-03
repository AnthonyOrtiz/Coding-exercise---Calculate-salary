''' class to check and extract worker data '''

import re

fileData = 'dataSchedules.txt'


def getDataWorkers():

	if fileData :
		listData = []
		
		#Open file .txt
		with open(fileData) as f_obj:
			
			#creation of a list of timetable dictionaries
			for line in f_obj:

				dictSchedules = {}

				#regular expressions
				erName = re.compile(r'\w+')
				erSchedules = re.compile(r'([A-Z]+)(\d+:\d+)-(\d+:\d+)')
			
				name = erName.search(line)
				schedules = erSchedules.findall(line)

				dictSchedules["Name"] = str(name.group())
				dictSchedules["Schedules"] = schedules

				listData.append(dictSchedules)

			return listData

	else:
		return listData