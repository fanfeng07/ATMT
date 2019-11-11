#!/bin/sh

# merges subword units that were split by BPE

sed -i 's/\@\@ //g' model_translations_bpe.txt