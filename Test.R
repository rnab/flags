library("magick")
library("tidyverse")

a<-image_read("data/ad.png")
print(a)
image_info(a)
?image_resize
p<-image_resize(a, "5x5!")
help("image_resize")
print(p)
head(p)

x<-p[[1]]
x[1:2,5,5]


library("tidyverse")
out<-read_csv("out.csv")

names(out)<-c("cn",paste0("v",1:75))

library("class")
tst=out%>%sample_n(10)

knn(out[,2:76],tst[,2:76],cl=out$cn)