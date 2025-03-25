def handle_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")

        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

            # Modify the content (e.g., convert to uppercase)
            modified_content = content.upper()

            # Determine the output filename
            output_filename = f"{filename.split('.')[0]}_modified.{filename.split('.')[-1]}"

            # Write the modified content to a new file
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)

            print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: An error occurred while trying to read or write the file '{filename}'.")

# Call the function
handle_file()
