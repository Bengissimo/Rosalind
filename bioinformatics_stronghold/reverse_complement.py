# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reverse_complement.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkandemi <bkandemi@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/20 16:13:29 by bkandemi          #+#    #+#              #
#    Updated: 2022/01/20 16:49:08 by bkandemi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

path = "/Users/bengisu/Desktop/rosalind/bioinformatics_stronghold/"
f_input = open(path + 'rosalind_revc.txt', 'r')
dna_seq = f_input.readline()
rev_seq = dna_seq[::-1]
rev_comp_seq = ''
for letter in rev_seq:
	if letter == 'A':
		rev_comp_seq += 'T'
	elif letter == 'T':
		rev_comp_seq += 'A'
	elif letter == 'G':
		rev_comp_seq += 'C'
	elif letter == 'C':
		rev_comp_seq += 'G'
print(rev_comp_seq)


