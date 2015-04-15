from skbio import DNA
from skbio.alignment import global_pairwise_align_nucleotide

s1 = DNA.read("data/seq1")
s2 = DNA.read("data/seq2")

alignment = global_pairwise_align_nucleotide(
    s1, s2, penalize_terminal_gaps=True)

aligned_s1 = alignment[0]
aligned_s2 = alignment[1]

print aligned_s1.fraction_same(aligned_s2)
