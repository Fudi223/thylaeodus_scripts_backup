#!/usr/bin/env python

# Script for further filtering our .PAF file data. 
# Selecting for a sequence divergence of max. 0.02
# Selecting for an alignment of >= 75% 

# Trial runs using a file with a subset of alignments

# Functions
from filters import seq_div_gt , query_percentage_lt, target_percentage_lt

import os
# Desired thresholds
SEQ_DIV_THRESHOLD = 0.05
QUERY_THRESHOLD:float = 0.75
TARGET_THRESHOLD:float = 0.75
# Input path for the file to be processed
path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "testing_secAliNo.paf")# Todo look at path library

# Output path
output_file_name = os.path.join(path_dir, "secAliNo_test.txt")

def main() -> None:
      
    with open(file_name, "r") as file:
        # Read the file line by line
        lines = file.readlines()
        # Information to be filtered out and saved in list: "x.xxxx"
    filtered_sequences = []         # list of all alignment sequences with the preset filters engaged

    # Iterate over every column of the lines in the file
    for line in lines:
         if seq_div_gt(line, SEQ_DIV_THRESHOLD):
              continue
         if query_percentage_lt(line, QUERY_THRESHOLD):
              continue
         if target_percentage_lt(line, TARGET_THRESHOLD):
               continue
         filtered_sequences.append(line)
    print("\n".join(filtered_sequences))

    with open(output_file_name, "w") as out_file:
         out_file.writelines(filtered_sequences)

if __name__ == "__main__":
     main()




#__________________________SCRAPPED_____________________________#

# 1.

# for align in sequence_divergence_list:
# search for sequence divergence scores lower than 0.020 (or others, depending on what is required)
#    if re.search("de:f:0.1.+", align):
#            print(align)

# 2. 

# sequence_divergence_list = read_input("50_lines_16_CPU.txt")
# sd_column = "de:"
# sequence_string = [word for word in sequence_divergence_list if word.startswith(sd_column)]        

# 3.    
 
# sd_div = []

# for lines in sequence_divergence_list:
#    new_line=lines.split("  ")
#    sd_div.append(new_line)
    
    
# print(sd_div)

# 4. (First version of solution "5.", splitting with tabs doesnt work though)

# sd_column = "de:f.+"
# sd_list = []
# sds_list = []
# for i in sequence_divergence_list:
#     split_results = i.split("\t")
#     sd_list.append(split_results [19])
#       
# print(sd_list)
# print(sds_list)

# 5. (Works but is not flexible if columns are at a different position. Also just finds the de:f: info, nothing else)

# Extract the 4th last column from a .paf file (will be changed to be more specific)          
# for sds in sequence_divergence_list:
#    sd_final.append(sds[-4])
# print(sd_string)

# 6. (Gives the wanted tab and number of the row there the info occurs)

# sdv = input("Find the column: ")

# for line, row in enumerate(alignments_raw):
#    if sdv in row:
#        print("Value {0} found in line {1}".format(sdv, line))

# sequence_divergence_list = []

# 6. From iteration from the 3rd of April, scrapped due to complications

#                # Convert number strings into integers
#                seq_dev_val_floats.append(numeric)
#                seq_dev_val.append(value)
#    # Filter out every value that is below the set threshold
#    for thresh_max in seq_dev_val_floats:
#        if thresh_max <= thresh:
#            seq_dev_thresh_floats.append(thresh_max)
#    # Create extra list that doesnt hold floats
#    for no_float in seq_dev_thresh_floats:
#        seq_dev_thresh.append(str(no_float))
# print("List of all lines with all data: \n-------------------------------------------\n",tabless_list, "\n")
# print("==============================================================================================================================\n")
# print("List of all the Sequence Deviation values: \n-------------------------------------------\n",seq_dev_val, "\n\n\n")
# print("Sequence Deviation below 0.02 as floats: \n------------------------------------------\n",seq_dev_thresh_floats, "\n\n\n")
# print("Sequence Deviation below 0.02: \n--------------------------------\n",seq_dev_thresh, "\n\n\n")
# print("Alignment containing wanted Sequence Deviation matches: \n----------------------------------------------------------\n", matching_lines_thresholds)
# Save the extracted data as a .txt file (just to check for now)
# with open("sd_values.paf", "wt") as f:
#   print(sdv, file=f)

# 7. Older "bloated" version:

    #  # Split the columns by tabs
    #     columns: list[str] = line.split("\t")
    #     # Get the "de:f:number" column from each line 
    #     for seq_div_col in columns:
    #         if seq_div_col.startswith("de"):
    #             # Remove the string "de:f:" and only keep the number in a string
    #             value = seq_div_col[len("de:f:"):]
    #             value = seq_div_col.strip("de:f:")
    #             numeric = float(value)
    #             # Convert number strings into integers
    #             seq_div_val_floats.append(numeric)
    #             seq_div_val.append(value)
    #     # Check if the sequence divergence of the current line is below the threshold
    #     if numeric <= thresh_seq_div:
    #         # Add entire alignment data line to the "matching_lines_thresholds" list and then the "m_lines" string.
    #         matching_lines_thresholds.append(line)
    #         match_lines = " ".join(matching_lines_thresholds)
    # Check for Query Sequence Coverage of 75% or more
    #  for q_match_col in matching_lines_thresholds:
        # Split lines into own elements
        # q_colls = q_match_col.split("\t")
        # # Define variables for percentage calculation based on position of target column
        # query_total = float(q_colls[1])                                                     # Total query sequence length is in the second column
        # query_start_col = float(q_colls[2])                                                 # Starting coordinate of the query sequence is in the third column
        # query_end_col = float(q_colls[3])                                                   # Ending coordinate of the query sequence is in the fourth column
        # query_lenght = float(query_end_col) - float(query_start_col)                        # Lenght of sequence between the start and end coordinate
        # query_percentages = percentage(query_lenght, query_total)      	                    # Calculate percentage of coverage
        # Set threshold for lines to be kept that contain query coverage of more than 75%
    #     if query_percentages >= 0: # Todo CHANGE THESE to 75 FOR THE REAL DEAL
    #         # Add new set of lines into a list called query_sequence_coverage
    #         query_sequence_coverage.append(q_match_col)
    #         query_sequence_cov_list = " ".join(query_sequence_coverage)       
    # # Check for Target Sequence Coverage of 75% or more
    # for t_match_col in query_sequence_coverage:
    #     t_colls = t_match_col.split("\t")
    #     # Define variables for percentage calculation based on position of target column
    #     target_total = float(t_colls[8])                                                    # Total target sequence length is in the 9th column
    #     target_start_col = float(t_colls[9])                                                # Starting coordinate of the target sequence is in the 10th column
    #     target_end_col = float(t_colls[10])                                                 # Ending coordinate of the target sequence is in the 11th column                                                                     
    #     target_length = float(target_end_col) - float(target_start_col)                     # Lenght of sequence between the start and end coordinate
    #     target_percentages = percentage(target_length, target_total)                        # Calculate percentage of coverage
    #     # Set threshold for lines to be kept that contain target coverage of more than 75%
    #     if target_percentages >= 0: # CHANGE THESE to 75 FOR THE REAL DEAL
    #         #Add new set of lines into a list called target_sequence_coverage
    #         target_sequence_coverage.append(t_match_col)
    #         target_sequence_cov_list = " ".join(target_sequence_coverage)
    # Extract numbered query and target genes (from the previously filtered information) and put them in a table
    # for genes in target_sequence_coverage:
    #         gene_colls = genes.split("_")
    #         query_genes.append(gene_colls[6])
    #         target_genes.append(gene_colls[13])
    # print(query_genes)
    # print(target_genes)
# print("____________________________________", "\n","|",q_gene_colls[6],"|","\t\t","|", t_gene_colls[13], "|")
#  print("\n\n\n Alignments with a sequence deviation value below 0.02 AND query sequence + target coverage of 75% or more: \n\n===========================================================================================================\n\n ",target_sequence_cov_list)
# with open("alignments_filtered.paf", "wt") as f:
    #print(target_sequence_cov_list, file=f)
