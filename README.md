# ribosomal_proteins

### Making bacterial ribosomal protein annotations more accessible
A pipeline based on the RefSeq Prokaryotic Genome Annotation Pipeline (PGAP), designed to rapidly annotate the presence of ribosomal proteins in bacterial genomes. This project was motivated by the fact that [gRodon](https://github.com/jlw-ecoevo/gRodon) uses RefSeq PGAP annotations of ribosomal proteins, but PGAP can take up to 6 hours to run for moderately sized genomes. This pipeline currently achieves a correlation of 0.91 with EGGO estimated growth rates, taking approximately 25 seconds to completely annotate the ribosomal proteins in each genome.

## Sparcle documentation
https://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/SparcleLabel/README
## Database links
https://ftp.ncbi.nih.gov/pub/blastrules/RELEASE_4.0/
https://ftp.ncbi.nih.gov/hmm/current/
https://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/SparcleLabel/README
https://ftp.ncbi.nih.gov/blast/executables/LATEST/
