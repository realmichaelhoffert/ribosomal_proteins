import sys
import os

with open(sys.argv[1], 'r') as genome_chunk:
    test_genomes = [l.replace('\n', '') for l in genome_chunk.readlines()]

faa_path = '/data/mhoffert/genomes/GTDB_r207/protein_faa_reps/bacteria/'
blast_db = '/data/mhoffert/db/pgap_ribosomal/blastrules_4.0/ribosomal_proteins'
blast6_fmt_str = '"6 qseqid sseqid pident length mismatch gapopen qlen qstart qend slen sstart send evalue bitscore"'
for i, test_genome in enumerate(test_genomes):
    # display(f'{i / len(test_genomes) * 100:.2f}%')
    # clear_output(wait=True)
    
    out_path = f'/data/mhoffert/genomes/GTDB_r207/pgap_ribosomal_results/{test_genome}'
    os.system(f'blastp -num_threads 4 -query {faa_path}{test_genome}_protein.faa -db {blast_db} -out {out_path}.blast6out -outfmt {blast6_fmt_str}')