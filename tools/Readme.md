
<img src="https://github.com/Ravenneo/proteins_tools/assets/41577767/b50ee419-ff74-4d4b-a175-f18c03a6aff1" alt="alt text" width="560" height="560">

## Acro_extractor: script designed to extract acronyms and their full forms from a Microsoft Word (.docx) document.

    1) The script starts by importing necessary Python libraries. This includes docx for reading the Word document, pandas for creating a DataFrame (a table-like data structure), and re for regular expressions, which are used to identify patterns in text.

    2) It prompts the user to input the name of the Word document from which they want to extract acronyms.

    3) It reads the Word document using the Document function from the docx library.

    4) The script then goes through each paragraph in the document. It uses a regular expression to identify potential acronyms (two or more consecutive capital letters) and their full forms (either preceding or following the acronym, enclosed in parentheses).

    5) It adds all identified acronyms and their full forms to a list.

    6) Once it has gone through the entire document, it filters out any duplicates from the list.

    7) It then converts this list into a DataFrame using the pandas library.

    8) Lastly, it saves this DataFrame as a .csv file, which can be easily opened and viewed in a spreadsheet program like Excel.

## fasta_to_a3:
This script is designed to convert a protein sequence alignment file in FASTA format to A3M format

