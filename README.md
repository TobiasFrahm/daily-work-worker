# daily work worker
The daily work worker does the daily work for you.
Just a little backup here, a small system update there. 
All the stuff you should do on a daily bases.

--------------------------------------------------------
I use and test this with ```Linux 5.8.6-1-MANJARO x86_64 20.1 Mikah```
# Usage
I uses this as a simple alias in .xxxxrc file.
Just add the line

```alias  dww = "python3 absolute/path/to/daily_work_worker.py``` to your.rc file.
# Borg Backup
[borg](https://borgbackup.readthedocs.io/en/stable/) is a platform independent backup tool.
The daily work worker uses borg to backup your ```/home```folder per default.
You can change this by passing the ```-s , --source ``` argument.
If you want to backup several folders, pass them as a list e.g. ```-s "/home, /etc"```.

You MUST give a path of your borg repository by passing the ```repo```
argument. The daily work worker will name the backup as the given source folder is called, followed by the date.
I recommend to store your backup at an external hard drive which should be about twice the size your build in storage.
