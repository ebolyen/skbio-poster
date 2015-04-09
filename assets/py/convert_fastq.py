import skbio.io

seqs = skbio.io.read("example.fna",
                     qual="example.qual",
                     format="fasta")

skbio.io.write(seqs,
               into="example.fastq",
               variant="illumina1.8",
               format="fastq")
