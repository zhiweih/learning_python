class AttrDisplay:
    def _gather_attrs(self):
        return ', '.join(('%s=%s' % (key, getattr(self, key)) for key in sorted(self.__dict__)))

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self._gather_attrs())
