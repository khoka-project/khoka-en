#!/bin/bash
for f in *
  do  
    xlsx2csv $f  >> $f.csv
done
