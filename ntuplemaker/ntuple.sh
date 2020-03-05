FILELIST=$1
MAXFILES=$2
JOBNUMBER=$3
#FILENAMES=$(cat $FILELIST | xargs -n$MAXFILES | sed -n "$(($JOBNUMBER+1)) p" | sed 's;^;root://cms-xrdr.sdfarm.kr:1094//xrd;g')
FILENAMES=$(cat $FILELIST | xargs -n$MAXFILES | sed -n "$(($JOBNUMBER+1)) p" | sed 's;^;/xrootd;g')
#FILENAMES=$(cat $FILELIST | xargs -n$MAXFILES | sed -n "$(($JOBNUMBER+1)) p" | sed)
#| sed 's;^/xrootd/;root://cms-xrdr.private.lo:2094//xrd/;g')
echo $FILENAMES
python ntuplemaker.py $FILENAMES
