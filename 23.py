class Configuracion:
    _inst = None

    def __new__(cls):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst

    def __init__(self):
        if not hasattr(self, '_init'):
            self._init = True
            self.data = {'modo': False}
