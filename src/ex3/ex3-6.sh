#!/bin/bash

if [ ! -d "$1" ]
then
   mkdir $1
   cd $1
   i=0
   
   while [ $i -lt 5 ]
   do
       touch "file$i.txt"
       i=$((i + 1))
   done

   tar cvf $1.tar file0.txt file1.txt file2.txt file3.txt file4.txt

   mkdir $1
   
   mv $1.tar $1
   cd $1
   tar xvf "$1.tar"
fi 

exit 0
