class SettingsAgent(object):
    _instance = None
    is_mouse_macros_activated = False
    is_button_held = False

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

        return cls._instance