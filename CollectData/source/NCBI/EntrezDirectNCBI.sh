#!/bin/bash
function downloadED() {
  # should I try ggColab so that I dont have to save too much packages unnecessarily
  if 
}

function download () {
    # make directory to save the data
    if ! test -d /content/drive/MyDrive/RetrieveData; then
      mkdir /content/drive/MyDrive/RetrieveData
      mkdir /content/drive/MyDrive/RetrieveData/Data`date +"%m_%d_%Y"`
    else
      if ! test -d /content/drive/MyDrive/RetrieveData/Data`date +"%m_%d_%Y"`; then
      mkdir /content/drive/MyDrive/RetrieveData/Data`date +"%m_%d_%Y"`
      fi
    fi

    # run code to get data
    
    keyword=$1
    SaveOutput=$2
    format=$3

    ${HOME}/edirect/esearch -db nucleotide -query "$keyword" -sort "Date Released" | ${HOME}/edirect/efetch -format $format> $SaveOutput
    done

  #Ex: source ./Haplogroup/finalCodes/bashScriptCodes/downloadDataNCBI.sh; download /content/drive/MyDrive/Haplogroup/finalCodes/others/countries.txt /content/drive/MyDrive/RetrieveData/OldCountryFasta
  #Ex: source CollectData/source/NCBI/EntrezDirectNCBI.sh; downloand "keyword" "SaveOutput" "format"
}
