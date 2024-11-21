def read_file_to_list(filename):
    data = []
    try:
        # Open the file for reading
        file_data = open(filename, "r")

        # Read all lines from the file into a list
        data = file_data.readlines()

        # Close the file after reading
        file_data.close()

        # Return the list of data
        return data
    except:
        # Ensure the file is closed in case of an error
        file_data.close()

        # Print an error message and return an empty list
        print("Error reading file")
        return data
def main ():
    m_d = {

    }
    filename = input("Enter file name: ")
    for line in filename:
        items = line.split('  ')
        key = items[1]
        val = items[0]
        m_d[key] = val
    print(m_d)

main()


