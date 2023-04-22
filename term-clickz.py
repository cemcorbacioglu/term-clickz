import curses
import random

def main(stdscr):
    # Configure the terminal and initialize colors
    curses.curs_set(0)
    stdscr.timeout(50)
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    # Initialize mouse support
    curses.mousemask(curses.ALL_MOUSE_EVENTS)

    particles = []

    while True:
        # Get the next input event
        event = stdscr.getch()

        # Check if it is a mouse event
        if event == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()

            # Create particles around the click position
            for _ in range(10):
                dx = random.randint(-5, 5)
                dy = random.randint(-5, 5)
                particle = {
                    'x': x,
                    'y': y,
                    'dx': dx,
                    'dy': dy,
                    'lifetime': 0
                }
                particles.append(particle)

        # Update particles
        new_particles = []
        for particle in particles:
            # Calculate new position
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']

            # Increment lifetime
            particle['lifetime'] += 0.4

            # Fade out particles
            if particle['lifetime'] < 10:
                new_particles.append(particle)

        particles = new_particles

        # Clear the screen
        stdscr.erase()

        # Draw particles
        for particle in particles:
            char = chr(random.randint(ord('!'), ord('~')))
            color = random.randint(1, curses.COLORS)
            try:
                stdscr.addstr(particle['y'], particle['x'], char, curses.color_pair(color))
            except curses.error:
                pass

        # Refresh the screen to display the new characters
        stdscr.refresh()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
