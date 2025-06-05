nyk0-nomikon - Emacs google calendar

## Emacs google calendar

Due to lack of easy solutions to view my google calendar without having\
to open my browser, I have emacs downloading my calendar as ics.

I use my private address and make a diary out of it. Then it shows up in\
my agenda.

Of course I cannot create new entries, but it suits me fine.

To update the calendar I run the function `nyko/getcals`

      ; DIARY WITH GOOGLE CALENDAR
      (setq diaryDir "~/Documents/diary/")
      (setq diary-file (concat diaryDir "nyk0"))
      (setq org-agenda-include-diary t)
      (setq org-agenda-insert-diary-extract-time t)
      (add-hook 'diary-list-entries-hook 'diary-sort-entries t)
      (add-hook 'diary-list-entries-hook 'diary-include-other-diary-files)
      (add-hook 'diary-mark-entries-hook 'diary-mark-included-diary-files)
      (setq diary-list-entries-hook '(diary-include-other-diary-files diary-sort-entries))

      ; calendars you want to download
      ; each item links to a remote iCal calendar
      (setq calendars
        '(
          ("nyk0" . "private address of galendar file")
           ))

      (defun getcal (url file)
      "Download ics file and add it to file"
      (let ((tmpfile (url-file-local-copy url)))
      (icalendar-import-file tmpfile file)
      (kill-buffer (car (last (split-string tmpfile "/"))))))

      (defun nyko/getcals ()
      "Load a set of ICS calendars into Emacs diary files"
      (interactive)
      (find-file (concat diaryDir "nyk0"))
      (erase-buffer)
      (getcal "private address of google calendar" (concat diaryDir "nyk0"))
      (kill-this-buffer)

      )

In order to import more than one calendars, you need to update each\
calendar to its own file and create a global diary file listing all the\
calendars.

Then you just define the global diary file as your default diary with\
`(setq diary-file (concat diaryDir "globalfile"))`

### Backlinks

[emacs news 2024-09-02 \>\
Other](https://sachachua.com/blog/2024/09/2024-09-02-emacs-news/)
