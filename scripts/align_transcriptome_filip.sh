#!/bin/bash

#SBATCH --job-name=minimap2-thylaeodus
#SBATCH --mail-type=BEGIN,END,TIME_LIMIT_25,TIME_LIMIT_50,TIME_LIMIT_80,TIME_LIMIT
#SBATCH --cpus-per-task=32
#SBATCH --mem=60000M
#SBATCH --time=5:00:00
#SBATCH --mail-user=a01342234@unet.univie.ac.at
#SBATCH --output=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/thylaeodus_al>
#SBATCH --error=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/thylaeodus_ali>


# Script for aligning sequences (in this case for the thylaeodus transcriptome)



# Takes as input 2 fasta files ("$1", "$2") that are to be compared and have their sequences aligned.
# Specify Nr. of CPUs to be used using "$4" for runs on login server.
# Returns a .paf table with found alignments ("$3")

module load minimap2

TXOME=/lisc/scratch/zoology/thylaeodus/analysis/2025-04_asm_cluster/cluster.tsv
OUTPUT=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/transcripts_alignments_2nd.paf

/usr/bin/time minimap2 -t 32 -x asm20 -X -c -L --eqx $TXOME $TXOME > $OUTPUT

# Notes for clarification: -X   Equivalent to ’-DP --dual=no --no-long-join’. Primarily used for all-vs>
#                          -c   Generate CIGAR. In PAF, the CIGAR is written to the ‘cg’ custom tag.
#                          -x   Preset []. This option applies multiple options at the same time. It sh>
#                          -L   Write CIGAR with >65535 operators at the CG tag. Older tools are unable>
#                          --eqx    Output =/X CIGAR operators for sequence match/mismatch.
#                          -t INT   specify number of threads used
# If we reached this point, the assembly succeeded. We clean up resources.

# Delete tmp directory at the end
