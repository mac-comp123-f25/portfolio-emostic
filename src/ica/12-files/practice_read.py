# file_in = open("../TextFiles/alice.txt", 'r')
# print(file_in)

file_in = open("../TextFiles/alice.txt", 'r')
count = 0
for text_line in file_in:
  text_line = text_line.strip()    # remove newline from end of line
  print("Line", count, ":", text_line)
  count = count + 1
file_in.close()
