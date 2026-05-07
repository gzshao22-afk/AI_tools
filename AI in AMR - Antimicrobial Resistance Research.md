

AI and computational modeling are transforming how we predict antimicrobial resistance (AMR) by ==moving from slow, culture-based laboratory tests to rapid, data-driven insights==. By analyzing massive datasets, these technologies identify patterns that humans cannot see, helping to select the right treatment instantly and uncovering the hidden genetic drivers of resistance. [[1](https://www.frontiersin.org/research-topics/73995/machine-learning-and-ai-driven-insights-into-microbial-pathogenesis-and-drug-resistance), [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12707637/), [3](https://www.sciencedirect.com/science/article/pii/S0025556422000384), [4](https://www.biorxiv.org/content/10.1101/2024.06.22.600223v1.full-text)]

**1. Predicting AMR Patterns**

AI models use two main types of data to forecast whether a specific drug will work against a pathogen: **genomic data** (the bacteria's DNA) and **clinical data** (patient history and hospital records). [[1](https://pmc.ncbi.nlm.nih.gov/articles/PMC11996750/), [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12081381/), [3](https://www.youtube.com/watch?v=OJsZM6ZcgB4&t=35), [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC12859369/)]

- **Genotype-to-Phenotype Prediction:** AI can "read" a pathogen's genome to predict its resistance level without waiting for it to grow in a lab.
    - **How it works:** Machine learning models like **Random Forest** or **XGBoost** are trained on thousands of known bacterial genomes paired with their lab-tested resistance levels. The model learns which specific genetic mutations or genes correlate with drug failure.
    - **Example:** A study using the **Pfizer ATLAS dataset** applied XGBoost to predict resistance for single drug-bug combinations with up to **95% accuracy**.
- **Clinical Decision Support:** AI analyzes Electronic Health Records (EHR) to predict resistance _before_ any lab results are available.
    - **How it works:** Models look at factors like a patient's age, past antibiotic use, and local "colonization pressure" (how common resistance is in that specific hospital ward).
    - **Example:** Researchers at [Massachusetts General Hospital](https://www.nature.com/articles/s44259-023-00015-2) used models to predict resistance in complicated urinary tract infections (UTIs), reducing mismatched treatments by nearly **42%** compared to traditional physician decisions. [[1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10044642/), [2](https://www.nature.com/articles/s41598-025-14078-w), [3](https://www.youtube.com/watch?v=tZtBn2o_qgc&t=516), [4](https://www.nature.com/articles/s44259-023-00015-2), [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC11791014/)]

**2. Understanding Resistance Mechanisms**

Computational modeling doesn't just predict _if_ resistance exists; it explains _why_ and _how_ it evolves. [[1](https://academic.oup.com/evolut/article/79/9/1900/8155086)]

- **Molecular Dynamics (MD) Simulations:** These models act like "virtual microscopes" to show how antibiotics interact with bacterial structures at an atomic level.
    - **Example:** Researchers use MD to study how the **bacterial cell envelope** changes to block drugs or how "efflux pumps" physically eject antibiotics from the cell.
- **Explainable AI (XAI):** Newer AI tools use "interpretability layers" to tell scientists exactly which genes they are looking at to make a prediction.
    - **Example:** Using **SHAP analysis**, scientists identified that specific mutations (like `katG` for tuberculosis) were the primary drivers of resistance to first-line drugs like Isoniazid. This helps researchers identify **new targets** for future drug development. [[1](https://journals.asm.org/doi/10.1128/cmr.00179-21), [2](https://pubs.acs.org/doi/10.1021/acsomega.0c05590), [3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12255030/), [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC11564165/), [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC11359845/)]

**Summary of AI Tools & Examples**

|Application [[1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12255030/), [2](https://www.nature.com/articles/s44259-023-00015-2), [3](https://www.nature.com/articles/s41598-025-91190-x), [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC11791014/), [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC9312204/)]|AI/Computational Tool|Real-World Example/Impact|
|---|---|---|
|**TB Diagnosis**|Gradient Boosting Classifier|Predicted multi-drug resistant Tuberculosis (MTB) with over **97% accuracy** using DNA markers.|
|**UTI Treatment**|Logistic Regression / TabNet|Reduced the use of broad-spectrum antibiotics by identifying patients who only needed narrow-spectrum drugs.|
|**Drug Discovery**|Graph Convolutional Networks|Screened vast chemical libraries to find molecules with potent antimicrobial properties, avoiding the "rediscovery" of old drugs.|
|**Outbreak Tracking**|Sequence-based ML|The [EDS-HAT system](https://pmc.ncbi.nlm.nih.gov/articles/PMC11791014/) uses genomic data to identify transmission routes of "superbugs" within hospitals in real-time.|

### ATLAS dataset
The **ATLAS (Antimicrobial Testing Leadership and Surveillance)** dataset, established by **[Pfizer](https://www.pfizer.com/science/focus-areas/anti-infectives/antimicrobial-surveillance)**, is one of the world's largest open-access resources for antimicrobial resistance data. You can access it through two primary channels depending on your needs: [[1](https://wellcomeopenresearch.org/articles/9-274), [2](https://www.pfizer.com/news/press-release/press-release-detail/pfizer_unveils_atlas_an_interactive_user_friendly_website_that_provides_global_antibiotic_resistance_surveillance_data_across_60_countries)]

**1. Interactive Visualization (For Quick Analysis)**

If you want to explore the data without downloading raw files, Pfizer provides a user-friendly interactive platform. [[1](https://www.pfizer.com/science/focus-areas/anti-infectives/antimicrobial-surveillance)]

- **Website:** [atlas-surveillance.com](https://atlas-surveillance.com/)
- **What you can do:** Filter by pathogen, region, and antibiotic to generate real-time tables, maps, and figures.
- **Access:** Registration is required for free "open access". [[1](https://www.amrindustryalliance.org/case-study/antimicrobial-testing-leadership-and-surveillance-atlas/), [2](https://atlas-surveillance.com/), [3](https://www.pfizer.com/news/press-release/press-release-detail/pfizer_unveils_atlas_an_interactive_user_friendly_website_that_provides_global_antibiotic_resistance_surveillance_data_across_60_countries), [4](https://globalhealthprogress.org/collaboration/pfizer-global-antimicrobial-surveillance-programs/)]

**2. Raw Dataset for AI Research (For Machine Learning)**

For computational modeling or large-scale data analysis, you must request the **de-identified raw data** through the **[Vivli AMR Register](https://amr.vivli.org/)**. [[1](https://wellcomeopenresearch.org/articles/9-273)]

- **Platform:** Vivli AMR Register
- **Direct Link:** Pfizer ATLAS Dataset on Vivli
- **Request Process:**
    1. Create an account on the Vivli platform.
    2. Submit a research proposal summarizing your goals.
    3. State how your research will improve patient outcomes or antibiotic stewardship.
    4. Once approved, the data becomes available for download based on your specific selection criteria. [[1](https://amr.vivli.org/ourmember/pfizer/), [2](https://wellcomeopenresearch.org/articles/9-273), [3](https://www.nature.com/articles/s41598-025-14078-w)]

Highthroughput Screening of LNP-AMR, Comparing with ATLAS database