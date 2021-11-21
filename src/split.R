library(tidyverse)

## Split index into stratified random train and test subsets, where
## the size of the test subset is approximately one tenth of the whole
## data set.

index <- read_csv("../data/raw/index.csv")

set.seed(1)

test <- index %>% group_by(label3) %>%
    slice_sample(prop=0.1) %>%
    ungroup

train <- setdiff(index, test)

## Validate

count(index, label3)

count(test, label3)

count(train, label3)

length(test$label3) / length(index$label3) # Approx 0.1

stopifnot(length(index$label3) == length(train$label3) + length(test$label3))

stopifnot(length(unique(index$label3)) == length(unique(test$label3)))

stopifnot(length(unique(test$label3)) == length(unique(train$label3)))

## Output

write_csv(test,"../data/processed/test.csv")
write_csv(train,"../data/processed/train.csv")
