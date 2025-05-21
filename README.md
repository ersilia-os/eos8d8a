# Membrane permeability in Mycobacterium tuberculosis

MycPermCheck predicts potential to permeate the Mycobacterium tuberculosis cell membrane based on physicochemical properties.
Due to the lack of reliable experimental datapoints, the authors defined the training set using molecules that are active against M.tb (MIC < 10 uM) (therefore, permeable) and have a molecular weight of <500 Dalton

This model was incorporated on 2021-10-14.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8d8a`
- **Slug:** `mycpermcheck`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`
- **Tags:** `Permeability`, `M.tuberculosis`, `ADME`, `Tuberculosis`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of permeability across the M.tb cell wall

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| mycpermcheck_proba | float | high | Probability of permeability in Mtb |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8d8a](https://hub.docker.com/r/ersiliaos/eos8d8a)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8d8a.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8d8a.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `421`


### References
- **Source Code**: [https://www.mycpermcheck.aksotriffer.pharmazie.uni-wuerzburg.de/index.html](https://www.mycpermcheck.aksotriffer.pharmazie.uni-wuerzburg.de/index.html)
- **Publication**: [https://academic.oup.com/bioinformatics/article/29/1/62/272745](https://academic.oup.com/bioinformatics/article/29/1/62/272745)
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
