# DarkSpace
A Discord bot for getting the link to your next online class.

# Requirements
Can be installed using `pip install -r requirements.txt`

- Python 3.0+
- Discord.py
- python-dotenv

# Running in Docker
Start DarkSpace: `bash start.sh` or `./start`
Stop DarkSpace: `bash stop.sh` or `./stop`
    -> Can remove the docker container using -f flag with `stop.sh`

# TODO:
- Add checks in bash script for docker being installed and install and run it if
  it isn't.

# Usage
To add your own timetable and classroom links, you can create a "timetable.csv"
file following the format in sample.csv.

Format: [\<day\>,\<hour\>,\<moduleName\>,\<hyperlink\>]

# Commands
## !currentClass
**Usage**: !currentClass

Messages the link to the online classroom for the class at this current hour on
this current day.

If there is no class right now, it will message with information about how to
use !nextClass to find your next class today.
## !nextClass
**Usage**: !nextClass

Messages the link to the online classroom for the next class today (not
including the current hour).

If there is no class today, it will message informing you of this and tell you
to have some fun!
