import sys
import os
import dill
from src.exception import CustomException

def save_obj(file_path: str, obj: object) -> None:
    """
    Saves a Python object to a file using dill serialization.

    Parameters:
    - file_path (str): The full path where the object should be saved.
    - obj (object): The Python object to save.

    Raises:
    - CustomException: If saving fails for any reason.
    """
    try:
        # Create directory if it doesn't exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Serialize the object using dill
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)
