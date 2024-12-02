# Algorithm Document

#### THINK before you code...
#### Write down the list of tasks to help you think

* Purpose: allows user to select file to turn into a dictionary
* Name: key_selection
* Parameters: none
* Return: filename
* Algorithm:
1. set filename equal to user input
2. while filename is not equal to the morsecode file
   1. output error message
   2. set filename equal to user input
3. while filename is not os pathway
   1. output error message
   2. set filename equal to user input
4. return filename



* Purpose: converts file to dictionary
* Name: file_to_dictionary
* Parameters: filename
* Return: m_d
* Algorithm:
1. set m_d equal to empty dictionary
2. morse_data equals open file for reading
3. for line in morse_data
   1. set item equal to line strip and line split
   2. set key equal to item index 1
   3. set value equal to item index 0
   4. m_d[key] equals value
4. close file
5. return m_d


* Purpose: allows user to select file to be translated
* Name: inputfile
* Parameters: none
* Return: input_file
* Algorithm:
1. set input_file equal to user input
2. while input file is not equal to morse1.txt and morse2.txt and morse3.txt:
   1. output error
   2. set input_file equal to user input
3. return input_file



* Purpose: translated input file and creates output file
* Name: translate_file
* Parameters: input_file, output_file, m_d
* Return: none
* Algorithm:
1. with open input file for reading as infile and open output file for writing as outfile:
    1. for line in infile
       1. letters = line strip and line split
       2. translation = empty string joined to m_d.get letter for letter in letters
       3. write translation plus new line



* Purpose: runs main program
* Name: main
* Parameters:  none
* Return: none
* Algorithm: 
1. print character times 70
2. output purpose
3. print character times 70
4. filename equals key_selection function
5. m_d equals file_to_dictionary function with parameters filename
6. input_file equals inputfile function
7. call translate file using input file, translation.txt, and m_d as parameters
8. output to user that their file has been translated into a new file and output thank you message