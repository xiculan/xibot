import curses

def main(stdscr):

    win = curses.newwin(5, 20, 10, 20);
    win.addstr('hello world')
    win.addstr('bon dia')
    win.getch()

    win.mvwin(15, 30)
    stdscr.refresh()

    win.getch()


if __name__ == '__main__':
    curses.wrapper(main)
