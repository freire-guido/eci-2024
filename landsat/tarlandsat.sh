for i in $1/*.tar; do mkdir $1/${i:0:-4} | mv $i 1/${i:0:-4}; done
for i in *; do tar -xvf $i/$i.tar -C $i; done