# Membrane permeability in Mycobacterium tuberculosis

MycPermCheck predicts potential to permeate the Mycobacterium tuberculosis cell membrane based on physicochemical properties.
Due to the lack of reliable experimental datapoints, the authors defined the training set using molecules that are active against M.tb (MIC < 10 uM) (therefore, permeable) and have a molecular weight of <500 Dalton

## Identifiers

* EOS model ID: `eos8d8a`
* Slug: `mycpermcheck`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of permeability across the M.tb cell wall

## References

* [Publication](https://academic.oup.com/bioinformatics/article/29/1/62/272745)
* [Source Code](https://www.mycpermcheck.aksotriffer.pharmazie.uni-wuerzburg.de/index.html)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos8d8a)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8d8a.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos8d8a) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://academic.oup.com/bioinformatics/article/29/1/62/272745) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!