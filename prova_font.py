import pyfiglet
import curses
import time


def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.refresh()

    curses.resize_term(40, 300)

    font1 = "ansi_regular"
    font2 = "electronic"
    title1 = pyfiglet.figlet_format('GSW 100', font=font2)
    title2 = pyfiglet.figlet_format('LAL 99', font=font2)
    timess = pyfiglet.figlet_format('08:27 4th', font=font1)
    stdscr.addstr(title1)
    stdscr.refresh()
    time.sleep(10)

    # print(f'[blue]{title1}[/blue]')
    # print(f'[white]{time}[/white]')
    # print(f'[yellow]{title2}[/yellow]')


curses.wrapper(main)

# import curses
# import time
# import pyfiglet


# def main(stdscr):
#     # Clear screen
#     stdscr.clear()
#     stdscr.refresh()

#     # Resize the terminal window
#     curses.resizeterm(40, 500)  # Resize to 40 rows, 500 columns

#     # Generate ASCII art
#     ascii_text = pyfiglet.figlet_format("Hello, ASCII Art!")

#     # Print ASCII art
#     stdscr.addstr(0, 0, ascii_text)

#     # Refresh the screen
#     stdscr.refresh()

#     # Wait for user input before exiting
#     stdscr.getkey()
#     time.sleep(10)


# # Run the curses application
# curses.wrapper(main)
