#!/bin/bash
tempfile="/tmp/tmp-jtalk.wav"
voice="nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice"
dic="/var/lib/mecab/dic/open-jtalk/naist-jdic"
option="-m /usr/share/hts-voice/$voice -x $dic -ow $tempfile"

echo "$1" | open_jtalk $option
aplay $tempfile