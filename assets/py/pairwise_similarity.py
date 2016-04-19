from skbio import DNA
from skbio.alignment import global_pairwise_align_nucleotide

s1 = DNA.read("data/seq1")
s2 = DNA.read("data/seq2")
query = DNA("TTTTCTTGTTGATTCTGGTCCAGAGTAATCGCTTGAGTGTTG")

def pairwise_similarity(seq, query):
    alignment = global_pairwise_align_nucleotide(seq, query)
    return alignment[0].fraction_same(alignment[1])

print "seq1: %s\nseq2: %s" % (s1, s2)
print "seq1-query: %s" % pairwise_similarity(s1, query)
print "seq2-query: %s" % pairwise_similarity(s2, query)
