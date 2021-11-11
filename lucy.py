import csv

with open('data.csv', 'r') as infile: 
    reader = csv.DictReader(infile)
    for row in reader: 
        print(row['fruit'], row['color'], row['taste'])
        output_filename = './fruit_files/' + row['fruit'] + '.md'
        with open(output_filename, 'w') as outfile: 
            outfile.write(row['color'] + '\n')
            outfile.write(row['taste'])


import csv
import io

with io.open('./pages/3mojidata.csv', 'r', encoding='utf-8') as infile: 
    reader = csv.DictReader(infile)
    for row in reader:
        print(row['filename'], row['file-info'])
        if row['file-info'].strip() == '': continue

        if 'smileys&emotion' in row['file-info']: 
            output_filename = './pages/smileys&emotion/' + row['filename']

        if 'people&body' in row['file-info']: 
            output_filename = './pages/people&body/' + row['filename']

        if 'animals&nature' in row['file-info']: 
            output_filename = './pages/animals&nature/' + row['filename']

        if 'food&drink' in row['file-info']: 
            output_filename = './pages/food&drink/' + row['filename']

        if 'travel&places' in row['file-info']: 
            output_filename = './pages/travel&places/' + row['filename']
        
        if 'travel&places' in row['file-info']: 
            output_filename = './pages/travel&places/' + row['filename']

        if 'activities' in row['file-info']: 
            output_filename = './pages/activities/' + row['filename']

        if 'objects' in row['file-info']: 
            output_filename = './pages/objects/' + row['filename']

        with io.open(output_filename, 'w', encoding='utf-8') as outfile: 
            outfile.write(row['file-info'])




# stopwords = ['with', 'on', 'the']
# titles = ['smiling face with smiling eyes', 'rolling on the floor laughing', 'grinning face with smiling eyes']
# for title in titles: 
#     new_title = title.title().split(' ')
#     new_new_title = []
#     for tok in new_title: 
#         if tok.lower() in stopwords: 
#             new_new_title.append(tok.lower())
#         else:
#             new_new_title.append(tok)
#     new_new_title = ' '.join(new_new_title)
#     print(new_new_title)


# titles = ['crab apples', 'apples', 'oranges', 'sweet oranges']
# query = 'a'
# for title in titles: 
#     tokens = title.split()
#     for tok in tokens: 
#         if tok.startswith(query): 
#             print(title)