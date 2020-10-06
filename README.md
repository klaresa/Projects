
# Projects
Here I add some projects I`ve done over the time.

- System App


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

![CPU SS](https://github.com/klaresa/Projects/blob/main/images/cpu-ss.PNG)

## Configuration

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