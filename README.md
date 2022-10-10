# Alchemy-Data-Analytics
Python Code that generates correlation heatmaps for Alchemy Data Analytics Project

## Installation
1. Clone current repository: `git clone` 
2. `cd` to project directory: `cd /path/to/cloned/repo`
3. Download python requirements: `pip3 install -r requirements.txt`

## Usage
```
School@pop-os:~/Documents/Fall 2022/INFO-465/heatmap$ python3 heatmap.py --help
                                                                                                                      
 Usage: heatmap.py [OPTIONS] COMMAND [ARGS]...                                                                        
                                                                                                                      
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell.           │
│                                                              [default: None]                                       │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it   │
│                                                              or customize the installation.                        │
│                                                              [default: None]                                       │
│ --help                                                       Show this message and exit.                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ full-gwp-heatmap           Creates Full Correlation Heatmap by GWP                                                 │
│ high-corr-heatmap          Creates Correlation Heatmap PNG by GWP with correlations >= 0.8                         │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


**Full High Correlation Heatmap example:**
```
School@pop-os:~/Documents/Fall 2022/INFO-465/heatmap$ python3 heatmap.py full-gwp-heatmap --help
                                                                                                                      
 Usage: heatmap.py full-gwp-heatmap [OPTIONS] FILENAME PICNAME                                                        
                                                                                                                      
 Creates Full Correlation Heatmap by GWP                                                                              
 This requires FILENAME and PICNAME                                                                                   
                                                                                                                      
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    filename      TEXT  CSV Data File [default: None] [required]                                                  │
│ *    picname       TEXT  Correlation Matrix PNG image [default: None] [required]                                   │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

```
Template: 
python3 heatmap.py high-corr-heatmap <CSV FILEPATH> <OUTPUT PNG IMAGE>

Practical Example: 
python3 heatmap.py high-corr-heatmap ../imputedset-2.csv pic-2.png
```

**Full GWP Correlation Heatmap example:**
```
School@pop-os:~/Documents/Fall 2022/INFO-465/heatmap$ python3 heatmap.py high-corr-heatmap --help
                                                                                                                      
 Usage: heatmap.py high-corr-heatmap [OPTIONS] FILENAME PICNAME                                                       
                                                                                                                      
 Creates Correlation Heatmap PNG by GWP with correlations >= 0.8                                                      
 This requires FILENAME and PICNAME                                                                                   
                                                                                                                      
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    filename      TEXT  CSV Data File [default: None] [required]                                                  │
│ *    picname       TEXT  Correlation Matrix PNG image [default: None] [required]                                   │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

```
Template: 
python3 heatmap.py full-gwp-heatmap <CSV FILEPATH> <OUTPUT PNG IMAGE>

Practical Example: 
python3 heatmap.py full-gwp-heatmap ../imputedset-2.csv pic-2.png
```
