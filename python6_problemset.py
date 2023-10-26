#!/usr/bin/env python3



#####Q1/2
#with open ('Python_06.txt', 'r') as data_file:
#    with open('Python_06_uc.txt', 'a') as output_file:
#        for line in data_file:
#            output_file.write(line.upper())
#
#with open('Python_06_uc.txt', 'r') as file_object:
#    content = file_object.read()

#print(content)



#####Q1/2


#####Q3
with open('Python_06.seq.txt', 'r') as seq_file:
    for line in seq_file:
        gene_id,seq= line.split()
        revseq = seq[::-1].upper()
        revseq = revseq.replace('A','t')
        revseq = revseq.replace('T','a')
        revseq = revseq.replace('C','g')
        revseq = revseq.replace('G','c')
        revseq = revseq.upper()
print(f'>{gene_id} revcomp\n{revseq}')


#####Q3:

#####Q4

#total_line=0
#total_count=0

#with open('Python_06.fastq','r') as q4_file:
#    for line in q4_file:
#        nline = len(line)
#        total_count += nline
#        total_line += 1
#    
#    m = total_count / total_line
#print('total de caracteres = ', total_count)
#print('total de linhas = ', total_line)
#print('média tamanho da linha = ', m)



#####Q4


#####Q5
seq = {}
nc = ('A', 'T', 'C', 'G')
#with open('Python_06.seq.txt') as file:
#    cur_key = ''
#    for line in file:
#        if line.startswith('>'):
#            cur_key = line.rstrip()[1:]
#            seq[cur_key] = ''
#        else:
#            seq[cur_key] += line.rstrip()
#    print(seq)


with open('saida.txt','w'):
    for i in seq:
        nc_count = []
        for x in nc:
            nc_count.append(seq[i].count(x))

        write(f'{i} - A:{nc_count[0]}, T:{nc_count[1]}, C:{nc_count[2]}, G:{nc_count[3]}\n')


