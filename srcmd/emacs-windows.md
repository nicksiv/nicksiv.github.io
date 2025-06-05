nyk0-nomikon - Emacs Windows installation

## Emacs Windows installation

Notes for required actions after installation of emacs on windows.

**Warning:** Emacs under Windows is soo slow\...

### Set home folder on Windows

Open Powershell in administrator mode and enter this line:\
`setx HOME %USERPROFILE%`

### Add to .emacs configuration file

    ;; Windows OS
    ;; Settings specific for Windows locale saving style

      (setq-default buffer-file-coding-system 'utf-8-unix)
      (setq buffer-file-coding-system 'utf-8-unix)

      (set-terminal-coding-system 'utf-8)
      ;(set-language-environment 'utf-8)
      (set-keyboard-coding-system 'utf-8)
      (prefer-coding-system 'utf-8)
      (setq locale-coding-system 'utf-8)
      (set-default-coding-systems 'utf-8)
      (set-terminal-coding-system 'utf-8)
      (setenv "LC_ALL" "C")
      

### Using Doc-View for windows (pdf display)

install [chocolatey](https://chocolatey.org/install)

`choco install xpdf-utils ghostscript`

### Gnus use of PGP for Windows

`choco install gnupg`

### Links

-   [Install doom-emacs on Windows](https://earvingad.github.io/posts/doom_emacs_windows/)
-   [Emacs on Windows](https://caiorss.github.io/Emacs-Elisp-Programming/Emacs_On_Windows.html)
