from mazerunner import MazeRunner
import pickle


def print_menu(maze):
    options = ["Generate a new maze", "Load a maze"]
    if maze:
        options.extend(["Save the maze", "Display the maze", "Find the escape"])
    options = [str(i + 1) + '. ' + option for i, option in enumerate(options)]
    options.append("0. Exit\n")
    options.insert(0, "=== Menu ===")
    return int(input("\n".join(options)))


def generate_maze(dim):
    m_r = MazeRunner(dim, dim)
    m_r.make_maze()
    return m_r


def save_maze(file, maze):
    with open(file, 'wb') as p_file:
        pickle.dump(maze, p_file)


def load_maze(file):
    with open(file, 'rb') as p_file:
        return pickle.load(p_file)


if __name__ == '__main__':
    my_maze = None
    while True:
        m = print_menu(my_maze)
        if not m:
            print("Bye!")
            break
        if m == 1:
            dim = int(input("Please, enter the size of a maze\n"))
            if dim:
                my_maze = generate_maze(dim)
                my_maze.print_maze()
            else:
                print("Incorrect dimensions")
        elif m == 2:
            my_maze = load_maze(input())
        elif m == 3:
            save_maze(input(), my_maze)
        elif m == 4:
            my_maze.print_maze()
        elif m == 5:
            my_maze.find_escape()



