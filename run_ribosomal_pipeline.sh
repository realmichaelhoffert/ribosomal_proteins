cd /data/mhoffert/tools/SparcleLabel/SparcleLabel-x64-linux
while read p; do
 
  ./rpsblast -parse_deflines -query /data/mhoffert/genomes/GTDB_r207/protein_faa_reps/bacteria/${p}_protein.faa -db /data/mhoffert/db/cdd/ribosomal_proteins -evalue 0.01 -outfmt 11 -out /data/mhoffert/genomes/GTDB_r207/pgap_ribosomal_results/$p.asn
  ./sparclbl -p precedences_sample.txt -o /data/mhoffert/genomes/GTDB_r207/pgap_ribosomal_results/$p.xml /data/mhoffert/genomes/GTDB_r207/pgap_ribosomal_results/$p.asn
  
done < $1
cd /data/mhoffert/realmichaelhoffert/ribosomal_proteins