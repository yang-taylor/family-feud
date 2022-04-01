points = 110
number = 0

with open ('qa.json', 'w') as final_file:
	final_file.write('[\n')
	with open('questions.txt', encoding='utf8') as txt_file:
		for line in txt_file:
			points = points - 10
			number = number + 1
			if 'Question' in line:
				points = 110
				number = 0
				final_file.write("""
		]
	},
	{
		"question": """)
#				final_file.write('\t\t]\n')
#				final_file.write('\t},\n')
#				final_file.write('\t{\n')
#				final_file.write("\t\t\"question\": ")
				final_file.write("\"" + line[9:len(line) - 2] + "\",\n")
				final_file.write("""		"answers": [\n""")
#				final_file.write("\t\t\"answers\": [\n")
			else:
				before = """\t\t\t{
				"number": """
				
				middle1 = """,
				"solution": \""""

				middle2 = """\",
				"points": """
				
				end = """
			},\n"""
				final_file.write(before + str(number) + middle1 + line[:len(line) - 1] + middle2 + str(points) + end)