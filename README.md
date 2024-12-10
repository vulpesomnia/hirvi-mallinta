# Simulating Moose - Computational Science Course 2024
In this course we made a simplified moose simulation packed with a drone surveying system. The job of the drone is to count the moose in a specified area as accurately
as possible using LIDAR sensors. The goal of the project was to create a cost-effective way to count moose accurately in a specified area using drones. The simulation
was tested using parameters created using a nearly orthoganal latin hypercube and our group ran around 170 simulations.

## Simulation
The simulation was programmed using Python and Pygame. It has built-in time, physics and rendering systems. 

### Preset Assumptions
- The sun rises at 9am and sets at 3pm.
- It's winter around December.
- The area is a rectangle.

### Moose
- **Herds**
    - The size of a herd is 1 to 3 moose.
    - There is a leader for each herd.
- **Movement**
  - The moose move around in herds in their own territories.
  - The moose move in a line following a leader.
- **Rest**
    - The moose take 3 breaks during the day.
    - The moose sleep around half the time during the night.

### Drones
- **Movement**
    - The drone moves in a zigzag around the scannable area.
    - The speed of the drone is constant.
- **LIDAR**
    - The LIDAR can scan in a line up to 400m.

## Running the Simulation
The assumption is that a manned drone costs 100e/h and the investment costs are around 12000e.
After simulation the program outputs a list of useful statistics.

### Parameters
Parameters can be changed in the ``parameters.txt`` file. There are currenlty 7 parameters.
1. **MOOSE_DENSITY_PER_THOUSAND_HECTARES**
   - Changes the density of moose (Can be a decimal).
   - Does not change the maximum amount of moose in a territory.
2. **MOOSE_SPEED**
   - Modifies the moose of the speed in m/s.
3. **ACTIVE_REST**
   - Changes the length of rests after sunrise. (hours)
4. **LESS_ACTIVE_REST**
   - Changes the length of rests after sunset. (hours)
5. **MIN_TERRITORY_RADIUS**
   - Since territories a circle, this changes their minimum radius in meters.
7. **DRONE_SPEED**
   - Modifies the drone speed in m/s.
   - Speed is constant.
8. **STARTING_TIME**
   - Changes the starting time of the simulation.
   - Should be between 0 and 24.

<details>
  <summary>Extra Parameters</summary>
  Extra parameters can be found in the <code>src/settings.py</code> file.
  Modified default parameters in the <code>src/settings.py</code> will be
  overwritten by <code>parameters.txt</code>.
  <ul>
    <li><h4>MAP_HEIGHT & MAP_WIDTH</h4></li>
    <li><h4>PIXELS_PER_METER</h4></li>
    <li><h4>SCREEN_HEIGHT & SCREEN_WIDTH</h4></li>
    <li><h4>SIMULATION_SPEED</h4></li>
    <li><h4>SIMULATION_AMOUNT</h4></li>
    <li><h4>TOGGLE_RENDERING</h4></li>
  </ul>
</details>

## How to run the program?
1. Install Python and Pygame.
2. Clone the repository ``git clone git@github.com:vulpesomnia/hirvi-mallinta.git`` (Requires git).
3. Navigate into the source folder.
4. Run ``python main.py``

## License
This project is licensed under the [MIT License](https://github.com/vulpesomnia/hirvi-mallinta/blob/main/LICENSE). <br />
Please see the ``LICENSE`` file for more information.

## Acknowledgements
- **Programming & Designing:**
    - [Tommy Kroon](https://github.com/vulpesomnia)
    - [Lyydia Lehtinen](https://github.com/CalsiumOksidi) 
