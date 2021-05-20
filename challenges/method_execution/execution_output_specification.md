# Execution pipelines output specification

## Synopsis

This specification describes required output of tool execution pipelines to ensure that the benchmarking pipelines have access to input files in the same format for each tool.

Outputs depend on features available for the tool (i.e. not all tools perform *de novo* identification of PAS) and can be grouped into three categories:

- identification challenge:
  - BED file with poly(A) sites with single nucleotide resolution
- quantification challenge:
  - BED file with TPM values for each site
- differential usage challenge:
  - TSV file with gene ID and significance of differential PAS usage.

## General info

* **Challenge:** Method execution
* **Identifier:** E1

## Inputs

Inputs to the execution pipeline depend on the method/tool.

## Outputs


| # | Format | Link | Example data |
  | --- | --- | --- | --- |
  | 1 | BED | [Specification][spec-bed] | [Link][out1] |
  | 2 | BED | [Specification][spec-bed] | [Link][out2] |
  | 3 | TSV | [Wikipedia][wiki-tsv] | [Link][out3] |
  
### Additional info inputs
  
#### Format 1

This BED file contains single-nucleotide position of poly(A) sites identified by the tool.

#### Format 2

This BED file contains positions of unique poly(A) sites as well as an additional column with TPM values for each identified site.

#### Format 3

This TSV file contains two columns:

1. gene ID
2. significance of differential PAS usage

Column names **should not be added to the file**.


[//]: # (References)
  
[out1]: ./example_files/output1.bed
[out2]: ./example_files/output2.bed
[out3]: ./example_files/output3.tsv
[spec-bed]: <https://genome.ucsc.edu/FAQ/FAQformat.html#format1>
[wiki-tsv]: <https://en.wikipedia.org/wiki/Tab-separated_values>

