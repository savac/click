# shows click/nonclick probabilities for each hour
rm(list = ls(all = TRUE))
setwd('~/Dropbox/Kaggle')
s1=read.csv("data/train_random1on100.csv",nrow=1000000,stringsAsFactors=F)
prop.table(table(s1$hour,s1$click),1)
