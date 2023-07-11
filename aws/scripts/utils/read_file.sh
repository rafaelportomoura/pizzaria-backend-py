file=$1

if command -v bat &>/dev/null; then
  bat --paging=never --plain $file
else
  cat $file
fi
