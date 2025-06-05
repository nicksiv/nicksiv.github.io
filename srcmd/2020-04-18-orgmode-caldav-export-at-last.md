nyk0-nomikon - Orgmode caldav export at last!

## Orgmode caldav export at last!

Today's revelation: I learned that I can export all my dated entries from my org-mode agenda files into an ics file.\
I saved this file to my NextCloud folder (by setting the `org-icalendar-combined-agenda-file` variable) to import the file into my android phone which is tricky. The events are going into the default calendar of the device and there is no standard way to erase it and update your events. For this to work, I'm using another app, the simple calendar, which imports locally the file and later, everything can be erased to import an update.\
One change I had to make though, was to tell org-mode to include all SCHEDULED and DEADLINE timestamps by customizing the group `org-export-icalendar`. By default, org-mode exports only active timestamps.

So, after doing that I figured: Caldav could work now.

<https://github.com/dengste/org-caldav>\
And finally! Org-caldav works perfectly with my Nextcloud calendar. I have tried it twice in the past and couldn't get it to work because of that little setting.

Needless to say, that info exists into the documentation. I sould have RTFM...
