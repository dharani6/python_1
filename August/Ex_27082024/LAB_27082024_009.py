def add_before_ui_after_ui(func):
    # two parts
# wrapper & call
    def wrapper():
        print("before the running UI TC")
        print("start thhe browse ")
        func()
        print("Ending the running UI Tc")
        print("quit the browser")
    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")

#test_ui()