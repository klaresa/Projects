
# Projects
Here I add some projects I`ve done over the time.

- System App
- Github Repository (JavaScript)
- Github Repository (React)
- Todo Task List
- Games JS
- Draw it

---

<br>

### System App
 This is a project to monitor some pc specs such as CPU, Memory and Disk usage; CPU information on model, cores and architecture; and processes. All info is shown to the user through pygame module.

**Server and Client**
This project has both a **Server** and a **Client**.

**External Libs**
- pygame
- psutil
- cpuinfo
- netifaces

It was made for Windows so there is no support for other OS but it can be easily modded.
It handles multiple clients.

Python project.

![CPU SS](https://github.com/klaresa/Projects/blob/main/images/cpu-ss.PNG)

#### Configuration

In order to run these scripts you'll need to install all external libs cited.
The use of a virtual environment is suggested.

```python
pip install pygame
pip install psutil
pip install cpuinfo
pip install netifaces
```

Run server.py on server folder.
Run main.py on root.

**Important**:
`server.py` must be executed before `main.py`

---
<br>

### Github Repository (JavaScript)

Quick project on querying Github users repositories. No installations required, it can be open on your browser.

It uses querySelectors, onclick event and a promise function to query Githubs API.
Bootstrap was used to improve design.

Javascript only project.

![Github Repository (JavaScript) SS](https://github.com/klaresa/Projects/blob/main/images/gitrepo-js-ss.PNG)


#### Configuration
No aditional configuration needed for this project. You can simply open it on your browser.


---
<br>

### Github Repository (React)

Another project on GitHubs repositories yet using React framework.


**Modules**:
- BrowserRouter
- Switch
- Route

![Github Repository (React) SS](https://github.com/klaresa/Projects/blob/main/images/git-repo-ss.PNG)

#### Configuration
React lib is needed to run this project.


1. Install React
`npm install -g create-react-app
`

2. Create a React Project
`create-react-app your-project
`

3. Change to your projects directory
`cd your-project
`

4. Run the script on your package.json depending on your configuration
`npm start`
`yarn start`

**OBS**:
You can also merge both installation and creation of a new project if using NPM 5.2+
`npx create-react-app your-project
`

If these steps didnt work then check out reacts instructions: [here](http://https://reactjs.org/docs/getting-started.html "here")

---
<br>

### Todo Task List

As everyone studying programming must have their very own todo task list, here is mine!

Some methods for this project:
- querySelector()
- createElement()
- setAttibute()
- appendChild()
- localStorage()
- JSON.parse()

Javascript only project.


![Todo Task List (Javascript only) SS](https://github.com/klaresa/Projects/blob/main/images/gitrepo-js-ss.PNG)


#### Configuration
No further installation is required.

---
<br>

### Draw it

Draw it is a small pixel canvas. It is cool to draw stuff clicking on squares. You can save colors you like to use them later.


**Features**
- a bunch querySelectorAll()
- color input value
- className()
- a bunch of addEventListener()

Javascript only project.

![Draw it (Javascript only) SS](https://github.com/klaresa/Projects/blob/main/images/draw-it-ss.PNG)

---
<br>

### Games JS

Random Games created with Javascript only. These games were based on freecodecamp.orgs tutorial with Ania Kubow: [here](https://www.youtube.com/watch?v=lhNdUVh3qCc&t=3522s&ab_channel=freeCodeCamp.org "here")

After finishing some games you'll be understanding:
- querySelector()
- addEventListeners()
- createElement()
- setAttribute()
- getAttribute
- appendChild()
- classList.add() / classList.remove() / classList.contains()
- setInterval()
- clearInterval()
- pop() / push() / unshift()
- forEach()
- arrow functions
...and more.

Javascript only project.


**Games**

1. *Connect Four*
 This games purpose is to connect four balls in a row. Whoever does it first wins the match. Two players.

 ![Connect Four](https://github.com/klaresa/Projects/blob/main/images/connect-four-ss.PNG)

2. *Memory Game*

 Simple game for one player that one must unravel all cards by matching its pictures.

 ![Memory Game](https://github.com/klaresa/Projects/blob/main/images/memory-game-ss.PNG)

3. *Nokia 3310 Snake*

 Classic snake game featured on Nokia phones. One player game.

 ![Snake Game](https://github.com/klaresa/Projects/blob/main/images/snake-game-ss.PNG)

4. *Space Invaders*

 Space Invaders game, thats the only description it takes. One player game. Kill those aliens!

  ![Space Invaders Game](https://github.com/klaresa/Projects/blob/main/images/space-game-ss.PNG)

5. *Whack-a-Mole*

 Just click on that hotdog as fast as you possibly can to score high!
 
![Whack-a-Mole Game](https://github.com/klaresa/Projects/blob/main/images/whack-game-ss.PNG)