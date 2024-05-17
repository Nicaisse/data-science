# 1-Kreye yon klas ki ap pran yon paramèt chemen yon fichye. Epi ki ap gen metòd pou w li, ajoute, efase kontni yo. Epi yon metod pou w efase fichye a si w gen pèmisyon.

import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "Fichye a pa egziste."
        except PermissionError:
            return "Ou pa gen pèmisyon pou li fichye sa a."
        except Exception as e:
            return f"Yon erè te fèt: {str(e)}"

    def write_file(self, content):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write(content)
                return "Kontni an te ekri avèk siksè."
        except PermissionError:
            return "Ou pa gen pèmisyon pou ekri nan fichye sa a."
        except Exception as e:
            return f"Yon erè te fèt: {str(e)}"

    def append_file(self, content):
        try:
            with open(self.file_path, 'a', encoding='utf-8') as file:
                file.write(content)
                return "Kontni an te ajoute avèk siksè."
        except PermissionError:
            return "Ou pa gen pèmisyon pou ajoute nan fichye sa a."
        except Exception as e:
            return f"Yon erè te fèt: {str(e)}"

    def delete_file(self):
        try:
            os.remove(self.file_path)
            return "Fichye a te efase avèk siksè."
        except FileNotFoundError:
            return "Fichye a pa egziste."
        except PermissionError:
            return "Ou pa gen pèmisyon pou efase fichye sa a."
        except Exception as e:
            return f"Yon erè te fèt: {str(e)}"


# file_manager = FileManager('test.txt')

# print(file_manager.read_file())

# print(file_manager.write_file('Bonjou, mond!'))

# print(file_manager.append_file('\nAjoute nouvo kontni.'))

# print(file_manager.delete_file())


# 2-Kreye yon klas Vivan, ki gen pwopriyete moun (pye, men, non, laj).

class Vivan:
    def __init__(self,pye,men,non,laj) :
        self.pye = pye
        self.men = men
        self.non = non
        self.laj = laj