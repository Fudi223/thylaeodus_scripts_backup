#!/bin/bash

#SBATCH --job-name=cdhit-thylaeodus
#SBATCH --mail-type=BEGIN,END,TIME_LIMIT_25,TIME_LIMIT_50,TIME_LIMIT_80,TIME_LIMIT
#SBATCH --cpus-per-task=8
#SBATCH --mem=100000M
#SBATCH --time=5:00:00
#SBATCH --mail-user=a01342234@unet.univie.ac.at
#SBATCH --output=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/error_and_output/cd-hit_sett_testing.out
#SBATCH --error=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/error_and_output/cd-hit_sett_testing.err

# All against all self alignment script for thylaedous transcripts

module load cdhit/4.8.1 

#INPUT=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/raw_data/transcripts.fasta
#OUTPUT=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/processed_data/cdhit_aligned_test

cd-hit-est -i transcripts.fasta -o cd-hit_cluster -c 0.9 -d -M 100000 -T 8
cd-hit-est -i transcripts.fasta -j transcripts.fasta -o transcripts_95.fa  -op test_cluster_2 -P 0 -c 0.9 -n 10 -d -M 100000 -T 8 -sc -g 1 -B -p 1
