#! /usr/bin/env python
import sys
import os
import argparse
import polars as pl


def main():
    p = argparse.ArgumentParser()
    p.add_argument('gtdb_tsvs', nargs='+')
    p.add_argument('-o', '--output-file', required=True)
    args = p.parse_args()

    xx = []
    for tsv in args.gtdb_tsvs:
        df = pl.scan_csv(tsv, separator='\t', has_header=False,
                         new_columns=['accession', 'tax']).with_columns(
                (pl.col("tax").str.split(';').list.last()).alias("species"),
        ).collect()
        print(len(df))
        for row in df.iter_rows(named=True):
            accession = row["accession"][3:]
            species = row["species"]
            name = f"{accession} {species}"

            genome_filename = f"prodigal/{accession}.ffn"
            protein_filename = f"prodigal/{accession}.faa"

            xx.append(dict(name=name,
                           genome_filename=genome_filename,
                           protein_filename=protein_filename))

    out_df = pl.DataFrame(xx)
    out_df.write_csv(args.output_file)


if __name__ == '__main__':
    sys.exit(main())
