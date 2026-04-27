
> Covering PI3K/AKT, GPCR, JAK/STAT, NF-κB, MAPK/ERK, mTOR, p53, and Toll-Like Receptor pathways — their roles in cell growth, metabolism, apoptosis, immune response, and cross-pathway interactions.

---

## Table of Contents

1. [PI3K/AKT Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#1-pi3kakt-pathway)
2. [GPCR Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#2-gpcr-pathway)
3. [JAK/STAT Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#3-jakstat-pathway)
4. [NF-κB Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#4-nf-%CE%BAb-pathway)
5. [MAPK/ERK Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#5-mapkerk-pathway)
6. [mTOR Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#6-mtor-pathway)
7. [p53 Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#7-p53-pathway)
8. [Toll-Like Receptor (TLR) Pathway](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#8-toll-like-receptor-tlr-pathway)
9. [Cross-Pathway Interactions & Network Integration](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#9-cross-pathway-interactions--network-integration)
10. [Summary Table](https://claude.ai/chat/64c3109a-2735-47df-a3cf-bde24987040c#10-summary-table)

---

## 1. PI3K/AKT Pathway

### Overview

The Phosphoinositide 3-Kinase (PI3K) / AKT (Protein Kinase B) pathway is one of the most frequently activated signaling cascades in human cancer and a central regulator of cell survival, growth, and metabolism.

### Activation Mechanism

1. **Receptor Tyrosine Kinase (RTK) activation**: Growth factors (e.g., EGF, PDGF, insulin) bind RTKs, triggering autophosphorylation.
2. **PI3K recruitment**: The p85 regulatory subunit of PI3K docks onto phosphorylated tyrosine residues, activating the p110 catalytic subunit.
3. **PIP3 production**: PI3K phosphorylates PIP2 → **PIP3** at the plasma membrane.
4. **AKT activation**: PIP3 recruits AKT and PDK1 to the membrane; PDK1 phosphorylates AKT at Thr308, and mTORC2 phosphorylates AKT at Ser473 for full activation.
5. **PTEN as negative regulator**: PTEN phosphatase converts PIP3 back to PIP2, acting as a tumor suppressor.

### Roles

|Function|Mechanism|
|---|---|
|**Cell Growth**|AKT phosphorylates and inhibits TSC1/2, activating mTORC1 → protein synthesis and ribosome biogenesis|
|**Metabolism**|Promotes GLUT4 translocation; activates hexokinase and PFK; inhibits gluconeogenesis via GSK3β|
|**Anti-Apoptosis**|Phosphorylates BAD (inactivating it); activates MDM2 to suppress p53; inhibits FOXO transcription factors|
|**Cell Cycle**|Promotes cyclin D1 expression via GSK3β inhibition; drives G1/S transition|

### Key Effectors

- **GSK3β** — inhibited by AKT; when released, promotes apoptosis and suppresses glycogen synthesis
- **FOXO transcription factors** — when phosphorylated by AKT, excluded from nucleus; when active, induce apoptosis and cell cycle arrest
- **MDM2** — activated by AKT; ubiquitinates and degrades p53
- **mTORC1** — downstream effector (see mTOR section)

---

## 2. GPCR Pathway

### Overview

G Protein-Coupled Receptors (GPCRs) are the largest family of cell-surface receptors (~800 members in humans). They transduce extracellular signals — hormones, neurotransmitters, odorants, photons — into intracellular responses via heterotrimeric G proteins (Gα, Gβ, Gγ).

### Activation Mechanism

1. **Ligand binding** causes conformational change in the GPCR.
2. **G protein activation**: The receptor acts as a GEF, catalyzing GDP → GTP exchange on Gα, causing dissociation of Gα-GTP from Gβγ.
3. **Signal branching**: Both Gα-GTP and free Gβγ activate downstream effectors.
4. **Termination**: Gα hydrolyzes GTP → GDP (intrinsic GTPase); arrestin binding desensitizes the receptor.

### G Protein Subtypes and Their Effects

|Subtype|Effector|Second Messenger|Cellular Effect|
|---|---|---|---|
|**Gαs**|Adenylyl cyclase ↑|cAMP ↑|PKA activation → gene transcription, metabolism|
|**Gαi**|Adenylyl cyclase ↓|cAMP ↓|Inhibits PKA; opens K⁺ channels|
|**Gαq**|PLCβ ↑|IP3 + DAG ↑|IP3 → Ca²⁺ release; DAG → PKC activation|
|**Gα12/13**|RhoGEF|RhoA ↑|Cytoskeletal reorganization|

### Roles

- **Cell Growth**: Gαs/cAMP/PKA axis activates CREB → mitogenic gene expression. Gβγ can activate PI3K directly.
- **Metabolism**: GPCRs regulate glucose homeostasis (glucagon, GLP-1 receptors), lipolysis (β-adrenergic), and energy sensing.
- **Apoptosis**: Depending on context, GPCRs can be pro-survival (via PI3K/AKT) or pro-apoptotic (via Gαi and Ca²⁺ overload).
- **Immune Response**: Chemokine receptors (CXCR4, CCR5) are GPCRs; direct leukocyte migration, mast cell degranulation, and inflammatory mediator release.

---

## 3. JAK/STAT Pathway

### Overview

The Janus Kinase (JAK) / Signal Transducer and Activator of Transcription (STAT) pathway is the primary signaling route for cytokines, interferons, and growth hormones. It links extracellular signals directly to gene transcription.

### Activation Mechanism

1. **Cytokine binding** (e.g., IL-6, IFN-γ, EPO) to receptors that lack intrinsic kinase activity.
2. **JAK trans-phosphorylation**: Receptor dimerization brings two receptor-associated JAKs (JAK1, JAK2, JAK3, TYK2) into proximity; they trans-activate each other.
3. **Receptor phosphorylation**: JAKs phosphorylate tyrosines on the receptor cytoplasmic tail, creating docking sites.
4. **STAT recruitment and activation**: STAT proteins dock via their SH2 domains, are phosphorylated by JAKs, dimerize, and translocate to the nucleus.
5. **Negative regulation**: SOCS proteins (Suppressor of Cytokine Signaling) provide feedback inhibition by binding JAKs and targeting receptors for degradation. PIAS proteins inhibit STAT binding to DNA.

### Key STATs and Their Targets

|STAT|Primary Activators|Target Genes / Functions|
|---|---|---|
|STAT1|IFN-α/β, IFN-γ|Antiviral ISGs; MHC-I/II expression|
|STAT2|IFN-α/β|Antiviral defense (ISGF3 complex)|
|STAT3|IL-6, IL-10, EGF|Bcl-2, Bcl-xL (anti-apoptosis); VEGF; cyclin D1|
|STAT4|IL-12|Th1 differentiation; IFN-γ production|
|STAT5a/b|IL-2, EPO, GH, Prolactin|Cell proliferation; erythropoiesis|
|STAT6|IL-4, IL-13|Th2 differentiation; IgE class switching|

### Roles

- **Cell Growth**: STAT3 and STAT5 are oncogenic when constitutively activated; they drive cyclin D1, c-Myc, and Bcl-2 expression.
- **Metabolism**: STAT5 mediates GH effects on liver metabolism; STAT3 regulates gluconeogenesis and lipid metabolism.
- **Apoptosis**: STAT3 strongly anti-apoptotic (upregulates Bcl-2, survivin); STAT1 can be pro-apoptotic in response to IFN.
- **Immune Response**: Central hub for innate and adaptive immunity — antiviral (STAT1/2), Th cell polarization (STAT4/6), regulatory T cell function (STAT5).

---

## 4. NF-κB Pathway

### Overview

Nuclear Factor kappa-light-chain-enhancer of activated B cells (NF-κB) is a master transcription factor controlling inflammation, immunity, cell survival, and stress responses. Dysregulation is implicated in many cancers and inflammatory diseases.

### Family Members

NF-κB consists of homo- or heterodimers of five subunits: **RelA (p65), RelB, c-Rel, p50/p105, p52/p100**.

### Canonical Pathway

1. **Stimulus**: TNF-α, IL-1β, LPS, antigen receptor signaling, genotoxic stress.
2. **IKK complex activation**: Stimulus activates TAK1 → IKK complex (IKKα/IKKβ/NEMO).
3. **IκB phosphorylation**: IKKβ phosphorylates IκBα at Ser32/36 → polyubiquitination → proteasomal degradation.
4. **NF-κB nuclear translocation**: Free p65/p50 heterodimer enters nucleus, binds κB sites.
5. **Target gene transcription**: TNF-α, IL-6, IL-8, COX-2, iNOS, Bcl-2, XIAP, cyclin D1.

### Non-Canonical Pathway

Activated by BAFF, CD40L, LTβ → NIK activation → IKKα homodimer → p100 processing → p52/RelB dimer → lymphoid organ development, B-cell maturation.

### Roles

- **Cell Growth**: Induces cyclin D1, c-Myc; suppresses CDK inhibitors. Constitutive NF-κB activation is a hallmark of many cancers.
- **Metabolism**: Promotes inflammatory metabolic reprogramming (Warburg effect in immune cells); regulates adipogenesis and insulin sensitivity.
- **Apoptosis**: **Pro-survival** via Bcl-2, Bcl-xL, XIAP, cIAP1/2, and cFLIP. Can suppress p53-mediated apoptosis. However, in some contexts (e.g., JNK co-activation) can become pro-apoptotic.
- **Immune Response**: Master regulator — activates macrophages, DCs, T and B cells; drives acute phase response; central to innate immune memory.

---

## 5. MAPK/ERK Pathway

### Overview

The Mitogen-Activated Protein Kinase (MAPK) pathway is a conserved cascade that translates extracellular signals into proliferation, differentiation, survival, and stress responses. The ERK1/2 branch is the most studied.

### Core Cascade: RAS → RAF → MEK → ERK

1. **RAS activation**: Growth factor → RTK → Grb2/SOS → RAS-GDP → RAS-GTP.
2. **RAF activation**: RAS-GTP recruits and activates RAF (BRAF, CRAF).
3. **MEK1/2 phosphorylation**: RAF phosphorylates MEK1/2 (dual specificity kinases).
4. **ERK1/2 activation**: MEK phosphorylates ERK1/2 on Thr and Tyr.
5. **Nuclear translocation**: Activated ERK translocates to nucleus; phosphorylates transcription factors (ELK1, c-Fos, c-Jun, c-Myc).

### Parallel MAPK Branches

|Branch|Activators|Core Kinases|Functions|
|---|---|---|---|
|**ERK1/2**|Growth factors, mitogens|RAS→RAF→MEK→ERK|Proliferation, differentiation|
|**JNK (SAPK)**|Stress, cytokines (TNF, IL-1)|MEKK1→MKK4/7→JNK|Apoptosis, inflammation, stress response|
|**p38 MAPK**|Inflammatory cytokines, stress, UV|ASK1→MKK3/6→p38|Inflammation, cell cycle arrest, differentiation|
|**ERK5**|Growth factors, stress|MEKK2/3→MEK5→ERK5|Survival, cardiac hypertrophy|

### Roles

- **Cell Growth**: ERK1/2 phosphorylates RSK → S6K and ELK1 → immediate early genes (c-Fos, Egr-1) → cyclin D1 upregulation → G1 progression.
- **Metabolism**: ERK regulates GLUT expression, glycolytic enzyme activity, and mitochondrial function through PGC-1α phosphorylation.
- **Apoptosis**: ERK is generally **anti-apoptotic** (phosphorylates and inactivates BAD, Bim). JNK and p38 are **pro-apoptotic** — activate c-Jun/AP-1 → FasL and Bim expression; phosphorylate Bcl-2 (inhibiting it).
- **Immune Response**: p38 and JNK are essential for cytokine production (TNF-α, IL-1β, IL-6) in macrophages. ERK regulates DC maturation and T cell activation threshold.

### BRAF V600E Mutation

The oncogenic BRAF V600E mutation constitutively activates ERK signaling independent of RAS, and is targeted by vemurafenib and dabrafenib in melanoma.

---

## 6. mTOR Pathway

### Overview

The mechanistic Target of Rapamycin (mTOR) is a serine/threonine kinase that serves as a master regulator of cell growth, metabolism, autophagy, and aging. It forms two distinct complexes: **mTORC1** and **mTORC2**.

### mTOR Complexes

|Feature|mTORC1|mTORC2|
|---|---|---|
|Unique components|Raptor, PRAS40|Rictor, mSin1|
|Rapamycin sensitivity|Acutely sensitive|Resistant (acute); sensitive (chronic)|
|Key activators|Amino acids, growth factors, energy|Growth factors (PI3K-dependent)|
|Key substrates|S6K1, 4E-BP1|AKT (Ser473), SGK1, PKCα|
|Primary functions|Protein synthesis, lipogenesis, autophagy inhibition|Cytoskeleton, AKT activation, metabolism|

### mTORC1 Activation

- **Nutrients (amino acids)**: Sensed by the Ragulator-RAG GTPase complex → mTORC1 recruited to lysosome.
- **Growth factors**: PI3K/AKT → phosphorylates and inhibits TSC1/2 complex → RHEB-GTP → mTORC1 activation.
- **Energy status**: AMPK (activated by low ATP) → phosphorylates TSC2 and Raptor → **inhibits** mTORC1.
- **Oxygen/redox**: Hypoxia → REDD1 → TSC1/2 activation → mTORC1 inhibition.

### mTORC1 Effectors

- **S6K1 (p70 S6 Kinase)**: Promotes ribosome biogenesis, mRNA translation, and feedback-inhibits IRS-1 (negative feedback to PI3K/AKT).
- **4E-BP1**: Phosphorylation releases eIF4E → cap-dependent mRNA translation.
- **ULK1**: Phosphorylation **inhibits** ULK1 → suppresses autophagy initiation.
- **TFEB**: Cytoplasmic sequestration → suppresses lysosomal biogenesis genes.

### Roles

- **Cell Growth**: mTORC1 is the primary anabolic switch — integrates nutrient, energy, and growth factor signals to promote protein and lipid synthesis.
- **Metabolism**: Promotes glycolysis (HIF-1α stabilization), lipogenesis (SREBP1c activation), and mitochondrial biogenesis. Also inhibits autophagy, blocking recycling of macromolecules.
- **Apoptosis**: mTORC1 is generally **anti-apoptotic** — promotes survival protein translation. Hyperactivation can paradoxically induce apoptosis via S6K1 feedback and AKT suppression.
- **Immune Response**: Regulates T-cell differentiation (mTORC1 → Th1/Th17; mTORC2 → Th2/Treg), DC function, and macrophage polarization.

### Rapamycin and Resistance in Yeast

Rapamycin (sirolimus) binds FKBP12 → the complex inhibits mTORC1 by blocking Raptor interaction. In yeast (_Saccharomyces cerevisiae_), TOR1 and TOR2 perform mTORC1 and mTORC2 functions respectively. Yeast **mitigate rapamycin effects** through:

1. **TOR2** (mTORC2 analog) is intrinsically rapamycin-resistant, maintaining essential actin cytoskeletal functions.
2. **Overexpression of TOR1** — increased TOR1 titrates away the rapamycin/FKBP12 complex.
3. **FPR1 deletion** (yeast FKBP12) — without FKBP12, rapamycin cannot form the inhibitory complex.
4. **Gain-of-function TOR1 mutations** (e.g., TOR1-1, S1972R in the FRB domain) prevent FKBP12-rapamycin docking.
5. **Tap42/PP2A regulation**: Yeast activate Tap42-associated phosphatases as compensatory signals when TOR is inhibited.

---

## 7. p53 Pathway

### Overview

p53 (TP53) is the most frequently mutated gene in human cancers (~50% of tumors). It functions as a **"guardian of the genome"** — a transcription factor activated by cellular stress to coordinate DNA repair, cell cycle arrest, senescence, or apoptosis.

### Activation Mechanism

1. **Under normal conditions**: p53 is kept at low levels by MDM2 (an E3 ubiquitin ligase that ubiquitinates p53 → proteasomal degradation). MDM2 is itself transcriptionally induced by p53 (negative feedback loop).
2. **Stress signals** (DNA damage, oncogene activation, hypoxia, ribosomal stress):
    - **DNA DSBs** → ATM/ATR → CHK1/CHK2 → phosphorylate p53 at Ser15/20 → disrupts MDM2 binding → p53 stabilization.
    - **ARF** (p14ARF/p19ARF): Induced by oncogenes (RAS, c-Myc); sequesters MDM2 in nucleolus → stabilizes p53.
3. **Tetrameric p53** binds p53 response elements (p53REs) in target gene promoters.

### p53 Target Genes and Outcomes

|Outcome|Target Genes|Mechanism|
|---|---|---|
|**G1 arrest**|p21 (CDKN1A)|Inhibits CDK2/4/6 → Rb hypophosphorylation → E2F inhibition|
|**G2/M arrest**|14-3-3σ, GADD45|Sequesters CDC25C; activates checkpoint kinases|
|**Apoptosis (intrinsic)**|PUMA, NOXA, BAX|BH3-only proteins activate BAX/BAK → cytochrome c → caspase-9|
|**Apoptosis (extrinsic)**|FasL, DR5/KILLER|Death receptor upregulation → caspase-8|
|**Senescence**|p21, PAI-1|Permanent cell cycle exit|
|**DNA repair**|PCNA, DDB2, XPC|Nucleotide excision repair components|
|**Metabolism**|TIGAR, GLS2|Reduces glycolysis; enhances mitochondrial respiration|
|**Autophagy**|DRAM, Sestrin 1/2|Promotes autophagy; activates AMPK|

### Roles

- **Cell Growth**: p53 is fundamentally **anti-proliferative** — arrests the cell cycle at G1 and G2/M checkpoints to allow damage repair.
- **Metabolism**: Opposes the Warburg effect by suppressing glycolysis (TIGAR) and promoting oxidative phosphorylation. Activates AMPK via Sestrins.
- **Apoptosis**: The central apoptosis inducer in response to irreparable damage — activates both intrinsic (mitochondrial) and extrinsic (death receptor) pathways.
- **Immune Response**: p53 activates innate immune signaling by inducing interferons and STING pathway components. Also modulates immune evasion — p53 loss reduces antigen presentation and innate immune sensing.

---

## 8. Toll-Like Receptor (TLR) Pathway

### Overview

Toll-Like Receptors (TLRs) are pattern recognition receptors (PRRs) of the innate immune system. They detect conserved **PAMPs** (Pathogen-Associated Molecular Patterns) and **DAMPs** (Danger-Associated Molecular Patterns) to initiate inflammatory and antiviral responses.

### TLR Family and Ligands

|TLR|Location|Ligand (PAMP)|Pathogen|
|---|---|---|---|
|TLR1/2|Cell surface|Triacyl lipopeptides|Bacteria|
|TLR2/6|Cell surface|Diacyl lipopeptides, LTA|Mycoplasma, gram+|
|TLR3|Endosome|dsRNA|Viruses|
|TLR4|Cell surface|LPS|Gram-negative bacteria|
|TLR5|Cell surface|Flagellin|Bacteria|
|TLR7/8|Endosome|ssRNA|Viruses|
|TLR9|Endosome|CpG DNA|Bacteria, viruses|

### Signaling Pathways

**MyD88-dependent (all TLRs except TLR3):**

1. TLR activation → MyD88/TIRAP recruitment.
2. MyD88 recruits IRAK4 → IRAK1/2 activation.
3. TRAF6 ubiquitination → TAK1 activation.
4. **TAK1** bifurcates into:
    - IKK complex → **NF-κB** activation → pro-inflammatory cytokines (TNF, IL-6, IL-12).
    - MKK3/6/4/7 → **p38/JNK** (MAPK) → AP-1 activation → cytokine amplification.

**TRIF-dependent (TLR3, TLR4):**

1. TRIF/TRAM recruitment.
2. TRAF3 → TBK1/IKKε → **IRF3/7 phosphorylation** → dimerization → nuclear translocation → **Type I IFN** (IFN-α/β) production.
3. TRIF → RIPK1 → NF-κB and apoptosis (FADD/Caspase-8).

### Roles

- **Cell Growth**: Generally anti-proliferative in immune cells (drives differentiation). In epithelial/tumor cells, TLR4 can paradoxically promote tumor growth via NF-κB.
- **Metabolism**: TLR4 activation by LPS drives inflammatory metabolic reprogramming in macrophages (glycolytic shift, succinate accumulation → HIF-1α → IL-1β). Implicated in obesity-associated inflammation via LPS from gut microbiome.
- **Apoptosis**: TRIF signaling can induce apoptosis via RIPK1-FADD-Caspase-8. TLR signals can also activate NLRP3 inflammasome → pyroptosis (inflammatory caspase-1-dependent cell death).
- **Immune Response**: Core function — activates innate immunity, bridges innate and adaptive responses via DC maturation and cytokine milieu that shapes T helper cell polarization.

---

## 9. Cross-Pathway Interactions & Network Integration

These pathways do not operate in isolation. They form a densely interconnected signaling network with extensive crosstalk.

### Key Interaction Nodes

#### AKT as a Master Integrator

- **AKT → mTORC1**: AKT phosphorylates and inhibits TSC2 → activates RHEB → mTORC1.
- **AKT → NF-κB**: AKT activates IKKα → IκB degradation → NF-κB.
- **AKT → p53**: AKT activates MDM2 → p53 degradation (AKT suppresses p53-mediated apoptosis).
- **AKT → FOXO**: Phosphorylates FOXO → nuclear exclusion → suppresses pro-apoptotic gene expression.
- **S6K1 → IRS-1 (negative feedback)**: mTORC1/S6K1 phosphorylates IRS-1 → degrades PI3K signal (insulin resistance mechanism).

#### RAS/MAPK and PI3K/AKT Parallel Activation

- RTKs simultaneously activate both RAS→ERK and PI3K→AKT; both are required for full mitogenic response.
- **RAS → PI3K** (direct interaction): Oncogenic RAS can directly activate PI3K, explaining why RAS mutations are hard to target with single-pathway inhibitors.
- **ERK → mTORC1**: ERK can directly phosphorylate TSC2 and RSK, converging on mTOR.

#### NF-κB and MAPK Cooperation

- **JNK + NF-κB balance determines apoptotic fate**: NF-κB activation is pro-survival; sustained JNK activation with NF-κB suppression → apoptosis (relevant in TNF signaling).
- **TAK1** (in TLR pathway) activates both NF-κB and MAPK simultaneously.

#### p53 and the Other Pathways

- **p53 ↔ NF-κB**: Mutual antagonism — they compete for limiting transcriptional co-activators (p300/CBP); NF-κB can directly repress p53 transcription.
- **p53 ↔ mTOR**: p53 activates AMPK (via Sestrins) and PTEN → inhibits mTOR. mTOR suppression in turn reduces HIF-1α and MDM2, creating a feedback loop that can either stabilize or destabilize p53 depending on context.
- **p53 ↔ PI3K/AKT**: PTEN (activated transcriptionally by p53) is the major brake on PI3K/AKT. AKT activates MDM2 to suppress p53.

#### JAK/STAT and Other Pathways

- **STAT3 and NF-κB co-regulation**: Both are activated by IL-6 via IL-6R/gp130; STAT3 and NF-κB can form heterocomplexes on some promoters (e.g., IL-6 itself → feed-forward loop in inflammation).
- **IFN/STAT1 and mTOR**: STAT1-driven ISG expression requires mTORC1 for translation of antiviral effectors; mTOR inhibition reduces IFN antiviral efficacy.
- **STAT3 and mTOR in cancer**: Both are commonly co-activated in tumors; STAT3 drives transcription of cyclin D1 while mTOR drives its translation.

#### TLR Pathway Convergence

- TLR4/MyD88 → **NF-κB** (shared with TNF and IL-1 signaling).
- TLR3/TRIF → **IRF3** → Type I IFN → **JAK/STAT** (IFNAR → JAK1/TYK2 → STAT1/STAT2 → ISG expression).
- LPS/TLR4 → PI3K/AKT activation (via TIRAP) → limits excessive inflammation (regulatory role).

#### GPCR Integration

- Gβγ subunits can directly activate PI3Kγ (class IB PI3K) — coupling GPCRs to the AKT/mTOR axis.
- cAMP/PKA can activate or inhibit RAF depending on cell type — in some cells PKA activates BRAF; in others it phosphorylates CRAF at an inhibitory site.
- GPCRs can transactivate RTKs (e.g., EGFR) via metalloprotease-mediated EGF shedding → full MAPK and PI3K activation downstream.

### The Apoptotic Decision Network

```
  DNA Damage / Stress
         |
    [p53 activation]
    /            \
[p21 → Arrest]  [PUMA/NOXA/BAX]
                       |
              [Bcl-2/Bcl-xL] ←── AKT, NF-κB, STAT3 (survival)
                  |  ↑
         [Cytochrome c release]
                  |
         [Apoptosome → Casp-9]
                  |
         [Effector Caspases 3/7]
                  |
              [Apoptosis]
```

Anti-apoptotic signals from PI3K/AKT, NF-κB, and JAK/STAT3 converge on the Bcl-2 family to oppose p53- and stress-driven cell death.

---

## 10. Summary Table

|Pathway|Primary Activators|Cell Growth|Metabolism|Apoptosis|Immune Response|
|---|---|---|---|---|---|
|**PI3K/AKT**|Growth factors, RTKs|↑ (cyclin D1, mTOR)|↑ Glycolysis, GLUT4|Anti (BAD, MDM2, FOXO)|Lymphocyte survival, activation|
|**GPCR**|Hormones, neurotransmitters|Context-dependent|Energy homeostasis|Context-dependent|Chemotaxis, degranulation|
|**JAK/STAT**|Cytokines, interferons|↑ (STAT3/5 → cyclin D1)|GH/insulin signaling|Anti (STAT3 → Bcl-2)|Core cytokine signaling hub|
|**NF-κB**|TNF, IL-1, LPS, stress|↑ (cyclin D1, c-Myc)|Warburg, adipogenesis|Anti (Bcl-2, XIAP)|Master inflammatory regulator|
|**MAPK/ERK**|Mitogens, stress|↑ ERK; ↓ JNK/p38|Glycolysis, mitochondria|ERK anti; JNK/p38 pro|Cytokine production, DC maturation|
|**mTOR**|Nutrients, growth factors|↑↑ (protein/lipid synthesis)|↑ Anabolic; ↓ Autophagy|Anti (survival proteins)|T-cell differentiation, DC function|
|**p53**|DNA damage, oncogene stress|↓↓ (p21, cell cycle arrest)|↑ OXPHOS; ↓ Glycolysis|Pro (PUMA, BAX)|IFN induction, immune evasion control|
|**TLR**|PAMPs, DAMPs|Context-dependent|Metabolic reprogramming|Pro (TRIF/pyroptosis)|Innate immunity, APC activation|

---

## Key Therapeutic Targets Summary

|Pathway|Drug Class|Examples|Clinical Use|
|---|---|---|---|
|PI3K/AKT|PI3K inhibitors|Idelalisib, Copanlisib|CLL, NHL, breast cancer|
|PI3K/AKT|AKT inhibitors|Capivasertib, Ipatasertib|Breast, prostate cancer|
|MAPK/ERK|BRAF inhibitors|Vemurafenib, Dabrafenib|Melanoma|
|MAPK/ERK|MEK inhibitors|Trametinib, Cobimetinib|Melanoma, NSCLC|
|mTOR|Rapalogs|Rapamycin, Everolimus|RCC, TSC, transplant rejection|
|mTOR|mTOR kinase inhibitors|Torin-1, Vistusertib|Investigational|
|JAK/STAT|JAK inhibitors|Ruxolitinib, Tofacitinib|MPN, RA, IBD, alopecia|
|NF-κB|Proteasome inhibitors|Bortezomib, Carfilzomib|Multiple myeloma|
|p53|MDM2 inhibitors|Navtemadlin (AMG-232)|AML, liposarcoma (p53 WT)|
|TLR|TLR agonists (immune)|MPL (TLR4), Imiquimod (TLR7)|Vaccine adjuvants, BCC|

---

_Document compiled from primary literature and established molecular biology sources. Pathway biology is an active research area; mechanisms continue to be refined._