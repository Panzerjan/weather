import shutil

class files():

    def set_filename(self, file_name , file_struc):
        '''
         Input:
            file_name: str --> name of the file
            file_struc: str --> extension file etc ,json, xml, csv
        '''
        file = file_name
        return f"{file}.{file_struc}"

    def move_file(new_path, his_path , file):
            shutil.move(f"{new_path}{file}", his_path)
            print(f'Moved {file} from {new_path} to {his_path}')