from skbio.io import read, write

seqs = read("example.fna", qual="example.qual",
                           format="fasta")

write(seqs, into="example.fastq",
            variant="illumina1.8",
            format="fastq")
