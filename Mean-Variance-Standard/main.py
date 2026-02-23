import numpy as np
import re

def calculate_var(my_list, var):
    if var == "mean":
        axis1 = np.mean(my_list, axis=0).tolist()
        axis2 = np.mean(my_list, axis=1).tolist()
        flattened = np.mean(my_list).tolist()
        return [axis1, axis2, flattened]
    
    elif var == "variance":
        return [np.var(my_list, axis=0).tolist(), np.var(my_list, axis=1).tolist(), np.var(my_list).tolist()]
    
    elif var == "standard":
        return [np.std(my_list, axis=0).tolist(), np.std(my_list, axis=1).tolist(), np.std(my_list).tolist()]
    
    elif var == "max":
        return [np.max(my_list, axis=0).tolist(), np.max(my_list, axis=1).tolist(), np.max(my_list).tolist()]
    
    elif var == "min":
        return [np.min(my_list, axis=0).tolist(), np.min(my_list, axis=1).tolist(), np.min(my_list).tolist()]
    
    elif var == "sum":
        return [np.sum(my_list, axis=0).tolist(), np.sum(my_list, axis=1).tolist(), np.sum(my_list).tolist()]

def calculate(list_of_nine_numbers):
    """
    Docstring for calculate
    
     Calculates mean, variance, standard deviation, max, min, and sum for a 3x3 matrix.
    
    Args:
        list_of_nine_numbers (list): A list of exactly 9 numbers (ints or floats).
    
    Returns:
        dict: A dictionary with keys 'mean', 'variance', 'standard deviation', 'max', 'min', 'sum'.
              Each value is a list of [axis1 (columns), axis2 (rows), flattened].
    """

    convert_to_an_array = np.array(list_of_nine_numbers).reshape(3, 3)

    return {
        "mean": calculate_var(convert_to_an_array, "mean"),
        "variance": calculate_var(convert_to_an_array, "variance"),
        'standard deviation': calculate_var(convert_to_an_array, "standard"),
        'max': calculate_var(convert_to_an_array, "max"),
        'min': calculate_var(convert_to_an_array, "min"),
        'sum' : calculate_var(convert_to_an_array, "sum")
    }


# choose 9 numbers and convert to integer type.
while True:
    nine_numbers = (input("Enter nine numbers in your choice without space or anythink:\n"))
    # if len(nine_numbers) == 9:
    if re.search(r"\d{9}", nine_numbers):
        try :
            print(calculate(list(map(lambda x: int(x), list(nine_numbers)))))
            break
        except Exception as error:
            print(error)
    else:
        continue