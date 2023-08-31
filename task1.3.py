
encoded_lists = [[1,2,3,4,6],[5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]

def explode_chains(encoded_lists):
    for chain in encoded_lists:
        for i in chain:
            if i+1 in chain:
                if i+2 in chain:
                    chain.remove(i+2)
                chain.remove(i)
                chain.remove(i+1)
    return encoded_lists

print(explode_chains(encoded_lists))