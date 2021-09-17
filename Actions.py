import slider

from test import board


class Actions:
    pass

move = Actions(board.browser)
action = move.dragAndDropBy(slider, 100, 0).build()
action.perform()
