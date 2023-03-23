#!/bin/zsh

percent="0.15"

cd Dataset

for D in "./TrainImages"/*; do
    if [ -d "${D}" ]; then
        count=`ls ${D}| wc -l`
		echo ${D} $count
		integer ceiling_result=`echo "$count * $percent" | bc`
		echo ${D} $ceiling_result
		
		#pwd
		
		cd ${D}
		
		mkdir -p "../../TestImages/${D}" && cp `ls | head -$ceiling_result` "../../TestImages/${D}"
		
		cd ../..
    fi
done
