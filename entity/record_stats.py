class RecordStats:
    def __init__(self, text, *args):
        self.star = None
        self.symbol = None
        self.last_price = None
        self.change_day = None
        self.high_day = None
        self.low_day = None
        self.volume_day = None
        self._get_record_by_text(text, *args)
        self._remove_commas_from_value()

    def _get_record_by_text(self, text, *args):
        for arg in args[0]:
            if text in arg:
                [self.__setattr__(obj, value) for obj, value in zip(self.__dict__, arg)]
                break

    def _remove_commas_from_value(self):
        [self.__setattr__(key, value.replace(',', '')) for key, value in self.__dict__.items() if ',' in value]
