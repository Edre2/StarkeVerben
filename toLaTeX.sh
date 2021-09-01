#!/bin/bash

cp template.tex Verbs.tex

verbs=`cat verbs.csv | \
       sed -e 's/B/ß/' | \
       sed -e 's/,/ \& /' | \
       sed -e 's/,/ \& /' | \
       sed -e 's/,/ \& /' | \
       sed -e 's/,/ \& /' | \
       sed -e 's/,/ \& /' | \
       sed -e 's/"//' | \
       sed -e 's/"//'`

function table {
   echo "\\section{$2}" >> Verbs.tex
   echo "" >> Verbs.tex
   echo "" >> Verbs.tex
   echo "\begin{center}" >> Verbs.tex
   echo "\\begin{longtable}{|c|c|c|c|c|c|}" >> Verbs.tex
   echo "   \hline" >> Verbs.tex
   echo "$1" | \
      sed -e 's/^/\t/' | \
      sed -e 's/$/\\\\\n\t\\hline/' >> Verbs.tex
   echo  "\\end{longtable}" >> Verbs.tex
   echo "\end{center}" >> Verbs.tex
   echo "" >> Verbs.tex
}

table "$verbs" "Starke Verben"

echo "\end{document}" >> Verbs.tex

pdflatex Verbs.tex
rm Verbs.aux Verbs.log
