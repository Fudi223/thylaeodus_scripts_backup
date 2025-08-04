def percentage(part, whole):
    percentage_nr =  100 * float(part)/float(whole)
    return percentage_nr

def seq_div_gt(line:str, threshold_seq_div:float) -> bool:
        # Split the columns by tabs
        columns: list[str] = line.split("\t")
        # Get the "de:f:number" column from each line 
        for seq_div_col in columns:
            if seq_div_col.startswith("de"):
                # Remove the string "de:f:" and only keep the number in a string
                seq_div:float = float(seq_div_col[len("de:f:"):])
                break
        return seq_div > threshold_seq_div

def query_percentage_lt(line:str, query_threshold:float) -> bool:
        q_colls:list[str] = line.split("\t")
        # Define variables for percentage calculation based on position of target column
        query_total:float = float(q_colls[1])                                                     # Total query sequence length is in the second column
        query_start_col:float = float(q_colls[2])                                                 # Starting coordinate of the query sequence is in the third column
        query_end_col:float = float(q_colls[3])                                                   # Ending coordinate of the query sequence is in the fourth column
        query_lenght:float = query_end_col - query_start_col                                      # Lenght of sequence between the start and end coordinate
        query_percentages:float = percentage(query_lenght, query_total)   
        return query_percentages < query_threshold

def target_percentage_lt(line:str, target_threshold:float) -> bool:
        t_colls = line.split("\t")
        # Define variables for percentage calculation based on position of target column
        target_total:float = float(t_colls[8])                                                    # Total target sequence length is in the 9th column
        target_start_col:float = float(t_colls[9])                                                # Starting coordinate of the target sequence is in the 10th column
        target_end_col:float = float(t_colls[10])                                                 # Ending coordinate of the target sequence is in the 11th column                                                                     
        target_length:float = float(target_end_col) - float(target_start_col)                     # Lenght of sequence between the start and end coordinate
        target_percentages:float = percentage(target_length, target_total)      
        return target_percentages < target_threshold


# import os
# from tqdm import tqdm # type: ignore

# path_dir = os.path.dirname(os.path.realpath(__file__))
# file_name = os.path.join(path_dir, "cluster.tsv")

# with open(file_name, "r") as file:
#     alignment_list = file.readlines()
#     alignments = " ".join(alignment_list)
#     gene_list= []
#     gene_pairs = []
#     columns = alignments.split("_")

#     # extract genes (i.e. "g3") from the lines in the .paf file and add them to the gene_list
#     for genes in columns:
#         if genes.startswith("g"):
#             gene_list.append(genes)
#     # print(gene_list)
    
#     print('creating list with genes...') #from each line paired up, aka the genes with alignments
#     for pairs in tqdm(range(0, len(gene_list), 2)):
#         pair = gene_list[pairs:pairs+2]
#         if len(pair) == 2:
#             gene_pairs.append(pair)
#     #print("These are my gene pairs","\n\n",gene_pairs)

    
#     # create a dictionary with the genes as keys and values set to "0"
#     components = {el:0 for el in gene_list}
#     # print(components)
    
#     component_counter = 1
#     gene_components = {}
#     print('parsing gene pairs...')
#     for gene_1, gene_2 in tqdm(gene_pairs):
#         # if gene_1 == gene_2:
#         #     continue
#         if gene_1 not in gene_components:
#             gene_components[gene_1] = component_counter
#             component_counter += 1
#         if gene_2 not in gene_components:
#             gene_components[gene_2] = gene_components[gene_1]


#     print("Clusters:\n", gene_components)
