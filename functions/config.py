from datetime import datetime

class files():

    def get_filename(self, file_name, file_struc):
            now = datetime.now()
            dato = now.strftime("%m-%d-%Y")
            file = file_name
            return f"{file}_{dato}.{file_struc}"