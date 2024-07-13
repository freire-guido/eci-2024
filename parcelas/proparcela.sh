cat $1 | sed 's/},{/}\n{/g' >> pro_$1
cat pro_$1 | grep -oP '"localidad":"\K[^"]*' | sort | uniq