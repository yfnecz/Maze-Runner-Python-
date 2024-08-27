 
The maze is generated using the algorithm based on the construction of a minimal spanning tree: [Randomized Prim's Algorithm](https://www.youtube.com/watch?v=cQVH4gcb3O4).

The path to exit the maze is found by Breadth First Traversal ( BFS ) 

Pickle Python module is used to save/load existing maze from file.

Example of execution:

```text
=== Menu ===
1. Generate a new maze
2. Load a maze
0. Exit
1
Please, enter the size of a maze
17
██████████████████████████████████
        ██                  ██  ██
██  ██████████████████  ██████  ██
██              ██              ██
██████████  ██████████████  ██████
██                              ██
██████████  ██████████████  ██████
██              ██      ██      ██
██████████████████  ██████  ██████
██              ██              ██
██████████  ██████████  ██████████
██      ██                      ██
██  ██████████████  ██████████████
██                              ██
██  ██████████████  ██████████████
██      ██                        
██████████████████████████████████


=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
3
maze.dat
=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
5
██████████████████████████████████
////    ██                  ██  ██
██//██████████████████  ██████  ██
██//////////    ██              ██
██████████//██████████████  ██████
██        //////////////////    ██
██████████  ██████████████//██████
██              ██      ██//    ██
██████████████████  ██████//██████
██              ██    //////    ██
██████████  ██████████//██████████
██      ██        //////        ██
██  ██████████████//██████████████
██                //            ██
██  ██████████████//██████████████
██      ██        ////////////////
██████████████████████████████████


=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
1
Please, enter the size of a maze
27
██████████████████████████████████████████████████████
                      ██          ██              ████
████████  ██████████████  ██████████████  ████████████
████                                              ████
████  ██████████████████  ██████████  ████████████████
████              ██              ██              ████
████  ██████████████████████████████  ████████████████
████                              ██              ████
████  ██████████████  ██████████████████████  ████████
████              ██      ██          ██          ████
████  ██████████████████████  ██████████████████  ████
████                                      ██      ████
████  ██████████████████████  ██████████████████  ████
████      ██              ██              ██      ████
████  ██████  ██████████████████████████████████  ████
████                      ██      ██          ██  ████
████  ██████  ██████████████  ██████  ████████████████
████      ██              ██                      ████
████████████  ██████████████████  ████████████████████
████                                      ██      ████
████████  ██████████████████  ██████  ██████  ████████
████                      ██      ██              ████
████████  ██████████████████████████████  ████████████
████                          ██      ██          ████
████  ██████  ██████  ██████████  ██████████  ████████
████      ██      ██                      ██          
██████████████████████████████████████████████████████



=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
5
██████████████████████████████████████████████████████
//////////            ██          ██              ████
████████//██████████████  ██████████████  ████████████
████//////                                        ████
████//██████████████████  ██████████  ████████████████
████//            ██              ██              ████
████//██████████████████████████████  ████████████████
████//                            ██              ████
████//██████████████  ██████████████████████  ████████
████//            ██      ██          ██          ████
████//██████████████████████  ██████████████████  ████
████//                                    ██      ████
████//██████████████████████  ██████████████████  ████
████//    ██              ██              ██      ████
████//██████  ██████████████████████████████████  ████
████//////////            ██      ██          ██  ████
████  ██████//██████████████  ██████  ████████████████
████      ██//            ██                      ████
████████████//██████████████████  ████████████████████
████        //////////////////////////    ██      ████
████████  ██████████████████  ██████//██████  ████████
████                      ██      ██//////        ████
████████  ██████████████████████████████//████████████
████                          ██      ██//////    ████
████  ██████  ██████  ██████████  ██████████//████████
████      ██      ██                      ██//////////
██████████████████████████████████████████████████████


=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
2
maze.dat
=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
4
██████████████████████████████████
        ██                  ██  ██
██  ██████████████████  ██████  ██
██              ██              ██
██████████  ██████████████  ██████
██                              ██
██████████  ██████████████  ██████
██              ██      ██      ██
██████████████████  ██████  ██████
██              ██              ██
██████████  ██████████  ██████████
██      ██                      ██
██  ██████████████  ██████████████
██                              ██
██  ██████████████  ██████████████
██      ██                        
██████████████████████████████████



=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
5
██████████████████████████████████
////    ██                  ██  ██
██//██████████████████  ██████  ██
██//////////    ██              ██
██████████//██████████████  ██████
██        //////////////////    ██
██████████  ██████████████//██████
██              ██      ██//    ██
██████████████████  ██████//██████
██              ██    //////    ██
██████████  ██████████//██████████
██      ██        //////        ██
██  ██████████████//██████████████
██                //            ██
██  ██████████████//██████████████
██      ██        ////////////////
██████████████████████████████████



=== Menu ===
1. Generate a new maze
2. Load a maze
3. Save the maze
4. Display the maze
5. Find the escape
0. Exit
0
Bye!
```
