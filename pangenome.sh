#sourmash scripts pangenome_createdb gtdb-cds-rs226.sig.zip -t /group/ctbrowngrp5/sourmash-db.new/gtdb-rs226/gtdb-rs226.lineages.sqldb -k 21 -o gtdb-cds-rs226.species.sig.zip

#mkdir -p singleton
#../2025-workflow-core99/scripts/remove-multihash-by-sig.py gtdb-cds-rs226.species.sig.zip -k 21 -o singleton/
#mv singleton/gtdb-cds-rs226.species.sig.zip    gtdb-cds-rs226.species.singleton.sig.zip

sourmash index -F rocksdb gtdb-cds-rs226.species.singleton.rocksdb gtdb-cds-rs226.species.singleton.sig.zip -k 21
