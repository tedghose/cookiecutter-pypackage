"""Main module."""

class Model:
    def __init__(self, args):
        self.args = args

    def ctrlr(self, ctrlr=None):
        if ctrlr is not None:
            self.controler = ctrlr
        return self.controler

class View:
    def __init__(self, ctrlr):
        self.ctrlr = ctrlr


class Controller(TaskController):
    def __init__(self, model):
        self.model = model
        self.model.ctrlr(self)
        self.view = View(self)

    def run(self):
        return 0
