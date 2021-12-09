#!/usr/bin/env Rscript

## Explore a problem with some duplicates in the index.

library(tidyverse)

df <- read_csv("../data/raw/index.csv")

dups <- df$filename[duplicated(df$filename)]

df2 <- filter(df, df$filename %in% dups)

df2 <- arrange(df2, filename)

df2 <- select(df2,-index)
write_csv(df2, "dups.csv")
