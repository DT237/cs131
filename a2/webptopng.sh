#!/bin/bash

echo "Please enter the path of the folder containing the .WEBP files: "
read input_path

if [ ! -d "$input_path" ]; then
 echo "Path does not exist."
 exit 1
fi

output_path="$input_path/png_files"
mkdir -p "$output_path"

for file in "$input_path"/*.webp; do
 if [ -f "$file" ]; then
  filename=$(basename "$file")
  ffmpeg -i "$file" "$output_path/$filename.png"
 fi
done

echo ".WEBP to .PNG conversion complete. .PNG files are stored in $output_path."

