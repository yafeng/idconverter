# idconverter
A tool to convert Ensembl (ENSP) or Uniprot protein ID to gene symbol

Usage :  python idconverter.py --input file_name --ouput file_name --n 1

--n specify which column the protein ID is. (count starts from 1)

Note: The first line in the input file is regarded as header line.

If the protein ID column contains multiple accessions (separated by ;), eg.

Q15149-3;Q15149-4;Q15149-8

The program will insert a gene symbol for each of the protein ID separated by ;

Q15149-3;Q15149-4;Q15149-8       PLEC;PLEC;PLEC

Speed

The program convert 25000 protein IDs within 0.03 second.
