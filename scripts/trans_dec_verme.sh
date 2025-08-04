#!/bin/bash

#SBATCH --job-name=transdecoder-thylaeodus
#SBATCH --mail-type=BEGIN,END,TIME_LIMIT_25,TIME_LIMIT_50,TIME_LIMIT_80,TIME_LIMIT
#SBATCH --cpus-per-task=32
#SBATCH --mem=60000M
#SBATCH --time=5:00:00
#SBATCH --mail-user=a01342234@unet.univie.ac.at
#SBATCH --output=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/thylaeodus_t-deco.out
#SBATCH --error=/lisc/scratch/zoology/thylaeodus/analysis/2025-03_transcriptome_sampling/thylaeodus_t-deco.err


module load transdecoder

TransDecoder.LongOrfs -t transcripts.fasta
