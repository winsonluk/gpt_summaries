#!/bin/sh

while true; do
  nohup python ~/gpt_summaries/generate_summaries.py $(($(wc -l ~/gpt_summaries/io/summaries.txt | cut -f1 -d' ') + 1))
done &
