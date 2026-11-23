# Membrane permeability in Mycobacterium tuberculosis

Estimates the probability that a small molecule crosses the Mycobacterium tuberculosis cell envelope, a waxy barrier that blunts otherwise potent inhibitors. This Ersilia replication of MycPermCheck (Merget and colleagues) is a LazyQSAR classifier trained on 3,910 compounds that inhibit mycobacterial growth against 39,100 decoys from the NIH MLSMR library, with AUROC 0.95 in five-fold out-of-fold validation. Decoys are easier to separate than measured non-permeable compounds, so real performance is lower. Permeability alone does not imply antitubercular activity.

This model was incorporated on 2021-10-14.
Last packaged on 2026-10-28.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8d8a`
- **Slug:** `mycpermcheck`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`
- **Tags:** `Permeability`, `ADME`, `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Rank of predicted permeability into Mycobacterium tuberculosis against 50,000 drug-like molecules; 0.65 is more likely permeable than 99% of them.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| mycpermcheck_rank | float | high | Rank score of the compound's predicted permeability into Mycobacterium tuberculosis, calibrated against a reference library of 50K drug-like molecules so that 0.65 is more likely permeable than 99% of them. Recommended threshold: 0.65. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Replicated`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8d8a](https://hub.docker.com/r/ersiliaos/eos8d8a)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8d8a.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8d8a.zip)
- **Apptainer**: [https://models-sif.s3.eu-north-1.amazonaws.com/eos8d8a_v2.sif](https://models-sif.s3.eu-north-1.amazonaws.com/eos8d8a_v2.sif)

### Resource Consumption
- **Model Size (Mb):** `42`
- **Environment Size (Mb):** `1857`
- **Image Size (Mb):** `1993.07`

**Computational Performance (seconds):**
- 10 inputs: `35.67`
- 100 inputs: `31.6`
- 10000 inputs: `675.45`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://doi.org/10.1093/bioinformatics/bts641](https://doi.org/10.1093/bioinformatics/bts641)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2013`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8d8a
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8d8a
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
