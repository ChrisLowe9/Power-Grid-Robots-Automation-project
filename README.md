# Power Grid Robots Automation project
This project aims to automate the Robots expansion for Power Grid, to assist players with using that expansion in their own games of Power Grid.

This is my first project, so it is very much a learning experience - all comments welcome. 
(I am sure I am making mistakes in terminology in the description)

I'm currently creating functions for creating dictionaries for the regions, cities, power plants, and resource market(s) so that gives the information that the robots will access to understand the game state.
Then (I think) I will create a 'player' class, that will hold information about what cities, power plants and resources the player has.
Then the robots will be a sub-class of the 'player' class, and I will create rules for the actions they will tell the human players to make for them.

The end goal is to put this into a website that human players can access, which will ask the human players for information about the game state and then tell the human players what actions to take for the robot player(s).
