# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    transcribe.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkandemi <bkandemi@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/20 15:19:52 by bkandemi          #+#    #+#              #
#    Updated: 2022/01/20 15:31:11 by bkandemi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

path = "/Users/bengisu/Desktop/rosalind/bioinformatics_stronghold/"
f_input = open(path + 'rosalind_rna.txt', 'r')
dna_seq = f_input.readline()
rna_seq = dna_seq.replace('T', 'U')	
print(rna_seq)