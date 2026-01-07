#! /usr/bin/env python
import sys
import os
import argparse
import polars as pl


def main():
    p = argparse.ArgumentParser()
    p.add_argument('gtdb_tsvs', nargs='+')
    p.add_argument('-b', '--batch-size', default=1000)
    p.add_argument('-o', '--outdir', required=True)
    args = p.parse_args()

    try:
        os.mkdir(args.outdir)
    except:
        pass

    curbatch = 1
    n = 0
    outfp = open(args.outdir + f'/batch_{curbatch:05d}.txt', 'wt')
    print('accession,name', file=outfp)
    for tsv in args.gtdb_tsvs:
        df = pl.scan_csv(tsv, separator='\t').select(['accession']).collect()
        for acc in df['accession'].to_list():
            acc = acc[3:]
            print(f'{acc},{acc}', file=outfp)
            n += 1

            if n == args.batch_size:
                outfp.close()
                curbatch += 1
                n = 0
                outfp = open(args.outdir + f'/batch_{curbatch:05d}.txt', 'wt')
                print('accession,name', file=outfp)


if __name__ == '__main__':
    sys.exit(main())
