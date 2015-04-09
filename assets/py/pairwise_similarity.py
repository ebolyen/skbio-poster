from skbio import DNA
from skbio.alignment import global_pairwise_align_nucleotide

s1 = DNA.read("seq1.fna")
s2 = DNA.read("seq2.fna")

alignment = global_pairwise_align_nucleotide(
    s1, s2, penalize_terminal_gaps=True)

aligned_s1 = alignment[0]
aligned_s2 = alignment[1]

fraction_same = aligned_s1.fraction_same(aligned_s2)
print fraction_same
