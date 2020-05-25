#prvi način
class Napaderror (Exception):
    def __init__(self):
        self.error_message='NAPAD ERROR: Unešena pogrešna vrijednost'
        print("\n Opis greške: {}".format(self.error_message))

# Drugi način
class Napaderror(Exception):
    def __init__(self, nsg='',code=000):
        self.error_message = ''
        self.error_dict = {
            000: 'NAPAD ERROR: Unešena pogrešna vrijednost'
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n Opis greške: {}".format(self.error_message))