import PySimpleGUI as sg


class fe:
    window = sg.Window("Placeholder")

    def renderGUI(self, rows):
        headings = ['Roommate', 'Job']
        header = [[sg.Text(h, size=(16, 1))
                   for h in headings]]
        layout = header + rows
        self.window = sg.Window("Today's Tasks", layout, font='Courier 12')
        self.window.read(1)

    def close(self):
        self.window.close()
