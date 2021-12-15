#!/usr/bin/env Rscript

## Copy images to sub-directories in a format expected by
## torchvision.datasets.ImageFolder based on label3
##


library(tidyverse)

df <- read_csv("../test-train/test.csv")

files <- file.path("/scratch/data/images", df$filename)

out <- file.path("test", df$label3, df$filename)

dir.create("test")

for (i in file.path("test", unique(df$label3))) {
    dir.create(i)
}

file.copy(files, out)


df <- read_csv("../test-train/train.csv")

files <- file.path("/scratch/data/images", df$filename)

out <- file.path("train", df$label3, df$filename)

dir.create("train")

for (i in file.path("train", unique(df$label3))) {
    dir.create(i)
}

file.copy(files, out)
