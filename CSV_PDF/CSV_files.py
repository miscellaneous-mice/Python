import csv

data = open('example.csv', encoding='utf-8')

csv_data = csv.reader(data) # We can also provide a delimiter -> check notebook

data_lines = list(csv_data)

print(data_lines[0]) # Table of contents

print("No. of rows {}".format(len(data_lines)))

print("No. of columns {}".format(len(data_lines[0])))

print("Last row {}".format(data_lines[-1]))

print("\nFirst five rows")
for line in data_lines[:5]: # O index is Table of contents, Hence data starts at index 1
    print(line)

print("\n")
print(data_lines[10])
print(data_lines[10][3])


print("\nEmail of first 14 data lines")
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)


print("\nFull names of first 14 data lines")
full_names = []
for line in data_lines[1:15]:
    full_names.append(line[1] + ' ' + line[2])

print(full_names)


print("\nWriting to a csv file")
file_to_output = open('to_save_file.csv', mode='w', newline='') # Will overwrite any file names to_save_file.csv
csv_writer = csv.writer(file_to_output, delimiter=',') # Demilimter is what seperates one column from another

csv_writer.writerow(['a', 'b', 'c']) # We can see delimiter is ,
'''
If delimiter is ;
Then csv_writer.writerow(['a'; 'b'; 'c'])
'''

csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()

f = open('to_save_file.csv', mode='a',newline='') # Mode a is append to the csv file, not overwrite
csv_writer = csv.writer(f)

csv_writer.writerow(['7', '8', '9'])
csv_writer.writerow(['10', '11', '12'])


f.close()


