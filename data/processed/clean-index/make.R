#!/usr/bin/env Rscript

## We found a problem with duplicates in the index.csv file. This
## script removes the duplicates. It also removes augmented images.
## It writes a new file called clean-index.csv.

library(tidyverse)

df <- read_csv("../../raw/index.csv")
count(df)

## Find duplicates

dups <- df$filename[duplicated(df$filename)]
df2 <- filter(df, df$filename %in% dups)
count(df2)

## Clean up and export a list of duplicates

df3 <- arrange(df2, filename)

df3 <- select(df3,-index)
write_csv(df3, "dups.csv")

## Remove the duplicates

df4 <- filter(df, !df$filename %in% dups)
count(df4)

## Check lengths

count(df) - count(df2) == count(df4)

## Remove augmented images (these have suffixes such as _fx.tif,
## _fy.tif and _fxy.tif

df5 <-filter(df4, endsWith(df4$filename, "hc.tif"))

count(df5)

write_csv(df5, "index-clean.csv")
