## Set up SparcleLabel
Directions here: https://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/SparcleLabel/README

### Make `tools` directory
```
mkdir /data/mhoffert/tools/SparcleLabel
cd /data/mhoffert/tools/SparcleLabel
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/SparcleLabel/SparcleLabel-x64-linux.tar.gz
tar -xzf SparcleLabel-x64-linux.tar.gz
cd SparcleLabel-x64-linux/
wget https://ftp.ncbi.nih.gov/blast/executables/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz
tar -xzf ncbi-blast-2.13.0+-x64-linux.tar.gz
cp ncbi-blast-2.13.0+/bin/rpsblast ncbi-blast-2.13.0+/bin/rpstblastn .
mkdir db
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/little_endian/Cdd_LE.tar.gz && tar -xzf Cdd_LE.tar.gz -C ./db && rm -f Cdd_LE.tar.gz
mkdir data
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/cddid.tbl.gz -O ./data/cddid.tbl.gz && gzip -d ./data/cddid.tbl.gz
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/cdtrack.txt -O ./data/cdtrack.txt
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/family_superfamily_links -O ./data/family_superfamily_links
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/cddannot.dat.gz -O ./data/cddannot.dat.gz && gzip -d ./data/cddannot.dat.gz
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/cddannot_generic.dat.gz -O ./data/cddannot_generic.dat.gz && gzip -d ./data/cddannot_generic.dat.gz
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/bitscore_specific.txt -O ./data/bitscore_specific.txt
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/specific_arch.txt -O ./data/specific_arch.txt
wget https://ftp.ncbi.nih.gov/pub/mmdb/cdd/superfamily_arch.txt -O ./data/superfamily_arch.txt
```

### Custom db
```
makeprofiledb -title SMART.v6.0 -in Smart.pn -out Smart -threshold 9.82 -scale 100.0 -dbtype rps -index true
```
