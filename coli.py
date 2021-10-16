import fire
from logging import getLogger, basicConfig, DEBUG
from os import system


log = getLogger('coli')
basicConfig(level=DEBUG)

def run(command):
    log.info(command)
    return system(command)


def assembly():
    run(
        "spades/bin/spades.py "
        "    -1 data/SRR292678sub_S1_L001_R1_001.fastq -2 data/SRR292678sub_S1_L001_R2_001.fastq "
        "    -o results/assembled "
    )

def mp_assembly():
    run(
        "spades/bin/spades.py "
        "    -1 data/SRR292678sub_S1_L001_R1_001.fastq -2 data/SRR292678sub_S1_L001_R2_001.fastq "
        "    --mp-1 1 data/SRR292862_S2_L001_R1_001.fastq --mp-2 1 data/SRR292862_S2_L001_R2_001.fastq "
        "    --mp-1 2 data/SRR292770_S1_L001_R1_001.fastq --mp-2 2 data/SRR292770_S1_L001_R2_001.fastq "
        "    -o results/assembled_mates "
    )


if __name__ == '__main__':
    fire.Fire()