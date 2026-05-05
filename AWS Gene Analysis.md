To analyze a large file, **~20 GB** on AWS, you move from raw data to biological insights using a structured pipeline of storage, high-memory compute, and specialized bioinformatics software.

**1. Setup & Storage (AWS S3 & SageMaker)**

- **Storage:** Upload your raw file (FASTQ/BAM) to **Amazon S3** ($0.023/GB).
- **Environment:** Launch **Amazon SageMaker** (Studio or RStudio).
    - **Crucial Step:** Increase your SSD storage from the default 5GB to **100GB+** to handle unzipped data and index files.
    - **Memory:** Use a memory-optimized instance like **r6i.xlarge** (32GB RAM) or **r6i.2xlarge** (64GB RAM).
- **Access:** Use the terminal command `aws s3 cp` to pull your file from S3 into your local SageMaker storage, or use **S3FS-FUSE** to mount the bucket like a local drive.

**2. Pre-Processing (Quality Control & Cleaning)**

- **Inspect:** Use `zcat file.fastq.gz | head` to peek at the data without unzipping.
- **QC:** Run **FastQC** to check for sequencing errors.
- **Clean:** Use **fastp** to automatically trim adapters and low-quality bases. This is the fastest way to "clean" a 20 GB file.

**3. Alignment (BWA-MEM)**

- **Map:** Align your cleaned reads to a reference genome (like hg38) using **BWA-MEM**.
- **Convert:** Pipe the output directly into **samtools** to convert the massive text-based SAM file into a compressed, sorted **BAM** file. This saves 80% of your disk space.

**4. Discovery (Variant Calling)**

- **Process:** Use **GATK (HaplotypeCaller)** to identify SNPs and Indels.
- **Cleanup:** Run **MarkDuplicates** to remove PCR artifacts and **BQSR** to recalibrate base quality scores for higher accuracy.
- **Output:** This generates a **VCF file**, which lists every mutation found.

**5. Interpretation (Annotation & CNV)**

- **Clinical Context:** Use **SnpEff** or **VEP** to cross-reference your VCF with databases like **ClinVar** to see which mutations are "Pathogenic."
- **Copy Numbers:** Use **CNVkit** or look at **Read Depth** in a viewer like IGV to check for extra chromosomes (Aneuploidy). An extra copy will show ~1.5x the normal coverage depth.