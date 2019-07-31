def do_mutation(chrom, prob = 10):
    
    # Code mutates chromesome that formed with dictionary
    # Mutation Probabily adjusted to %10
    
    chrom_keys = [list(chrom.keys())[i] for i in range(len(chrom))]
    chrom_values = [list(chrom.values())[i] for i in range(len(chrom))]
    
    mut_prob = np.random.randint(0,100)
    mut_prob = 5
    
    if mut_prob < prob :
        
        np.random.shuffle(chrom_values)
    
    return {chrom_keys[i] : chrom_values[i] for i in range(len(chrom))}
