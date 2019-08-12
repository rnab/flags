library("magick")
library("tidyverse")

a<-image_read("data/ad.png")
print(a)
image_info(a)
?image_resize
p<-image_resize(a, geometry_size_pixels(width = 5, height = 5))
print(p)
head(p)
