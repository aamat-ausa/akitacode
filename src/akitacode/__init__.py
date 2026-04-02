from importlib import import_module

__version__ = "2.0.11"

__all__ = [
    'bd',
    'canbus',
    'conditionals',
    'data',
    'document',
    'frame',
    'information',
    'instances',
    'keys',
    'line_state_machine',
    'line',
    'mask',
    'messages',
    'numerics',
    'protocol',
    'situation'
]


def __getattr__(name: str):
    if name in __all__:
        module = import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
