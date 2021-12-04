def oops() -> None:
    raise IndexError
def oops2() -> None:
    try:
        oops()
    except Exception:
        print('Помилка спробуйте ще раз :)')
oops2()
