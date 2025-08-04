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
