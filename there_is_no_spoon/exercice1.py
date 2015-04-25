import sys, math

# Don't let the machines win. You are humanity's last hope...


width = int(input()) # the number of cells on the X axis
height = int(input()) # the number of cells on the Y axis
grid = []
sys.stderr.write(str(grid) + "\n")

i = 0
for x in range(height):
    grid.append([])
            line = input() # width characters, each either 0 or .
                j = 0;
                    for c in line:
                        if c == '0' :
                            grid[i].append((j, i))
                        else:
                            grid[i].append((-1, -1))
                                                                                j += 1
                                                                                    i += 1
                                                                                    sys.stderr.write(str(grid)
                                                                                            + "\n")  

                                                                                    def get_right(x,
                                                                                            y):
                                                                                        x = x+1
                                                                                                while
                                                                                                    (x
                                                                                                            <
                                                                                                            len(grid[y])):
                                                                                                        if
                                                                                                                    (grid[y][x]
                                                                                                                            !=
                                                                                                                            (-1,
                                                                                                                                -1)):
                                                                                                                                return
                                                                                                                            "{}
                                                                                                                                        {}".format(*grid[y][x])
                                                                                                                                    else:
                                                                                                                                        x
                                                                                                                                                                +=
                                                                                                                                                                1
                                                                                                                                                                    return
                                                                                                                                                                "-1
                                                                                                                                                                -1"

                                                                                                                                                                def
                                                                                                                                                                get_bottom(x,
                                                                                                                                                                        y):
                                                                                                                                                                    y
                                                                                                                                                                        =
                                                                                                                                                                        y+1
                                                                                                                                                                            while
                                                                                                                                                                                (y
                                                                                                                                                                                        <
                                                                                                                                                                                        len(grid)):
                                                                                                                                                                                    if
                                                                                                                                                                                                (grid[y][x]
                                                                                                                                                                                                        !=
                                                                                                                                                                                                        (-1,
                                                                                                                                                                                                            -1)):
                                                                                                                                                                                                            return
                                                                                                                                                                                                        "{}
                                                                                                                                                                                                                    {}".format(*grid[y][x])
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    y
                                                                                                                                                                                                                                            +=
                                                                                                                                                                                                                                            1
                                                                                                                                                                                                                                                return
                                                                                                                                                                                                                                            "-1
                                                                                                                                                                                                                                            -1"


                                                                                                                                                                                                                                            i
                                                                                                                                                                                                                                            =
                                                                                                                                                                                                                                            0
                                                                                                                                                                                                                                            for
                                                                                                                                                                                                                                                y
                                                                                                                                                                                                                                                in
                                                                                                                                                                                                                                                grid:
                                                                                                                                                                                                                                                    j
                                                                                                                                                                                                                                                        =
                                                                                                                                                                                                                                                        0
                                                                                                                                                                                                                                                            for
                                                                                                                                                                                                                                                                x
                                                                                                                                                                                                                                                                in
                                                                                                                                                                                                                                                                y:
                                                                                                                                                                                                                                                                    if
                                                                                                                                                                                                                                                                                x
                                                                                                                                                                                                                                                                                !=
                                                                                                                                                                                                                                                                                (-1,
                                                                                                                                                                                                                                                                                        -1):
                                                                                                                                                                                                                                                                                    right
                                                                                                                                                                                                                                                                                                =
                                                                                                                                                                                                                                                                                                get_right(j,
                                                                                                                                                                                                                                                                                                        i)
                                                                                                                                                                                                                                                                                                bottom
                                                                                                                                                                                                                                                                                                            =
                                                                                                                                                                                                                                                                                                            get_bottom(j,
                                                                                                                                                                                                                                                                                                                    i)
                                                                                                                                                                                                                                                                                                            print("{}
                                                                                                                                                                                                                                                                                                                        {}
                                                                                                                                                                                                                                                                                                                        {}
                                                                                                                                                                                                                                                                                                                        {}".format(x[0],
                                                                                                                                                                                                                                                                                                                            x[1],
                                                                                                                                                                                                                                                                                                                            right,
                                                                                                                                                                                                                                                                                                                            bottom))
                                                                                                                                                                                                                                                                                                                        j
                                                                                                                                                                                                                                                                                                                                +=
                                                                                                                                                                                                                                                                                                                                1
                                                                                                                                                                                                                                                                                                                                    i
                                                                                                                                                                                                                                                                                                                                    +=
                                                                                                                                                                                                                                                                                                                                    1
