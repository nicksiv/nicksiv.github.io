nyk0-nomikon - Linux - music file management commands

## Linux - music file management commands

## Copy m3u playlist files in a folder

Run this script where the m3u playlist is stored

::: {#cb1 .sourceCode}
``` {.sourceCode .bash}
sed "s/#.*//g" < starFM.m3u | sed "/^$/d" | while read line; do (( COUNTER++ )); filename="${line##*/}"; cp "${line}" "/home/nick/export/starFM/$COUNTER - $filename"; done
```
:::

## Linux: Split flac, cue files

shnsplit is the program used to split tracks, while cuebreakpoints it reads the break-points from file.cue and pipe them to shnsplit.

### Install tools

    sudo apt-get install cuetools shntool flac

### Make the split

    cuebreakpoints file.cue | shnsplit -o flac file.flac

### Real example

    # step 1
    cuebreakpoints Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue | shnsplit -o flac Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.flac  -f Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue -t "%n. %t" Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.flac < Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue 

    # step 2
    # fill the tags (make sure the original flac is in another dir)

    cuetag Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue *.flac
