class Celle:
    # konstruktør
    def __init__(self):
        self._status = False

    # endre status
    def settDoed(self):
        self._status = False

    def settLevende(self):
        self._status = True

    def erLevende(self):
        return self._status

    def hentStatusTegn(self):# skrive et tegn som presentere døde og levende.
        if self._status == 1:
            return "O"
        else:
            return "."
