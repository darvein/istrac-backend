#!/bin/bash

photo_pk=1
lenarr=0
tplace_pk=1
output_file="tplaces.yaml"

> $output_file

generate_photos() {
    local photo_dir=$1
    local -n current_pk=$2
    local photo_ids=()

    for photo in "$photo_dir"/*.jpg; do
        echo "- model: api.photo" >> $output_file
        echo "  pk: $current_pk" >> $output_file
        echo "  fields:" >> $output_file
        echo "    created_by: 1" >> $output_file
        echo "    image: ${photo#*/}" >> $output_file
        photo_ids+=($current_pk)
        ((current_pk++)) 
    done

    echo "${photo_ids[*]}" 
}

generate_tplaces() {
    local locpk=$1
    local name=$2
    local slug=$3
    local description=$4
    local photo_ids_string=$5 
    local photo_ids=($photo_ids_string) 

    echo "- model: api.tplace" >> $output_file
    echo "  pk: $tplace_pk" >> $output_file
    echo "  fields:" >> $output_file
    echo "    name: $name" >> $output_file
    echo "    description: $description" >> $output_file
    echo "    location: $locpk" >> $output_file
    echo "    created_by: 1" >> $output_file

   IFS=','
   echo "    photos: [${photo_ids[*]}]" >> $output_file
   IFS=' '

    echo "    videos: []" >> $output_file
    echo "    comments: []" >> $output_file
    echo "    categories: []" >> $output_file
    ((tplace_pk++)) 
}

for txt in *.txt; do
    while IFS='|' read -r locpk name slug description; do
        photo_ids=() 
        photo_dir="../../../data/photos/$slug"
        if [ -d "$photo_dir" ]; then
            # Check if the directory is empty
            if [ "$(find "$photo_dir" -maxdepth 1 -type f | wc -l)" -gt 0 ]; then
                photo_ids_string=$(generate_photos "$photo_dir" photo_pk)
                photo_ids=($photo_ids_string) 
                
                lenarr=${#photo_ids[@]}
                ((photo_pk=photo_pk+lenarr))

                generate_tplaces "$locpk" "$name" "$slug" "$description" "${photo_ids[*]}"
            else
                echo "Directory $photo_dir is empty, skipping..."
                continue
            fi
        fi
    done < "$txt"
done
