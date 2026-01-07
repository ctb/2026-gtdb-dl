# download multiple batches of accessions
for batch in batches/batch_*.txt
do
    sourmash scripts gbsketch $batch -f fasta -k --download-only -c 4 -v --no-overwrite-fasta -g
done
