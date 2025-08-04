#!/bin/bash

#SBATCH --job-name=cdhit-thylaeodus
#SBATCH --mail-type=BEGIN,END,TIME_LIMIT_25,TIME_LIMIT_50,TIME_LIMIT_80,TIME_LIMIT
#SBATCH --cpus-per-task=16
#SBATCH --mem=100000M
#SBATCH --time=5:00:00
#SBATCH --mail-user=a01342234@unet.univie.ac.at
#SBATCH --output=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/error_and_output/cd-hit_testing_paths2.out
#SBATCH --error=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/error_and_output/cd-hit_testing_paths2.err

# All against all self alignment script for thylaedous transcripts

module load cdhit/4.8.1

#INPUT=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/raw_data/transcripts.fasta
#OUTPUT=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/processed_data/cdhit_aligned_test
#OUTPUT2=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/processed_data/cdhit_aligned_test2
#OUTPUT3=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/processed_data/cdhit_aligned_test3

cd-hit-est -i transcripts.fasta -o transcripts_cluster_test1 -c 0.95 -n 10 -d 0 -M 100000 -T 16
cd-hit-est -i transcripts.fasta -j transcripts.fasta -o t_cluster_test2 -op t_cluster_test3 -P 1 -c 0.95 -n 10 -d 0 -M 100000 -T 16
