#!/bin/bash

spark-submit \
    --master local[4] \
    main.py \
    --input /home/hadoop/asm1/ \
    --output /home/hadoop/asm1/rating_out/
	 

    
