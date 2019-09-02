import PySimpleGUI as sg


class fe:
    def renderGUI(self, rows):
        headings = ['Roommate', 'Job']
        header = [[sg.Text(h, size=(16, 1))
                   for h in headings]]
        layout = header + rows
        window = sg.Window("Today's Tasks", layout, font='Courier 12')
        window.Read()
