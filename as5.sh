#!/bin/bash
# In-place convert absolute or invalid relative file path
# Delete os.chdir lines


target="../Words-2"
wordfile="$(readlink -f twl06.txt)"
sedscript="s/open *(.*)/open('$(echo "$wordfile" | sed 's/\//\\\//g')')/g"

find "$target" -mindepth 3 -name "*.py" | xargs -I {} sed -i "$sedscript" {}
find "$target" -mindepth 3 -name "*.py" | xargs -I {} sed -i '/os\.chdir/d' {}

