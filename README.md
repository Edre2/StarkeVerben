# StarkeVerben
Little project to learn the irregular verbs in German in the terminal. The 'ß' are replaced by 'B' to make typing the verbs with this character easy.
This project also includes a script to turn the verbs into a LaTeX document and convert it to pdf (the package `texlive` is needed to compile the document)
# Installation
```
git clone https://github.com/Edre2/StarkeVerben
cd StarkeVerben

# To learn the verbs
pyhton3 main.py

# To make a pdf (not nececary if verbs.csv hasn't been changed)
./toLaTeX.sh
# Opening the pdf
your_pdf_viewer Verbs.pdf
```
# Changing the verbs
To change the verbs, edit `verbs.csv` and in `main.py`, make sure to change the variables `NUMBER_OF_FORMS_DE` and `NUMBER_OF_FORMS_FR` so that it gets the correct elements as the German and French forms of the verbs
