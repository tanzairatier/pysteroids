1. Overview
================================================================================
Title: Pysteroids: Asteroids in Python
Author: Joe Krall
When: January 2013
About: Built with Pygame for Python 2.7.  
Summary: Control your ship in playstyle-physics and shoot down asteroids to gain points, while evading them and keeping the ship healthy.  Items spawn that can improve ship components such as guns and provide shields for protection.

2. How-To-Play
================================================================================
Controls: Control the ship with either the A/D or Left/Right arrow keys for rotation, and the W/Up arrow keys for thrust.  The S/Down arrow keys apply a braking force, while space bar/left mouse click can be used to fire the ship's guns.  The Q key can be used while in a live game to quit and return to starting menu.

Non-Disconnecting Interface: The player is in control of the ship at all times.  This provides a non-disconnecting interface to the game.  In this manner, the player drives the ship into menu options to select them.

Items: Items sometimes spawn, and it is wise to pick them up before they disappear.  Each item is a sphere with a letter or a number inside to signify what its effect is.
(A): Increase the power of the ship's guns by 1.0.  When the power of the ship's guns surpass certain values, the color and size of the gun beams is changed to reflect its growing power.
(S): Increase the speed of the ship's guns.  The faster the speed of the shots, the better your accuracy can be.
(H): Provides the ship with a temporarily lasting shield which protects the ship from any danger.
(P): A package providing 2500 points to the player.  Every 10,000 points yields an extra ship-life.
(1): Improve the Type-I guns of the ship.  Type-I guns are standard spreader type guns, which can complement up to 5 beams at once in a small arc.
(2): Improve the Type-II guns of the ship.  Type-II guns are 360-degree spreader guns, ranging from 2-way, 4-way, 8-way and 32-way beams.  However, the ship can only fire a limited number of shots at once.  So the 32-way beam gun can likely only be fired once at a time.
(3): Improve the Type-III guns of teh ship.  Type-III guns are standard parallel shooters, ranging across double-shot, triple-shot and five parallel shots.

Tip: At the start of every level, the player has a temporary 3-second shield after enemies respawn, and is given three seconds notice before enemies respawn.

Tip: Combine the use of the mouse and space bar for rapid shooting.

3. List of Features (non-extensive):
================================================================================
 - Background of Stars
 - - Stars twinkle randomly
 - - Stars move at very slow and random directions, and wrap around to stay in screen

 - Ship Thrust Particle Effect
 - - When ship is moving, it propels from thrust which is vividly drawn as a particle effect

 - No Disconnected Interface
 - - From the moment the game begins, you interface the game with and only with the ship

 - Various Modes of Play
 - - Easy and Difficult Modes, and Insane
 - - Ship Painter & About/Help Screens

 - Music & Sound Effects
 - - Controlled, random selections of various background musics
 - - Controlled sound effects for a variety of in-game events such as shooting the ship's guns

 - Playstyle Space Physics
 - - A style of space physics which allow for a convenient control over the ship

 - Shooting
 - - Can shoot with the ship's guns.
 - - A variety of shot patterns and schemes

 - Keyboard & Mouse Input
 - - Accepts variety of keyboard input as well as mouse click input events

 - Drawing of Labels
 - - Labels drawn with convenient location tags that allow for ease of layout

 - Zero Image Loading  
 - - Reduction of image loading and restriction to procedurally generated content enhance system performance

 - Enemies
 - - Polygon type enemies have hp and other parameters that yield points when shot down
 - - Interior colors change according to current hp
 - - Enemy size shrinks relative to percentage of hp remaining
 - - Trail of debris when an enemy is hit

 - Countdown Timers
 - - Timer counts down to prepare you between rounds and at the start
 - - Temporary shield between levels

 - Ship Painter
 - - Adjust the color of your ship through the non-disconnective interface

 - Collision Bounce between Enemies
 - - Enemies bounce off each other through elastic collisions

 - Ship Blowups
 - - Cool particle effects when ship blows up