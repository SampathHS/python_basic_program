def main():
    # Open file for output
    outfile = open("Players.txt", "w")

    # Write data to the file
    outfile.write("Sachin\n")
    outfile.write("Rahul\n")
    outfile.write("Kumble\n")

    print("File name is: ",outfile.name)
    print("File accessing mode is:  ", outfile.mode)

    outfile.close() # Close the output file

    # Open file for output
    outfile = open("new_Players.txt", "w")

    # Write data to the file
    outfile.writelines("Sachin\nRahul\nBharathi\nMadhumitha...\n")
    
    outfile.close() # Close the output file

main() # Call the main function
