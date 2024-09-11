---
title: tmux
date:  2023-11-19
tags:  cli software tutorial
---

Learning tmux from the book **The Tao of tmux** by Tony Narlock.

* prefix-d : detach
  you re-attach by running tmux attach
  this is the best way to get out of the server while keeping tmux panes open
* prefix-[ : copy mode
  then press [space] to enter copy mode and start selection
  use arrow keys to make the selection
  press [enter] to copy
  press prefix-] to paste
* prefix-s : select session
  when there are more than one sessions running
  also prefix+( and prefix+) for previous/next sessions
* prefix-c : create window
  if you want to rename the window use prefix-,
  to move to previous/next window use prefix+p/n
  to select window use prefix+' and press tab for a list
  to change the location of a window use prefix+.
* prefix-x : kill window
  also ctrl+d dows the same
* prefix-% : split window horizontally
* prefix-" : split window vertically
* prefix-(arrow keys) : move between panes
  of prefix-o for next pane and prefix-; for previous
* prefix-z : zoom in/out current pane
* prefix-M-(arrow keys) : resize pane x5 step
* prefix-C-(arrow keys) : resize pane x1 step

# References
* <https://leanpub.com/the-tao-of-tmux/read][The Tao of tmux (book)>
* <https://github.com/rothgar/awesome-tmux>
