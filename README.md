# RSEM_FPKM_extract
to extract FPKM reads with RSEM package


rsem is a package for RNA-seq reading count. however, rsem package only provide the function to extract the reads but not FPKM. Here I developed a extended python function to extract the FPKM reads.


**this extended function only designed for "genes.results" fiiles, it will not work for "isoforms.results" files.**

_instruciton:_
1. put all rsem read count files (name ending with "genes.results") into one folder 
**=====the file must be ending with "genes.results", othervise, it will not work=====**

2. implement the function by "python rsem-count-and-FPKM-extract-genes.py" or "python rsem-FPKM-extract-genes.py"
3. the output will be tap seperated files. it can be open by Rstuido with "read.table (sep = '\t')" function
