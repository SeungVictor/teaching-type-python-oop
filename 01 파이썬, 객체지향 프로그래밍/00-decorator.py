# decorator


def copyright(func):
    def new_func():
        print("@ amamovsdfjkldjsakfljdskaljfkdsla")
        func()

    return new_func


#바로위에다가 함수를 재정의 decorator를 사용해서
@copyright
def smile():
    print("🙃")


@copyright
def angry():
    print("🤯")


@copyright
def love():
    print("🥰")


smile()
angry()
love()
