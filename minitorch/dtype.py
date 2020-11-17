

class dtype(object):
    def __init__(self):
        super().__init__()

    def is_floating_point(self) -> bool:
        raise NotImplementedError('is_floating_point NotImplementedError')

    def is_complex(self) -> bool:
        raise NotImplementedError('is_complex NotImplementedError')

    def is_signed(self) -> bool:
        raise NotImplementedError('is_signed NotImplementedError')

class dtype_float32(dtype):
    def __init__(self):
        super().__init__()

    def is_floating_point(self) -> bool:
        return True

    def is_complex(self) -> bool:
        return False

    def is_signed(self) -> bool:
        return True

float32 = dtype_float32()
float = float32


