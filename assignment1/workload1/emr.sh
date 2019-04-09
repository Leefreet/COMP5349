#!/bin/bash

spark-submit \
    --master local[4] \
    main.py \
    --input /home/hadoop/COMP5349/assignment1/ \
    --output /home/hadoop/COMP5349/out/
	 

    
