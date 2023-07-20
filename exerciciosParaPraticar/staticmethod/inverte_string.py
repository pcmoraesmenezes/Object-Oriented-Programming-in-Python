class StringUtil:

    @staticmethod
    def inverter_string(string):
        inverter_string = ''
        for i in string:
            inverter_string =  i+ inverter_string
        return inverter_string

string = StringUtil.inverter_string('abacate')
print(string)
