nyk0-nomikon - Using a batch file for a handy Windows command line launcher

## Using a batch file for a handy Windows command line launcher

For a Linux guy, working on a locked down Windows PC can be a pain sometimes. It would be nice to have my Linux terminal to run stuff but instead, I don't even have access to a DOS prompt.

To work down a solution, I've created a batch file and saved it under my user name's root. I call it s.bat. That means whenever I run **s** followed by a command I get to launch something. And by that I don't mean an application, but almost anything I can think of. Usually it's Excel workbooks. Several files which I should open them every day and I have absolutely no interest in looking for desktop shortcuts or recent file lists with my mouse. I would kill to use just my keyboard.

First I define the location of my Excel executable. Then I define one command named *report* which will open a specific Excel file.

Here's the code:

``` batch
set EXL="C:\Program Files (x86)\Microsoft Office\Office16\excel.exe"
if %~1 == report START "" %EXL% "D:\monthReport.xlsx"
```

Now all I have to do is bring up the Run dialog pressing Win+R and type in *s report*. That's all.

Later I have added a command for opening a folder:

``` batch
if %~1 == folder START "" "N:\my Folder"
```

I have a whole batch file with such commands. All I have to do is just remember them!

I found this trick quite convenient and it has been helping me for a couple of years now without fail.
