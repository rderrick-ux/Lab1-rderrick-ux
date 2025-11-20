#!/usr/bin/env bash
set -euo pipefail

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

if [[ ! -d "$ARCHIVE_DIR" ]]; then
  mkdir -p "$ARCHIVE_DIR"
fi

shopt -s nullglob
csv_files=(*.csv)

if [[ ${#csv_files[@]} -eq 0 ]]; then
  echo "No CSV files found."
  exit 0
fi

for file in "${csv_files[@]}"; do
  timestamp="$(date +%Y%m%d-%H%M%S)"
  base="${file%.csv}"
  new_name="${base}-${timestamp}.csv"
  dest="${ARCHIVE_DIR}/${new_name}"

  {
    echo "==== Archive Entry ===="
    echo "Timestamp: ${timestamp}"
    echo "Original File: ${file}"
    echo "Archived As: ${dest}"
    echo "--- File Content Start ---"
    cat "${file}"
    echo "--- File Content End ---"
    echo
  } >> "${LOG_FILE}"

  mv -- "${file}" "${dest}"
  echo "Archived ${file} -> ${dest}"
done

