from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.setBackgroundColor(0, 0, 0)  # black background

app = MyApp()
app.run()