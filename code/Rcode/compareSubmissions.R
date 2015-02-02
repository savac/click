# opens two submissions and plot one as a function of the other
rm(list = ls(all = TRUE))
setwd('~/Dropbox/Kaggle')
s1=read.csv("data/sub3.csv",nrow=1000000,stringsAsFactors=F)
s2=read.csv("data/submissiontestshift.csv",nrow=1000000,stringsAsFactors=F)
y1=s1$click
y2=s2$click
plot(y1,y2)
