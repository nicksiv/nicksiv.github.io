(menu-bar-mode -1)
(tool-bar-mode -1)
(scroll-bar-mode -1)
(setq inhibit-splash-screen t)
(display-battery-mode 1)
(setq battery-mode-line-format "[%p% %b%t minutes] ")
(setq display-time-24hr-format t)
(setq display-time-day-and-date t)
(display-time-mode 1)
(global-hl-line-mode 1)
(global-font-lock-mode 1)                     ; syntax highlighting by default;
(fset 'yes-or-no-p 'y-or-n-p)                 ; Changes all yes/no questions to y/n type;
(setq visible-bell 1)                         ; No sound bell;
(setq current-language-environment "Greek")
(setq default-input-method "greek")           ; Change layout with C-\
(set-input-method "greek")
(setq auto-save-default nil)
(setq-default word-wrap 1)                    ; Natural reading, wrap at the word
(setq create-lockfiles nil)
(setq vc-follow-symlinks t)
(winner-mode nil)
(setq delete-by-moving-to-trash t) 
(show-paren-mode)
(fido-vertical-mode)
(require 'org-tempo) ; for <s [tab] to create script blocks
(ffap-bindings)  ; Enable find file at point
(global-auto-revert-mode 1) ; set file to auto refresh when change detected (For example, changed by other)

(recentf-mode 1)
(setq recentf-max-menu-items 25)
(setq recentf-max-saved-items 25)
(global-set-key "\C-x\ \C-r" 'recentf-open-files)

(make-directory "~/.tmp/emacs/auto-save/" t)
(setq auto-save-file-name-transforms '((".*" "~/.tmp/emacs/auto-save/" t)))
(setq backup-directory-alist '(("." . "~/.tmp/emacs/backup/")))
(setq backup-by-copying t)
;(setq make-backup-files nil) ; Do not make backup files

(setq orgDir "~/Documents")
(setq arcDir "~/Documents")

(setq org-hide-leading-stars t)
(setq default-major-mode 'org-mode);
(add-to-list 'auto-mode-alist '("\\.org\\'" . org-mode))
(add-to-list 'auto-mode-alist '("\\.txt\\'" . org-mode))
(setq org-use-fast-todo-selection t);
(setq org-return-follows-link t);
(setq org-agenda-files (list orgDir ))
(load-theme 'modus-vivendi t)
(if (display-graphic-p)
  (when (find-font (font-spec :name "Iosevka"))
  (set-face-attribute 'default nil :font "Iosevka-12")
  ))
(global-visual-line-mode t)

(global-set-key "\C-cl" 'org-store-link);
(global-set-key "\C-ca" 'org-agenda);
(global-set-key "\C-cb" 'org-iswitchb);
(define-key global-map "\C-cc" 'org-capture)
(global-set-key (kbd "<f5>") 'bookmark-bmenu-list)
(global-set-key [(control q)] 'kill-this-buffer)
(global-set-key (kbd "S-<f7>") 'ansi-term)
(global-set-key (kbd "<f7>") (lambda () (interactive) (switch-to-buffer "*ansi-term*")))
(global-set-key (kbd "<f12>") (lambda () (interactive) (dired orgDir) ))
(global-set-key (kbd "S-<f12>") (lambda () (interactive) (dired arcDir) ))
(global-set-key (kbd "C-c f") '("Quick open file" . (lambda ()  (interactive) (cd orgDir) (call-interactively 'find-file))))
(global-set-key (kbd "C-r") 'bookmark-jump)
(global-set-key (kbd "C-c d") (lambda () (interactive) (darkroom-mode 'toggle)))
(global-set-key (kbd "M-n") (lambda () (interactive) (org-next-link)))
(global-set-key (kbd "M-p") (lambda () (interactive) (org-previous-link)))
(global-set-key (kbd "C-<f6>") (lambda () (interactive) (org-toggle-link-display)))
(global-set-key (kbd "C-c t") 'modus-themes-toggle)

(setq gnus-select-method
'(nnimap "gmail" (nnimap-address "imap.gmail.com")
; it could also be imap.googlemail.com if that's your server.
(nnimap-server-port 993) (nnimap-stream ssl)))
;(add-to-list 'gnus-secondary-select-methods '(nnml ""))
;(add-to-list 'gnus-secondary-select-methods '(nntp "news.gnus.org"))

(setq message-send-mail-function 'smtpmail-send-it smtpmail-starttls-credentials
'(("smtp.gmail.com" 587 nil nil))
smtpmail-auth-credentials
'(("smtp.gmail.com" 587 "nsivridis@gmail.com" nil))
smtpmail-default-smtp-server "smtp.gmail.com"
smtpmail-smtp-server "smtp.gmail.com"
smtpmail-smtp-service 587
smtpmail-local-domain "yourdomain")

;; @see http://www.gnu.org/software/emacs/manual/html_node/gnus/Expiring-Mail.html
;; press 'E' to expire email
(setq nnmail-expiry-target "nnimap+gmail:[Gmail]/Trash")
(setq nnmail-expiry-wait 'immediate)

; Sort threads first by number, and then in reverse order by date
(setq gnus-thread-sort-functions
'(gnus-thread-sort-by-number
(not gnus-thread-sort-by-date)))

;; Make Gnus NOT ignore [Gmail] mailboxes
(setq gnus-ignored-newsgroups "^to\\.\\|^[0-9. ]+\\( \\|$\\)\\|^[\"]\"[#'()]")
(setq epa-pinentry-mode 'loopback) 
(global-set-key (kbd "<f8>") 'gnus)

(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))

(require 'ledger-mode)
(setq ledger-reports
  '(("income vs expense" "ledger [[ledger-mode-flags]] -f %(ledger-file) bal ^exp ^inc -n")
    ("new annual credit" "ledger [[ledger-mode-flags]] -f %(ledger-file) balance ^liabi -b 2024-01-01")
    ("position" "ledger [[ledger-mode-flags]] -f %(ledger-file) bal ass liab")
    ("expenses-month" "hledger -f %(ledger-file) balance  ^exp ^inc -M")
    ("income-statement (m)" "hledger -f %(ledger-file) incomestatement -M -b 2024-01-01 --depth 2")
    ("income-statement (y)" "hledger -f %(ledger-file) incomestatement -b 2024-01-01 --depth 2")

    ("bal" "%(binary) -f %(ledger-file) bal")
    ("reg" "%(binary) -f %(ledger-file) reg")
    ("payee" "%(binary) -f %(ledger-file) reg @%(payee)")
    ("account" "%(binary) -f %(ledger-file) reg %(account)")))

    (global-set-key (kbd "C-c s i") '("Ledger import this" . (lambda ()  (interactive) (nyko/ledger-import))))

    (defun nyko/ledger-import ()
      "Import active winbank txt file buffer to ledger"
      (interactive)
      (let ((filename (buffer-file-name)))
      (shell-command (concat "python3 ~/org/data/sys/ledger.py import " filename )  )
      )
      )

(require 'darkroom)
(darkroom-tentative-mode)
(setq darkroom-text-scale-increase 1)

;; Automatically tangle our Emacs.org config file when we save it
   (defun efs/org-babel-tangle-config ()
     (when (string-equal (buffer-file-name)
			 (expand-file-name "~/Documents/emacs-config.org"))
       ;; Dynamic scoping to the rescue
       (let ((org-confirm-babel-evaluate nil))
	 (org-babel-tangle))))

   (add-hook 'org-mode-hook (lambda () (add-hook 'after-save-hook #'efs/org-babel-tangle-config)))
