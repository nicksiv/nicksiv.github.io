nyk0-nomikon - My Emacs writing setup

## My Emacs writing setup

## My writing setup

I like to use Emacs for as much as I can. Because I love it. It's fast, open source and gives your fingers real superpowers. So anything I write, posts, prose or whatever I use Emacs and I got installed a package just for it. It's called **Writeroom mode** and I it's available to me at the push of a shortcut.

![wroom](/images/wroom.png)

I will show you how to set it up along with some general instructions:

### Setup packages and install writeroom mode (for noobs)

To use writeroom mode you need to have access to the melpa package archive which is not setup by default into Emacs. Add the following to your .emacs file to enable it:

;; Package setup (setq package-archives (quote (("gnu" . "<http://elpa.gnu.org/packages/>") ("melpa" . "<https://melpa.org/packages/>"))))

After that change, restart Emacs (or run a M-x eval-buffer) and run M-x package-list-packages. You can search the list of packages after appearing with C-s and find what you're looking for, click on it and install.

*note: In emacs keyboard shortcuts M stands for Alt and C for Control. So M-x means Alt+X*

## My function

Writeroom mode makes Emacs full screen for distraction-free editing. But I needed bigger font for writing and the spellchecker on. So I quickly made a function (you can add it to your .emacs file after installing writeroom mode):

;; Activate writeroon and spellcheck (global-set-key \[f8\] (lambda () (interactive) (writeroom-mode)(flyspell-mode)(text-scale-set 1)(end-of-buffer)))

Now pressing F8 turns any buffer into a distraction free editor with spell checking enabled. Writing in this environment feels like typing on a real typewriter. It helps me focus so much that I would recommend it to anyone who prefers minimal writing environments.

You can customize additional settings of writeroom mode easily. Just run M-x customize-group and enter writeroom.

[Writeroom Project page](https://github.com/joostkremers/writeroom-mode) by Joost Kremers
