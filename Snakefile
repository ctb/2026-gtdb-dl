#G, = glob_wildcards('{acc}_genomic.fna.gz')

G = []

# only load accessions that are in fasta-list.txt but not in
# prodigal-list.uniq.
found = set()
for acc in open('prodigal-list.uniq'):
    found.add(acc.strip())

for filename in open('fasta-list.txt'):
    filename = '_'.join(filename.split('_', 2)[:2])
    if filename not in found:
        G.append(filename)

print(f'found {len(G)} left.')

rule all:
    input:
        expand("prodigal/{g}.ffn", g=G),
        
rule prodigal:
    input:
        g="fasta/{g}_genomic.fna.gz",
    output:
        ffn="prodigal/{g}.ffn",
        faa="prodigal/{g}.faa",
    threads: 1
    shell: """
        prodigal -i {input.g} -d {output.ffn} -a {output.faa} -o /dev/null
    """
