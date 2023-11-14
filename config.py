import configparser

class API_Config:
    def __init__(self):
        self.conf = configparser.ConfigParser()

        try:
            with open("settings.ini") as f:
                self.conf.read_file(f)
        except IOError:
            print("settings.ini file is not found")
            exit()

        self.conf.sections()



