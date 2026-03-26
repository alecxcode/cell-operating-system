from codons import DNA_Codons, RNA_Codons


def reverse_complement(dna):
    res = ''
    rev_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for a in dna:
        res += rev_map[a]
    return res[::-1]


print(reverse_complement("GGCAATTTG"))


def translate_RNA(rna):
    prot = ''
    i = 0
    while i < len(rna):
        try:
            triplet = rna[i:i+3]
            aa = RNA_Codons[triplet]
            if aa == '.':
                break
            prot += aa
            i += 3
        except:
            print("translation error")
            break
    return prot


dna = """tgc tac atc cag
      aac tgc ccc ctg gga"""
dna = dna.replace('\n', '').replace(' ', '').upper()
rna = dna.replace('T', 'U')
print(rna)
print(translate_RNA(rna))


def translate_directly(rna):
    prot = ''
    i = 0
    while i < len(rna):
        try:
            triplet = rna[i:i+3]
            aa = DNA_Codons[triplet]
            if aa == '.':
                break
            prot += aa
            i += 3
        except:
            print("translation error")
            break
    return prot


print(translate_directly("tgctacatccagaactgccccctggga".upper()))


def insideout_dict(dictionary):
    reversed_dict = {}
    for k, v in dictionary.items():
        if v in reversed_dict:
            reversed_dict[v].append(k)
        else:
            reversed_dict[v] = [k]
    return reversed_dict


print(insideout_dict(DNA_Codons))


def genetic_code_simplified(prot):
    aa_to_dna = insideout_dict(DNA_Codons)
    i = 0
    dna = ''
    for amino_acid in prot:
        i += 3
        try:
            triplets = aa_to_dna[amino_acid]
            dna += triplets[0]
        except:
            print("decoding error")
            break
    return dna


print(genetic_code_simplified("CYIQNCPLG"))
