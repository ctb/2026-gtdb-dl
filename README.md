# 2026-gtdb-dl

GTDB rs226 processing => prodigal.

All files on farm under `/home/ctbrown/scratch3/2026-gtdb-dl`.

## 0. Download the GTDB TSVs

You need:
```
ar53_metadata_r226.tsv.gz  bac120_metadata_r226.tsv.gz
ar53_taxonomy.tsv.gz       bac120_taxonomy.tsv.gz
```

## 1. Run `get-acc.py` to split the accessions into batches of ~1000

```
./get-acc.py *_metadata_tsv.gz
```

## 2. Run `cmd.sh` to use the directsketch plugin to download genomes in batches

```
./cmd.sh
```

## 3. Run `snakemake` to use prodigal to call genes on all genomes

(There's some tricky stuff here to get snakemake to run efficiently on 700,000 files.)

## 4. Run `tax-to-manysketch.py` to build a manysketch CSV to sketch everything

```
./tax-to-manysketch.py *_taxonomy.tsv.gz -o gtdb-cds-rs226.manysketch.csv
```

## 5. Run manysketch to sketch everything

```
sourmash scripts manysketch gtdb-cds-rs226.manysketch.csv -o gtdb-cds-rs226.sig.zip \
         -p dna,k=21,k=31,k=51
```

## 6. Run `pangenome.sh` to create the pangenome CDS, remove multihashes, and create a RocksDB database

```
./pangenome.sh
```

