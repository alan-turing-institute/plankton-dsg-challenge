#!/usr/bin/env Rscript

## Merge the index and ecotaxa data to get labelled features.

library(tidyverse)

df1 <- read_csv("../clean-index/index-clean.csv")
count(df1)

df2 <- read_tsv("../morphocut/ecotaxa_export.tsv")
count(df2)

df2$filename <- str_replace(df2$img_file_name,"hc-1.tif", "hc.tif")

df2$filename <- str_replace(df2$filename,"0-Pia1", "Pia1")

df <- inner_join(df1, df2, by="filename")
count(df)

write_csv(df, "labelled-features.csv")
