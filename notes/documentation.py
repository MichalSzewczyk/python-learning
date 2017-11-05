# Methods documentation

# Methods documentation consists of two parts:
# Summary - first line in multi line comment inside method
# Description - all lines inside comment in method

def method():
    """
    Summary of method: here is single line summary
    Description of method: here is multi line description
    of what method is doing etc
    """


# Documentation is later accessible through __doc__ class variable
print(method.__doc__)
