class Calc():
    def __init__(self) -> None:
        self.inputCurrent: str = ''
        self.ans: int
        self.inputHistory: str = ['']

    def get_operation(self, num) -> None:
        if(type(num)== str):
            self.inputCurrent = self.inputCurrent + num 
            print(self.inputCurrent)

    def edit_operation(self, val):
        if (val == '='):
            try:
                self.ans = round(eval(self.inputCurrent), 4)
                self.inputHistory.append(self.inputCurrent)
                self.inputCurrent = str(self.ans)
            except ZeroDivisionError:
                self.inputCurrent = "'Math Error'"
            except Exception:
                print(Exception)
        elif (val == 'del'):
            self.inputCurrent = self.inputCurrent[:-1]
        elif (val == 'clear'):
            self.inputCurrent = ''
        
    def get_last_of_list(self) -> str:
        return self.inputHistory[-1]
    