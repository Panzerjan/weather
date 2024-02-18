import shutil
import os
from common import Dato

class files():

    def set_filename(self, file_name=str , file_struc=str):
        '''
         Input:
            file_name: str --> name of the file
            file_struc: str --> extension file etc ,json, xml, csv
        '''
        file = file_name
        return f"{file}.{file_struc}"


    def move_file(new_path, his_path, file):
        """
        Move a file from one directory to another.

        Args:
            new_path (str): The path of the directory from which the file will be moved.
            his_path (str): The path of the directory to which the file will be moved.
            file (str): The name of the file to be moved.

        Returns:
            None
        """
        shutil.move(f"{new_path}{file}", his_path)
        print(f'Moved {file} from {new_path} to {his_path}')

    def remove_old_files(folder_path, num):
        """
        Remove files from a folder that are older than the specified date.

        Args:
            folder_path (str): The path of the folder from which files will be removed.
            cutoff_date (datetime.datetime): The cutoff date. Files older than this date will be removed.

        Returns:
            None
        """
        date = Dato()
        cutoff_date = date.calculate_date(num).timestamp()
        print(cutoff_date)

        # Ensure the folder path exists
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print(f"Folder '{folder_path}' does not exist or is not a directory.")
            return

        # Iterate over files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # Check if it's a file and if it's older than the cutoff date
            if os.path.isfile(file_path):
                file_modified_time = os.path.getmtime(file_path)
                if file_modified_time < cutoff_date:
                    os.remove(file_path)
                    print(f"Removed file '{filename}' from folder '{folder_path}' (last modified: {file_modified_time})")


