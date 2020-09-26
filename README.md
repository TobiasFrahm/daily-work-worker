# daily work worker
The daily work worker does the daily work for you.
Just a little backup here, a small system update there. 
All the stuff you should do on a daily bases.

--------------------------------------------------------
I use this for ```Linux 5.8.6-1-MANJARO x86_64 20.1 Mikah```

# Borg Backup
[borg](https://borgbackup.readthedocs.io/en/stable/) is a platform independent backup tool.
The daily work worker uses borg to backup your per default your ```/home```folder.
You can change this by passing the ```-s , --source ``` argument.
You MUST give a path where to store the backups by passing the ```--backup-path```
argument. The daily work worker will name the backup as the given source folder is called, followed by the date.


# Status
Pretty raw, pretty much work in progress.
Use it if you understand it, if not wait for a more elaborated status.
