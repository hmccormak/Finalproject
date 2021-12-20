## Team Members: Joseph Hartner, Henry McCormak, Mary Waller

# File Purposes:
CIRA.py = Codémon Project Code\
codélist.csv = a csv file containing the list and stats of Codés\
itemlist.csv = a csv file containing the list of items and item effects\
PDF Document 326 Final.pdf = Final check-in pdf of project process

# How to use CIRA.py:
Mac terminal: python3 CIRA.py\
PC terminal: python CIRA.py

# Attribution:
This project was very collaborative. Functions, Classes, and Methods were mostly developed by the team somewhat evenly, however below are our specific focuses.

### Henry McCormack mainly authored:
main()\
battle() (full of block that really should be their own functions)\
check_select()\
ItemCatalog() (including methods)

### Joseph Hartner mainly authored:
Codédex() and Codé() class\
battle() (assist with item/Codémon/change section)\
battle() (assist with while loop)

### Mary Waller mainly authored:
pandas_table()\
opponent_select()\
attack()\
get_item() from Item() class

 # Works Cited:
    Pallavi. "How to read csv file with Pandas without header?" Geeks for Geeks, 3 Mar. 2021, www.geeksforgeeks.org/  how-to-read-csv-file-with-pandas-without-header/. Accessed 17 Dec. 2021.
    Used in line 411 to read csv files in pandas\
    Verma, Ankur. "Add column names to dataframe in Pandas." Geeks for Geeks, 1 Aug. 2020, www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/. Accessed 17 Dec. 2021.
    Used example 2 in line 411 to name column headers in csv dataframe\
    Zibrita, Pavol. "How to print pandas DataFrame without index." Stack Overflow, 18 Sept. 2015, stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index. Accessed 17 Dec. 2021.
    Used df.to_string(Index = False) in lines 424, 431, 438, 444

