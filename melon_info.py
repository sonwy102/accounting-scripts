"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons_dict):
    """Print each melon with corresponding attribute information."""

    # Iterate over the melons dictionary
    for name, attributes in melons_dict.items():

        # Print melon's name
        print(name.upper())

        # Iterate over the key(dict) of each item in melons_dict
        for attribute, meloninfo in attributes.items():
            
            # Print each attribute of a melon
            print(f"    {attribute} : {meloninfo}")

        # A line break for formatting
        print("---------------------------------------------------------")