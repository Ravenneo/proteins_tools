# proteins_tools

Place files in same folder than HTML protein Database.
change "chandra" with the name of your Database.

·Main_Proteins.py: This script imports the ProteinHtml class from a module named ProteinHtml, then it defines the main function. In the main function, an instance of the ProteinHtml class is created and passed the argument "chandra.html" as the input file name.

The function getFileName is called on the instance and the returned value is printed. Then the function searchProtein is called and passed the argument "Acidobacterium ailaaui" as the protein name to search for, the count of how many times it occurs in the file is printed.

The function findAllProteinNames is then called and the returned value, a dictionary of all protein names found in the file and the count of how many times each occurs, is printed.

·ProteinHtml: The first script is a Python class called "ProteinHtml" that can be used to parse an HTML file containing information about proteins. The class has two methods:

    searchProtein(proteinName): searches for a given protein name in the HTML file and returns the number of occurrences of that protein in the file.
    findAllProteinNames(): returns a dictionary containing all the protein names in the HTML file and their count.

·Protein_Sorter.py: This script uses the Python programming language and the Pandas library to extract information from an HTML file named "chandra.html". The "ProteinHtml" class from the "ProteinHtml" module is imported and used to create an object called "protein". The "findAllProteinNames" method is called on this object, which returns a dictionary of protein names and their locations within the HTML file. The script then creates two lists, "names" and "places", to store the extracted protein names and their locations, respectively. The information is then used to create a dictionary called "data", which is then used to create a Pandas DataFrame called "dataframe". The "dataframe" is then saved as a CSV file named "all_proteins.csv". Finally, the "dataframe" is printed.

·Incomplete_protein_counter.py: This script makes an agrupation of families in Chandra's List.

For *Cala.py*:
Python script that allows the user to either display the protein information on the console or export it to a CSV file. The user is prompted to select one of the two options. If the first option is selected, the script creates an instance of the ProteinHtml class, reads the name of the file using getFileName() method, and then searches for a specific protein name using searchProtein() method. Finally, it prints all the protein names and their count using findAllProteinNames() method. If the second option is selected, the script creates a DataFrame from the dictionary returned by findAllProteinNames(), prompts the user for a file name, and exports the DataFrame to a CSV file with the specified name.




