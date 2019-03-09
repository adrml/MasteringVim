---
author: Greg Ippolito
description: |
    VI and VIM Linux editor tutorial of advanced editing features and
    tricks. This tutorial covers advanced use, tagging, vim plugins and
    integration with cscope. The YoLinux portal covers topics from desktop
    to servers and from developers to users
keywords: 'vi,vim,tutorial,advanced,linux,unix,vi editor,vi guide,vi help'
title: 'VI and VIM editor: Tutorial and advanced features'
viewport: 'width=device-width, initial-scale=1'
---

[]() []()
<div class="container-fluid">

<div class="row" itemprop="breadcrumb">

1.  [<span itemprop="name">Home</span>](/)
2.  [<span itemprop="name">Tutorials</span>](/TUTORIALS/)
3.  [<span itemprop="name">Linux Text
    Editors</span>](/TUTORIALS/LinuxTextEditors.html)
4.  [<span itemprop="name">vi and
    vim</span>](/TUTORIALS/LinuxTutorialAdvanced_vi.html)

</div>

<div class="row">

<div class="col-sm-3 top-space">

[![Yolinux.com
Tutorial](images/YoLinux_Tutorial_logo.png)](http://www.yolinux.com/)

</div>

<div class="col-sm-9">

Linux vi and vim editor: Tutorial and advanced features
=======================================================

<div class="ad-head" align="center">

</div>

</div>

</div>

<div class="row">

<div id="globalNavigation">

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  search   **  |   [Home Page](/ "YoLinux Home Page"){.menubar} |  [Linux Tutorials](/TUTORIALS/ "YoLinux Web Site Tutorials Index"){.menubar} |  [Terms](/YoLinux-Terms.html "YoLinux.com terms of use"){.menubar} |  [Privacy Policy](/privacy.html "YoLinux.com privacy policy"){.menubar} |  [Advertising](/YoLinux-Advertising.html "Advertising rates for YoLinux.com"){.menubar} |  [Contact](/YoLinuxEmailForm.html "Send us an email"){.menubar}  | **
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

</div>

<div class="yo-row">

<div id="leftcol">

<div class="sectionv1">

**Related YoLinux Tutorials:**

°[Text Editors](LinuxTextEditors.html)

°[Emacs and C/C++](LinuxTutorialXemacs.html)

°[Software development tools](LinuxTutorialSoftwareDevelopment.html)

°[C++ Info, links](LinuxTutorialC++.html)

°[YoLinux Tutorials Index](index.html)

</div>

<div class="sectionv2">

------------------------------------------------------------------------

------------------------------------------------------------------------

[Free Information Technology Magazines and Document Downloads\
![TradePub link
image](images/TradePubMagazines.gif)](http://yolinux.tradepub.com/)

</div>

</div>

<div id="content">

<div class="labelbar">

Vim Intro:

</div>

This "**vi**" tutorial is intended for those who wish to master and
advance their skills beyond the basic features of the basic editor. It
covers buffers, "**vi**" command line instructions, interfacing with
UNIX commands, and ctags. The **vim** editor is an enhanced version of
**vi**. The improvements are clearly noticed in the handling of tags.

The advantage of learning **vi** and learning it well is that one will
find **vi** on all Unix based systems and it does not consume an
inordinate amount of system resources. Vi works great over slow network
ppp modem connections and on systems of limited resources. One can
completely utilize vi without departing a single finger from the
keyboard. (No hand to mouse and return to keyboard latency)

NOTE: Microsoft PC Notepad users who do not wish to use "**vi**" should
use "`gedit`" (GNOME edit) or "`gnp`" (GNOME Note Pad) on Linux. This is
very similar in operation to the Microsoft Windows editor, "Notepad".
(Other Unix systems GUI editors: "dtpad", which can be found in
`/usr/dt/bin/dtpad` for AIX, vuepad on HP/UX, or xedit on all Unix
systems.)

See our list of [Linux GUI editors](LinuxTextEditors.html)

<div class="labelbar">

Vim Installation:

</div>

Red Hat / CentOS / Fedora:

-   `rpm -ivh vim-common-...rpm vim-minimal-...rpm vim-enhanced-...rpm vim-X11-...rpm`
-   `yum install vim-common vim-minimal vim-enhanced vim-X11`

Ubuntu / Debian:
-   `apt-get install vim vim-common vim-gnome             vim-gui-common vim-runtime`

Compiling Vim from source:
-   Download vim source from `http://vim.org`
-   `tar xzf vim-7.0.tar.gz`
-   `cd vim70`
-   `./configure --prefix=/opt             --enable-cscope`
-   `make`
-   `make install`

<div class="labelbar">

Vi/Vim Command Line Arguments:

</div>

Command usage: `vim [arguments] filename1 [filename2 ...]`

Vim arguments are listed in this table:
  --------------------------------------------------------------------------------------------------------------------------------------
  Arguments         Description
  ----------------- --------------------------------------------------------------------------------------------------------------------
  +\[num\]          Open editor with cursor on line "num". If "num" is not specified, the cursor will be on the last line of the file.

  +/{pat}           Open editor with cursor on the first occurrence of {pat}.

  -c {command}\     A "ex" command in dowble quotes will be processed against the file specified.
  --cmd {command}   

  -b                Binary file mode.

  -C\               VI compatibility mode. Loses the more advanced vim features.
  -v                

  -d                Diff file mode. Must list all files to perform a diff upon (list 2, 3 or 4 files). Same as vimdiff.

  -g                GUI gvim mode (if compiled in and available).

  -h\               Print help messages. Also see `vimtutor`
  --help            

  -i *filename*     Specify viminfo file. Default is `~/.viminfo`

  -r\               Recovery mode. Used after a crash. The ".swp" file is used. See ":help recovery".
  -L                

  -M\               File modifications and write not allowed.
  -R                

  -n                Prohibit ".swp" file generation. Required for special devices of limited space.

  -x                Use encryption when writing files. Will prompt for a crypt key.

  --noplugin        Skip loading plugins.

  --version         Print vim version.
  --------------------------------------------------------------------------------------------------------------------------------------

<div class="labelbar">

Basic "vi" features:

</div>

One edits a file in `vi` by issuing the command: `vi file-to-edit.txt`

The vi editor has three modes, command mode, insert mode and command
line mode.

1.  **Command mode:** letters or sequence of letters interactively
    command vi. Commands are case sensitive. The ESC key can end
    a command.
2.  **Insert mode:** Text is inserted. The ESC key ends insert mode and
    returns you to command mode. One can enter insert mode with the "i"
    (insert), "a" (insert after), "A" (insert at end of line), "o" (open
    new line after current line) or "O" (Open line above current line)
    commands.
3.  **Command line mode:** One enters this mode by typing ":" which puts
    the command line entry at the foot of the screen.

Partial list of interactive commands:

**Cursor Movement Commands:**
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Keystrokes    Action
  ------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  h/j/k/l       Move cursor left/down/up/right

  spacebar      Move cursor right one space

  -/+           Move cursor down/up in first column

  ctrl-d\       Scroll **d**own one half of a screen.\
  n ctrl-d      Set scroll to "n" lines. New default set for half screen.

  ctrl-u\       Scroll **u**p one half of a screen\
  n ctrl-u      Set scroll to "n" lines. New default set for half screen.

  ctrl-f\       Scroll **f**orward one screen\
  n ctrl-f      Scroll forward "n" screen

  ctrl-b\       Scroll **b**ack one screen\
  n ctrl-b      Scroll back "n" screen

  ctrl-y\       Scroll forward one line\
  n ctrl-y      Scroll forward "n" lines

  ctrl-e\       Scroll back one line\
  n ctrl-e      Scroll back "n" lines

  M (shift-m)   Move cursor to middle of page

  H (shift-h)   Move cursor to top of page

  L (shift-l)   Move cursor to bottom of page

  W\            Move cursor a **word** at a time (white space delimited)\
  w\            Move cursor a word at a time (first non-alphanumeric)\
  5w            Move cursor ahead 5 words

  B\            Move cursor **back** a word at a time (white space delimited)\
  b\            Move cursor back a word at a time (first non-alphanumeric)\
  5b            Move cursor back 5 words

  E\            Move cursor to **end** of word (white space delimited)\
  e\            Move cursor to end of word (first non-alphanumeric)\
  5e            Move cursor ahead to the end of the 5th word

  0 (zero)      Move cursor to beginning of line

  :30           Move cursor to line thirty

  \$            Move cursor to end of line

  )             Move cursor to beginning of next sentence (delimeted by ".", "?" or "!")

  (             Move cursor to beginning of current sentence

  }             Move cursor to beginning of next paragraph (delimeted by blank line or nroff macros: .IP, .LP, .PP, .QP, .P, .LI and .bp) Also see "set paragraphs" to define a paragraph.

  {             Move cursor to beginning of current paragraph

  \]\]          Move cursor to beginning of next section (delimeted by nroff macros: .NH, .SH, .H, .HU). Also see "set sections" to define a section.

  \[\[          Move cursor to beginning of current section

  G             Move cursor to end of file

  %             Move cursor to the matching bracket.\
                Place cursor on {}\[\]() and type "%".\
                Use the [matchit](http://www.vim.org/scripts/script.php?script_id=39) or [xmledit](http://www.vim.org/scripts/script.php?script_id=301) plug-in to extend this capability to XML/XHTML tags.

  '.            Move cursor to previously modified line.

  m\            Mark the line on which the cursor resides. Marking requires an identifier.\
  ma            Mark the line as identified by the letter "a" by marking with keystroke "ma"

  'a            Move cursor to line mark "a" generated by marking with keystroke "ma"

  'A            Move cursor to line mark "A" (global between buffers) generated by marking with keystroke "mA"

  \]'           Move cursor to next lower case mark.

  \['           Move cursor to previous lower case mark.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Editing Commands:**

  ------------------------------------------------------------------------------------------------------------------------------------------
  Keystrokes   Action
  ------------ -----------------------------------------------------------------------------------------------------------------------------
  i            Insert at cursor. Puts you in insert mode. Must use esc key to terminate insert mode.

  I            Insert before the cursor. Puts you in insert mode. Must use esc key to terminate insert mode.

  a            Append after cursor. Puts you in insert mode. Must use esc key to terminate insert mode.

  A            Append at end of line. Puts you in insert mode. Must use esc key to terminate insert mode.

  o            Open a new line below the current cursor position. Also puts you in insert mode. Must use esc key to terminate insert mode.

  O            Open a new line above the current line. Also puts you in insert mode. Must use esc key to terminate insert mode.

  ESC          Terminate insert mode. Terminates most other modes as well.

  u            Undo last change

  U            Undo all changes to entire line

  dd\          Delete line (stored in local buffer)\
  3dd          Delete 3 lines (stored in local buffer).

  D            Delete contents of line after cursor

  C            Delete contents of line after cursor and insert new text. Press esc key to end insertion.

  dw\          Delete word\
  4dw\         Delete 4 words\
  d)\          Delete to end of sentence\
  d\$\         Delete all characters from cursor to end of line\
  d-\          Delete current and previous line\
  dfx\         Delete from cursor to first occurance of the letter "x"\
  d'x\         Delete from the current line to the line marked with the identifier "x"\
  'ad'b\       Delete from the line of mark "a" to the line marked "b".\
  d/cat        Delete all characters from the cursor to the next occurance of (but not including) "cat"

  cw\          Change word\
  c)\          Change sentence\
  c\$          Change from cursor to end of line\
               (See "d" delete above for other variations)

  x            Delete character at cursor

  X            Delete character before cursor

  Y\           Yank (copy) current line into "unnamed" storage buffer.
  or\          
  yy           

  p            Paste unnamed storage buffer after current line.

  P            Paste unnamed storage buffer before current line.

  r            Replace character

  R            Overwrite characters from cursor onward

  s            Substitute one character under cursor continue to insert

  S            Substitute entire line and begin to insert at beginning of line

  J            Join current and following line into one line

  \~           Change case of individual character

  ctrl-a\      Increment number under the cursor.\
  ctrl-x       Decrement number under the cursor.

  .            repeat last command action.
  ------------------------------------------------------------------------------------------------------------------------------------------

**Control Characters:** Note that to enter control characters while in
insert mode, prefix the the control character with "ctrl-v" and then
type the control character (ex. Carriage control: ctrl-M, Form feed:
ctrl-L, Backspace: ctrl-H, Delete: ctrl-P, ...). Each control character
must first be preceeded by ctrl-v while in insert mode.
**Delete/Restore Buffers:** Each time you delete or yank a line, it is
stored in a local buffer and can be recalled and pasted. See "vi line
buffers" examples below.

**Search Commands:**

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Keystrokes                          Action
  ----------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  /*search\_string*{CR}               Search for *search\_string*

  ?*search\_string*{CR}               Search backwards (up in file) for *search\_string*

  /\\&lt;*search\_string*\\&gt;{CR}   Search for *search\_word*\
                                      Ex: /\\&lt;s\\&gt;\
                                      Search for variable "s" but ignore declaration "string" or words containing "s". This will find "string s;", "s = fn(x);", "x = fn(s);", etc

  n                                   Find **n**ext occurrence of search\_word

  N                                   Find previous occurrence of search\_word

  fx\                                 Move cursor to **f**irst occurance of letter "x" after the cursor but in the same line\
  nfx\                                Move cursor to "n"th occurance of letter "x" in line\
  ;                                   Go to next occurance in line

  Fx\                                 Move cursor backwards to next occurance of letter "x" in line\
  nFx\                                Move cursor backwards to "n"th occurance of letter "x" in line\
  ;                                   Go to previous occurance in line

  tx\                                 Move cursor to one char before the next occurance of letter "x" in line\
  ntx\                                Move cursor to one char before the "n"th occurance of letter "x" in line.\
  ;                                   Go to one char before the next occurance in line

  Tx\                                 Move cursor backwards to one char before the next occurance of letter "x"\
  nTx\                                Move cursor backwards to one char before the "n"th occurance of letter "x"\
  ;                                   Go to one char before previous occurance in line
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Where search strings can have the following patterns:
  Pattern            Description
  ------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  .                  A period matches any single character
  \^                 Finds the beginning of a line
  \^A                Finds the beginning of a line where the first character is the letter 'A'
  \$                 Matches the end of a line
  \[abc\]            Matches a string which contains any of the letters (a, b or c) between the brackets
  \\                 Turn off the special meaning of a character. Example "\\." does not match the period to any character but to the period character specifically
  \\d                Match any single digit (0 to 9)
  \*                 A search expression followed by a '\*' matches zero or more of the search expression. For example "A\*" will match A, AA and AAA
  +                  Same as '\*' above except that it matches one or more of the search expression.
  ?                  Same as '\*' and "+" except that it matches zero or one occurances
  string1|string2    Match any either string 1 or string 2
  a.b                Matches a string beginning with the letter 'a' followed by any character, again followed by the letter 'c'
  \^.\$              Matches an entire line containing only a single character
  a(b\*|c\*)d        Matches a string beginning with the letter 'a' followed by zero or more of the letter 'b', followed by zero or more of the letter 'c' and then followed by the letter 'd'
  Linux.\*Linux      Finds a line containing two instances of the string "Linux"
  .\* \[a-z\]+ .\*   Finds a line containing a word comprised of all lower case letters with a single blank on either side of the word

**Information Commands:**

  -----------------------------------------------------------------------------------------------
  Keystrokes    Action
  ------------- ---------------------------------------------------------------------------------
  ctrl-g\       List file info: fine name, number of lines in file, position of cursor in file.
  or\           
  :f            

  :set list\    Show tabs and end of line markers\
  :set nolist   Turn of tab and eol markings

  :args         Show command line arguments used
  -----------------------------------------------------------------------------------------------

Terminate session:

-   Use command: ZZ\
    Save changes to current file and quit.
-   Use command line: "`:wq`"\
    Save (write) changes to current file and quit.
-   Use command line: "`:w`"\
    Save (write) changes to current file without quitting.
-   Use command line: "`:w!`"\
    Save (write) changes to current file overriding the file permissions
    if the user has the privileges to change the file permissions. For
    example this will save a file with read only privileges if the user
    is the owner or has the ability to modify the privileges to allow
    a write. This will not permanently modify the file privileges. Note
    that there is no space between the two characters. A space will
    infer that the output is streamed to a Unix command following
    the "!".
-   Use command line: "`:w filename`"\
    Save (write) changes to a new file of name "*filename*"
    without quitting.
-   Use command line: "`:q!`"\
    Ignore changes and quit. No changes from last write will be saved.
-   Use command line: "`:qa`"\
    Quit all files opened.

New session:

-   Use command: "`:e filename`"\
    Start new edit session on specified file name without closing
    current vi / vim editor process.

<div class="labelbar">

Vi/Vim modes:

</div>

Vi/Vim modes are set using the "set" command and its many options.

**:set all** - display all mode settings of your editing session.\
**:set termcap** - display terminal settings of your editing session.

**:set ic** - Change default to ignore case for text searches\
Default is changed from noignorecase to ignorecase. (ic is a short form
otherwise type **set ignorecase**)

Common options to set:\
Full "set" Command
Short form
Description
:set autoindent\
:set noautoindent
:set ai\
:set noai
{CR} returns to indent of previous line.\
Turn on autoindent: `:set ai`\
Turn off autoindent: `:set noai`\
Set indent width: `set shiftwidth=4`\
Intelligent auto-indent: `set smartindent`\
Toggle autoindent on/off when pasting text (press F2 key to toggle mode
after one is in "insert" mode): `set pastetoggle=<F2>`\
or add the following to your `~/.vimrc` file:
``` {.code-box}
noremap <F2> :set invpaste paste?
set pastetoggle=<F2>
          
```

:set autowrite\
:set noautowrite
:set aw\
:set noaw
This tells vim to automatically write the file when switching to edit
another file. See tags, editing multiple files (next, rewind)
:set backspace=indent,eol,start\
:set backspace
:set bs=indent,eol,start\
:set bs
Allow backspacing over an indent, line break (end of line) or start of
an insert
:set backup=on\
:set backup=off
:set bk=on\
:set bk=off
Create backup file of file changes while editing.\
To automatically remove the backup file after the file being edited is
written, use the option `:set writebackup=on/off`\
File backup mode settings: `:set backupcopy=yes/no/auto`
:set cryptmethod=zip\
:set cryptmethod=blowfish
 
Set file encryption for file save of buffer contents.
-   zip: pkzip
-   blowfish: strong encryption

This is set upon reading a file if encrypted.\
Vim 7.3+
:set errorbells\
:set noerrorbells
:set eb\
:set noeb
Silence error beep
:set flash\
:set noflash
:set fl\
:set nofl
Screen flashes upon error (for deaf people or when noerrorbells is set)
:set tabstop=8
:set ts
Tab key displays 8 spaces
:set ignorecase\
:set noignorecase
:set ic\
:set noic
Case sensitive searches
:set number\
:set nonumber
:set nu\
:set nonu
Display line numbers
:set showmatch\
:set noshowmatch
no abbreviations
Cursor shows matching ")" and "}"
:set showmode\
:set noshowmode
no abbreviations
Editor mode is displayed on bottom of screen
:set showmatch\
:set noshowmatch
no abbreviations
Cursor shows matching ")" and "}"
:set syntax on\
:set syntax off
no abbreviations
Set syntax highlighting and color highlighting for a file type (eg XML,
HTML, C++, Java, etc). Also cursor shows matching ")" and "}"\
Also can set syntax highlighting explicitly: `:set syntax=html`\
Syntax definition files: `/usr/share/vim/vim73/syntax/`
:set taglength
:set tl
Default=0. Set significant characters
:set closepunct='".,;)\]}
\
% key shows matching symbol.\
Also see showmatch
:set linelimit=1048560
\
Maximum file size to edit
:set wrapscan\
:set nowrapscan
:set ws\
:set nows
Breaks line if too long
:set wrapmargin=0\
:set wrapmargin=8\
:set nowrapmargin
:set wm\
 \
:set nowm
Define right margin for line wrapping.\
Wrap when past 8 characters from the edge of column display (often
default 80).
:set list\
:set nolist
\
Display all Tabs and Ends of lines (Dislays these hidden characters).
:set bg=dark\
:set bg=light
\
VIM: choose color scheme for "dark" or "light" console background.
See full list of [set
options](http://vimdoc.sourceforge.net/htmldoc/options.html)

<div class="labelbar">

Advanced "vi" features:

</div>

### Interactive Command Examples:

-   **Marking a line:**\
    Any line can be "Book Marked" for a quick cursor return.
    -   Type the letter "**m**" and any other letter to identify
        the line.
    -   This "marked" line can be referenced by the keystroke sequence
        "**'**" and the identifying letter.\
        Example: "**mt**" will mark a line by the identifier "t".\
        "**'t"** will return the cursor to this line at any time.\
        A block of text may be referred to by its marked lines.
        i.e.**'t,'b**
    -   Write a marked block to a new file: **'t,'bw *newfile***
-   **vi line buffers:**\
    To capture lines into the buffer:

    -   Single line: "**yy**" - yanks a single line (defined by current
        cursor position) into the buffer
    -   Multiple lines: "**y't**" - yanks from current cursor position
        to the line marked "t"
    -   Multiple lines: "**3yy**" - yank 3 lines. Current line and two
        lines below it.

    Note all lines deleted are also stored in numbered line buffers.

    Copy an entry in the buffer to the editing session:

    -   "**p**" - place contents of latest entry to the buffer after
        current line defined by current cursor position. The buffer can
        be referenced by its number as well. The latest entry to the
        buffer is entry "1". Recall with the keystroke `"1p`
    -   Each deleted line will end up in the vim line buffer. To recall
        the prior entry to the buffer use the keystroke: `"2p`. The
        prior entries to the buffer can all be referenced by its number.
        Each time an entry to the buffer is made, its position in the
        stack is incremented. Typically vim has nine (1-9) default
        "numbered" buffers.
-   **vi named line buffers:**\
    Storage buffers can be named with letters of the alphabet: a-z.\
    To capture lines into the buffer:
    -   Single "yanked" line stored in buffer "a": **"ayy** - yanks a
        single line (defined by current cursor position) into the buffer
        named "a"
    -   Deleted line stored in buffer "b": **"bdd** - deletes a single
        line (defined by current cursor position) into the buffer named
        "a"
    -   Deletes 4 lines and stores in buffer "t": **"t4dd** - deletes
        four lines (defined by current cursor position) into the buffer
        named "a"

    \
    To paste lines from a named buffer:
    -   Single line stored in buffer "a": **"ap** - paste contents of
        the buffer named "a" after the current line (defined by current
        cursor position)
-   **vim: Shift a block of code left or right:**
    -   Enter into visual mode by typing the letter "v" at the top
        (or bottom) of the block of text to be shifted.
    -   Move the cursor to the bottom (or top) of the block of text
        using "j", "k" or the arrow keys.\
        Tip: Select from the first collumn of the top line and the last
        character of the line on the bottom line.\
        Zero ("0") will move the cursor to the first character of a line
        and "\$" will move the cursor to the last character of the line.
    -   Type &gt;&gt; to shift the block to the right.\
        Type &lt;&lt; to shift the block to the left.

    Note: The number of characters shifted is controlled by the "shift
    width" setting. i.e. 4: "`:set sw=4`"\
    This can be placed in your `$HOME/.vimrc` file.
-   **vim: Shift a block of code left or right (method \#2):**
    -   **:20,40&gt;**\
        Shift text from row 20 to 30, to the right
    -   **:20,40&lt;**\
        Shift text from row 20 to 30, to the left

### Command Line Examples:

-   **command options:**\
    The vi command line interface is available by typing "**:**".
    Terminate with a carriage return.\
    Example commands:
    -   **:help *topic***\
        If the exact name is unknown, TAB completion will cycle through
        the various options given the first few letters. Ctrl-d will
        print the complete list of possibilites.
-   **Executing Unix commands in vi:**\
    Any UNIX command can be executed from the vi command line by typing
    an "!" before the UNIX command.\
    Examples:
    -   **:!pwd** - shows your current working directory.
    -   **:!ls** - shows files in your current working directory.
    -   **:sh** - open a new Bash shell. Editing session is suspended
        until you exit the shell. Execute all the commands you want and
        then return to the vim session.
-   **Reading and merging/including external text:**
    -   **:r *filename*** - include the contents of an external file
    -   **:r !date** - reads the results from the date command into a
        new line following the cursor.
    -   **:r !ls -1** - Place after the cursor, the current directory
        listing displayed as a single column.
-   **Line numbers:**\
    Lines may be referenced by their line numbers. The last line in the
    file can be referenced by the "\$" sign.\
    The entire file may be referenced by the block "**1,\$**" or
    "**%**"\
    The current line is referred to as "**.**"\
    A block of text may be referred to by its line numbers or its
    marked lines. i.e. **5,38** or **'t,'b**\
    Write out a block of text denoted by line numbers **:5,38 w
    *newfile***\
    Append a marked block to an existing file: **'t,'bw &gt;&gt;
    *filename***
-   **Find/Replace:**\
    Example:
    -   **:%s/fff/rrrrr/** - For all lines in a file, find string "fff"
        and replace with string "rrrrr" for the first instance on
        a line.
    -   **:%s/fff/rrrrr/g** - For all lines in a file, find string "fff"
        and replace with string "rrrrr" for each instance on a line.
    -   **:%s/fff/rrrrr/gc** - For all lines in a file, find string
        "fff" and replace with string "rrrrr" for each instance on
        a line. Ask for confirmation
    -   **:%s/fff/rrrrr/gi** - For all lines in a file, find string
        "fff" and replace with string "rrrrr" for each instance on a
        line. Case insensitive.
    -   **:'a,'bs/fff/rrrrr/gi** - For all lines between line marked
        "a" (ma) and line marked "b" (mb), find string "fff" and replace
        with string "rrrrr" for each instance on a line.
        Case insensitive.
    -   **:5,20s/fff/rrrrr/gc** - For all lines between line 2 and line
        20, find string "fff" and replace with string "rrrrr" for each
        instance on a line. Confirm each change with y/n.
    -   **:1,\$s/\$/XXX/** - For all lines in the file, append a tripple
        X (XXX)
    -   **:1,\$s/XXX\$//** - For all lines in the file, remove the
        tripple X (XXX)
    -   **:%s/ \*\$/** - For all lines in a file, delete blank spaces at
        end of line (there is a single space before the asterisk).
        Repeat with a tab instead of a space to delete trailing tabs.
    -   **:%s/\\(.\*\\):\\(.\*\\)/\\2:\\1/g** - For all lines in a file,
        move last field delimited by ":" to the first field. Swap fields
        if only two.
    -   **:%s\#&lt;\[\^&gt;\]\\+&gt;\#\#g** - Find and remove all HTML
        tags but keep the text contents.
    -   **:%s/\^\\(.\*\\)\\n\\1\$/\\1/** - Find and remove all duplicate
        lines

    For more info type:
    -   **:help substitute**
    -   **:help pattern**
    -   **:help gdefault**
    -   **:help cmdline-ranges**
-   **Sorting:**\
    Example:
    -   Mark a block of text at the top line and bottom line of the
        block of text. i.e. "**mt**" and "**mb**" on two separate lines.
        This text block is then referenced as **"'t,'b**.
    -   Sort lines in block: (man page:
        [sort](http://man.yolinux.com/cgi-bin/man2html?cgi_command=sort))\
        **:'t,'b !sort**
    -   Reverse order of lines in block: (man page:
        [tac](http://man.yolinux.com/cgi-bin/man2html?cgi_command=tac))\
        **:'t,'b !tac**
    -   Sort lines of text in a paragraph. Block of lines defining the
        paragraph are identified by the cursor as the top and the first
        blank line as the end of the paragraph. Place curson on the line
        "Blue chair" and type the following:\
        **!}sort**\
        File to edit:

        ``` {.code-box}
        Blue chair
        Red table
        Green grass
        Black stone

        Other stuff goes here...
        and here
                      
        ```

        Becomes

        ``` {.code-box}
        Black stone
        Blue chair
        Green grass
        Red table

        Other stuff goes here...
        and here
                      
        ```

        Note that lines below the blank line delimeter are not sorted.

    -   Sort lines of text in a paragraph by the second collumn:\
        **!}sort -f -k2**\
        option "-f" : ignore case\
        option "-k" : list collumn number to sort by\
        For a list of all options, see the [sort man
        page](http://man.yolinux.com/cgi-bin/man2html?cgi_command=sort)\
        File in previous example becomes:

        ``` {.code-box}
        Blue chair
        Green grass
        Black stone
        Red table

        Other stuff goes here...
        and here
                      
        ```

    -   Sort lines of text in a paragraph and arrange into four
        collumns:\
        **!}sort | pr -4t**\
        option -4 : four collumns\
        option -t : omit page headers and trailer\
        [pr man
        page](http://man.yolinux.com/cgi-bin/man2html?cgi_command=pr)\
        File to edit:

        ``` {.code-box}
        Blue
        Red
        Green
        Black
        Yellow
        Orange
        White
        Brown

        Other stuff goes here...
        and here
                      
        ```

        Becomes

        ``` {.code-box}
        Black         Brown         Orange        White
        Blue          Green         Red           Yellow


        Other stuff goes here...
        and here
                      
        ```

        Note that lines below the blank line delimeter are not sorted.

-   **Moving columns, manipulating fields and awk:**\
    **:'t,. !awk '{print \$3 " " \$2 " " \$1}'** - This will reverse the
    order of the columns in the block of text. The block of text is
    defined here as from the line marked with the keystroke **"bt"** and
    the current line (**"."**). This text block is referenced as
    "**'t,.**" (man page:
    [awk](http://man.yolinux.com/cgi-bin/man2html?cgi_command=awk))

    ``` {.code-box}
                  aaa bbb ccc              ccc bbb aaa
                  xxx yyy zzz   becomes->  zzz yyy xxx
                  111 222 333              333 222 111
                  
    ```

-   **Source Code Formatting:** C++/Java
    -   Use vim visual text selection to mark the lines to format
        (beautify):
        -   eg. Whole file:
            -   Go to first line in file: `shift-v`
            -   Go to last line in file: `shift-g`
            -   Select the key equals: `=`

        This will align all braces and indentations. For the equivalent
        in emacs see the [YoLinux emacs
        tutorial](LinuxTutorialXemacs.html).
-   **Text Formatting:**

    -   Mark a block of text at the top line and bottom line of
        the block. i.e. "**mt**" and "**mb**" on two separate lines.
    -   Example: "**:'t,'b !nroff**"
    -   You can insert nroff commands i.e.:

        .ce 3

        Center the next three lines

        .fi

        Fill text - left and right justify (default)

        .nf

        No Fill

        .ls 2

        Double line spacing

        .sp

        Single line space

        .sv 1.0i

        Vertical space at top of page space

        .ns

        Turn off spacing mode

        .rs

        Restore spacing mode

        .ll 6.0i

        Line length = 6 inches

        .in 1.0i

        Indent one inch

        .ti 1.0i

        Temporarily one time only indent one inch

        .pl 8.0i

        Page length = 8 inches

        .bp

        Page break

        Example:

        ``` {.code-box}
        .fi
        .pl 2i
        .in 1.0i
        .ll 6.0i
        .ce
        Title to be centered
        .sp
        The following text bla bla bla bla bla bla bla bla bla bla 
        bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla 
        bla bla bla bla bla bla bla bla bla bla bla bla bla bla 
        bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla 
        bla bla bla bla bla
        ```

        Becomes:

        ``` {.code-box}
                                 Title to be centered

                  The following text bla bla bla bla bla bla bla bla
                  bla  bla  bla  bla bla bla bla bla bla bla bla bla
                  bla bla bla bla bla bla bla bla bla  bla  bla  bla
                  bla  bla  bla  bla bla bla bla bla bla bla bla bla
                  bla bla bla bla bla bla bla bla bla  bla  bla  bla
                  bla bla bla bla

        ```

    man pages:

    -   [nroff](http://man.yolinux.com/cgi-bin/man2html?cgi_command=nroff) -
        text formatter (emulate nroff command with groff)
    -   [troff](http://man.yolinux.com/cgi-bin/man2html?cgi_command=troff) -
        troff processor of the groff text formatting system
    -   [tbl](http://man.yolinux.com/cgi-bin/man2html?cgi_command=tbl) -
        table formatter (for troff)

-   **Text Width Formatting:**
    -   Mark a block of text or reference a block by their line numbers
        and pipe them through `fmt`, a text formatter which splits lines
        on word boundaries.
    -   **:20,30 !fmt -80** will re-format the lines from line 20 to
        line 30 to wrap at an 80 collumn margin. Any line longer than 80
        characters (eg a long URL), will not get split. A line split
        occurs at word delimiters such as a blank space.

    man page:
    [fmt](http://man.yolinux.com/cgi-bin/man2html?cgi_command=fmt)
-   **Spell Checking:**
    -   Mark a block of text by marking the top line and bottom line of
        the block. i.e. "**mt**" and "**mb**" on two separate lines.
    -   **:'t,'b !spell** will cause the block to be replaced with
        misspelled words.
    -   Press "**u**" to undo.
    -   Proceed to correct words misspelled.

    man page:
    [aspell](http://man.yolinux.com/cgi-bin/man2html?cgi_command=aspell)
-   **Vim/Vi Macros:** **:map letter commands\_strung\_together**\
    **:map** - lists current key mappings\
    Example - **:map g n cwNEW\_WORD{ctrl-v}{esc}i{ctrl-v}{CR}**\
    This example would find the next search occurrence, change the word
    and insert a line feed after the word. The macro is invoked by
    typing the letter "g".
    -   Control/Escape/Carriage control characters must be prefixed
        with ctrl-V.
    -   Choose a letter which is not used or important. (i.e. a poor
        choice would be "i" as this is used for insert)
-   **Double spacing:**
    -   **:%s/\$/{ctrl-V}{CR}/g**\
        This command applies an extra carriage return at the end of all
        lines
-   **Strip blanks at end of line:**
    -   **:%s/{TAB}\*\$//**
-   **Delete all lines beginning with or matching a pattern:**
    -   **:1,\$ /\^\#/d**\
        Delete all (first to last line: 1,\$ or g) comments lines
        in file. Delete all lines beginning (\^) with "\#" (specify
        text pattern).
    -   **:g/\#/d**\
        Delete all lines (g) containing comments (comments follow "\#")
        in file. Delete all lines containing "\#".
    -   **:g!/\^\#/d**\
        Delete all lines except (g! or v) comment lines beginning (\^)
        with "\#".
-   **Strip DOS ctrl-M's:**
    -   **:1,\$ s/{ctrl-V}{ctrl-M}//**\
        Note: In order to enter a control character, one muust first
        enter ctrl-v. This is true throughout vi. For example, if
        searching for a control character (i.e. ctrl-m):
        `/ctrl-v ctrl-M` If generating a macro and you need to enter esc
        without exiting the vi command line the esc must be prefixed
        with a ctrl-v: `ctrl-v esc`.
-   **Convert tabs to spaces:**
    -   **:% !expand -t4**\
        convert tabs to four blank spaces for the whole file (%).
    -   **:20,30 !expand -t4**\
        convert tabs to four blank spaces for lines 20 through 30.

    Man page:
    [expand](http://man.yolinux.com/cgi-bin/man2html?cgi_command=expand)
-   **Editing multiple files:**
    -   **vi file1 file2 file3**
    -   **:n** Edit next file (file2)
    -   **:n** Edit next file (file3)
    -   **:rewind** Rewind to the first file (file1)\
        or **shift-ctrl-\~**
    -   **:rewind!** Rewind to the first file (file1) without saving
        changes

    Note: Named buffers from "yanked" and deleted lines are shared
    between files. Contents of unamed buffers are not. To save file
    changes when switching files `:set autowrite`
-   **Line folding:**

    Many times one may encounter a file with folded lines or may wish to
    fold lines. The following image is of a file with folded lines where
    each "+" represents a set of lines not viewed but a marker line
    prefixed with a "+" is shown stating how many lines have been folded
    and out of view. Folding helps manage large files which are more
    easily managed when text lines are grouped into "folds".

    Example: `vim               /usr/share/vim/vim63/plugin/netrw.vim`

    ![VIM folded lines](images/vim-folded-lines.gif)

    Keystrokes:

      Keystroke   Description
      ----------- -------------------------------------------------------
      zR          Unfold all folded lines in file.
      za          Open/close (toggle) a folded group of lines.
      zA          Open a closed fold or close an open fold recursively.
      zc          Close a folded group of lines.
      zC          Close all folded lines recursively.
      zd          Delete a folded line.
      zD          Delete all folded lines recursively.
      zE          Eliminate all folded lines in file.
      zF          Create "N" folded lines.

-   **Hyper-Linking to include files:**

    -   Place cursor over the file name (i.e. `#include "fileABC.h"`)
    -   Enter the letter combination: **gf**\
        (go *to* file)

    This will load file `fileABC.h` into vim. Use the following entry in
    your `~/.vimrc` file to define file paths. Change path to something
    appropriate if necessary.

    ``` {.code-box}
    "Recursively set the path of the project.
    set path=$PWD/**
    ```

-   **Batch execution of vi from a command file:**\
    Command file to change HTML file to lower case and XHTML compliance:

    ``` {.code-box}
    :1,$ s/<HTML>/<html>/g
    :1,$ s/<\/HTML>/<\/html>/g
    :1,$ s/<HEAD>/<head>/g
    :1,$ s/<\/HEAD>/<\/head>/g
    :1,$ s/<TITLE>/<title>/g
    :1,$ s/<\/TITLE>/<\/title>/g
    :1,$ s/<BODY/<body/g
    :1,$ s/<\/BODY/<\/body/g
    :1,$ s/<UL>/<ul>/g
    :1,$ s/<\/UL>/<\/ul>/g
    ...
    ..
    .
    :1,$ s/<A HREF/<a href/g
    :1,$ s/<A NAME/<a name/g
    :1,$ s/<\/A>/<\/a>/g
    :1,$ s/<P>/<p>/g
    :1,$ s/<B>/<b>/g
    :1,$ s/<\/B>/<\/b>/g
    :1,$ s/<I>/<i>/g
    :1,$ s/<\/I>/<\/i>/g
    :wq
           
    ```

    Execute:
    `vi -e file-name.html <               ViCommands-HtmlUpdate.txt`

    \[Potential Pitfall\]: This must be performed while vim has none of
    the files open which are to be affected. If it does, vim will error
    due to conflicts with the vim swap file.

<div class="labelbar">

Tagging:

</div>

This functionality allows one to jump between files to locate
subroutines.

-   **ctags \*.h \*.c** This creates a file names "tags".

Edit the file using **vi**.

-   Unix command line: **`vi -t                   subroutine_name`**
    This will find the correct file to edit.\
    OR
-   Vi command line: **`:tag                 subroutine_name`** This
    will jump from your current file to the file containing the
    subroutine. (short form **`:ta subroutine_name`** )\
    OR
-   By cursor position: **ctrl-\]** Place cursor on the first character
    of the subroutine name and press **ctrl-\]** This will jump to the
    file containing the subroutine.\
    **Note:** The key combination `ctrl-]` is also the default telnet
    connection interrupt. To avoid this problem when using telnet block
    this telnet escape key by specifying NULL or a new escape key:
    -   `telnet -E file-name`
    -   `telnet -e "" file-name`

In all cases you will be entered into the correct file and the cursor
will be positioned at the subroutine desired.\
If it is not working properly look at the "tags" file created by
**ctags**. Also the tag name (first column) may be abbreviated for
convenience. One may shorten the significant characters using **:set
taglength=number**

Tag Notes:

-   A project may have a tags file which can be added and referred to
    by: **`:set tags=tags\             /ad/src/project1.tags`**\
    A "\\" must separate the file names.
-   **`:set autowrite`** will automatically save changes when jumping
    from file to file, otherwise you need to use the **:w** command.
-   Autowrite can be intentionally avoided by using "!" to avoid the
    save when switching files. Changes will be lost: **:ta! *next-tag***

**vim tagging notes:** (These specific tag features not available in vi)

+--------------------------------------+--------------------------------------+
| Tag Command                          | Description                          |
+======================================+======================================+
| `:tag start-of-tag-name_TAB`         | Vim supports tag name completion.    |
|                                      | Start the typing the tag name and    |
|                                      | then type the TAB key and name       |
|                                      | completion will complete the tag     |
|                                      | name for you.                        |
+--------------------------------------+--------------------------------------+
| `:tag /search-string`                | Jump to a tag name found by a        |
|                                      | search.                              |
+--------------------------------------+--------------------------------------+
| **`ctrl-]`**                         | The vim editor will jump into the    |
|                                      | tag to follow it to a new position   |
|                                      | in the file or to a new file.        |
+--------------------------------------+--------------------------------------+
| **`ctrl-t`**                         | The vim editor will allow the user   |
|                                      | to jump back a level.\               |
|                                      | (or `:pop`)                          |
+--------------------------------------+--------------------------------------+
| **`:tselect                 <functio | When multiple entries exist in the   |
| n-name>`**                           | tags file, such as a function        |
|                                      | declaration in a header file and a   |
|                                      | function definition (the function    |
|                                      | itself), the operator can choose by  |
|                                      | issuing this command. The user will  |
|                                      | be presented with all the references |
|                                      | to the function and the user will be |
|                                      | prompted to enter the number         |
|                                      | associated with the appropriate one. |
+--------------------------------------+--------------------------------------+
| **`:tnext`**                         | When multiple answers are available  |
|                                      | you can go to the next answer.       |
+--------------------------------------+--------------------------------------+
| `:set ignorecase`\                   | The ignore case directive affects    |
| (or `:set ic`)                       | tagging.                             |
+--------------------------------------+--------------------------------------+
| `:tags`                              | Show tag stack (history)             |
+--------------------------------------+--------------------------------------+
| `:4pop`                              | Jump to a particular position in the |
|                                      | tag stack (history).\                |
|                                      | (jump to the 4th from bottom of tag  |
|                                      | stack (history).\                    |
|                                      | The command "`:pop`" will move by    |
|                                      | default "1" backwards in the stack   |
|                                      | (history).)\                         |
|                                      | or\                                  |
|                                      | `:4tag`\                             |
|                                      | (jump to the 4th from top of tag     |
|                                      | stack)                               |
+--------------------------------------+--------------------------------------+
| `:tnext`                             | Jump to next matching tag.\          |
|                                      | (Also short form `:tn` and jump two  |
|                                      | `:2tnext`)                           |
+--------------------------------------+--------------------------------------+
| `:tprevious`                         | Jump to previous matching tag.\      |
|                                      | (Also short form `:tp` and jump two  |
|                                      | `:2tp`)                              |
+--------------------------------------+--------------------------------------+
| `:tfirst`                            | Jump to first matching tag.\         |
|                                      | (Also short form `:tf`, `:trewind`,  |
|                                      | `:tr`)                               |
+--------------------------------------+--------------------------------------+
| `:tlast`                             | Jump to last matching tag.\          |
|                                      | (Also short form `:tl`)              |
+--------------------------------------+--------------------------------------+
| ``` {.code}                          | Using multiple tag files (one in     |
| :set tags=./tags,./subdir/tags       | each directory).\                    |
| ```                                  | Allows one to specify all tags files |
|                                      | in directory tree:                   |
|                                      | `set tags=src/**/tags`\              |
|                                      | Use Makefile to generate tags files  |
|                                      | as well as compile in each           |
|                                      | directory.                           |
+--------------------------------------+--------------------------------------+

Links:

-   [Vim docs -
    ctags](http://vimdoc.sourceforge.net/htmldoc/usr_29.html)
-   Man page:
    [ctags](http://man.yolinux.com/cgi-bin/man2html?cgi_command=ctags)
-   [vim/tag search](http://vimdoc.sourceforge.net/htmldoc/tagsrch.html)
-   [ctags framework](http://www.softpanorama.org/Editors/ctags.shtml)

<div class="labelbar">

The ctags utility:

</div>

There are more than one version of ctags out there. The original Unix
version, the GNU version and the version that comes with vim. This
discussion is about the one that comes with vim. (default with Red Hat)

For use with C++:

-   ctags version 5.5.4:

    ``` {.code}
       ctags *.cpp ../inc/*.h

                  
    ```

-   ctags version 5.0.1:

    ``` {.code}
       ctags --lang=c++ --c-types=+Ccdefgmnpstuvx *.cpp ../inc/*.h
    ```

To generate a tags file for all files in all subdirectories:
`ctags -R .` [](){#EXRC}

The ctags program which is written by the VIM team is called " Exuberant
Ctags" and supports the most features in VIM.

Man page:
[ctags](http://man.yolinux.com/cgi-bin/man2html?cgi_command=ctags) -
Generate tag files for source code

<div class="labelbar">

Defaults file:

</div>

**VIM: `$HOME/.exrc`**

-   `~/.vimrc`
-   `~/.gvimrc`
-   `~/.vim/` (directory of vim config files.)

**VI: `$HOME/.exrc`**

Example:
``` {.code-box}
         set autoindent
         set wrapmargin=0
         map g hjlhjlhjlhlhjl
         "
         " S = save current vi buffer contents and run spell on it,
         "     putting list of misspelled words at the end of the vi buffer.
         map S G:w!^M:r!spell %^M
         colorscheme desert
         "Specify that a dark terminal background is being used.
         set bg=dark
        
```

Notes:

-   Look in `/usr/share/vim/vim61/colors/` for available colorschemes.\
    (I also like "colorscheme desert")
-   Alternate use of autoindent: `set ai             sw=3`

[](){#CSCOPE}

<div class="labelbar">

Using vim and cscope:

</div>

Cscope was developed to cross reference C source code. It now can be
used with C++ and Java and can interface with vim.

Using Cscope to cross reference souce code will create a database and
allow you to traverse the source to find calls to a function, occurances
of a function, variable, macros, class or object and their respective
declarations. Cscope offers more complete navigation than ctags as it
has more complete cross referencing.

Vim must be compiled with Cscope support. Red Hat Enterprise Linux 5 (or
CentOS 5), includes vim 7.0 with cscope support. Earlier versions of Red
Hat or Fedora RPM does not support Cscope and thus must be compiled.

#### Compiling Vim from source:

-   Download vim source from [http://vim.org](http://www.vim.org)
-   `tar xzf vim-7.0.tar.gz`
-   `cd vim70`
-   `./configure --prefix=/opt --enable-cscope`
-   `make`
-   `make install`

#### Using Cscope with vim:

The Cscope database (`cscope.out`) is generated the first time it is
invoked. Subsequent use will update the database based on file changes.\
The database can be generated manually using the command i.e.:
`cscope -b *.cpp *.h` or `cscope -b -R           .`
Invoke Cscope from within vim from the vim command line. Type the
following: `:cscope find search-type           search-string` The short
form of the command is ":cs f" where the "search-type" is:

  Search Type   Type short form   Description
  ------------- ----------------- --------------------------------------------------
  symbol        s                 Find all references to a symbol
  global        g                 Find global definition
  calls         c                 Find calls of this function
  called        d                 Find functions that the specified function calls
  text          t                 Find specified text string
  file          f                 Open file
  include       i                 Find files that "\#include" the specified file

Results of the Cscope query will be displayed at the bottom of the vim
screen.

-   To jump to a result type the results number (+ enter)
-   Use tags commands to return after a jump to a result: `ctrl-t`\
    To return to same spot as departure, use `ctrl-o`
-   To use "tags" navigation to search for words under the cursor
    (ctrl-\\ or ctrl-\]) instead of using the vim command line
    "`:cscope`" (and "ctrl-spaceBar" instead of "`:scscope`"), use the
    vim plugin, `cscope_maps.vim` \[[cache](src/cscope_maps.vim)\]\
    When using this plugin, overlapping ctags navigation will not
    be available. This should not be a problem since cscope plugin
    navigation is the same but with superior indexing and cross
    referenceing.\
    Place this plugin in your directory "`$HOME/.vim/plugin`"\
    Plugin required for vim 5 and 6. This feature is compiled in with
    vim 7.0 on Red Hat Enterprise Linux 5 and CentOS 5 and newer
    Linux OS's. Attempts to use the plugin when not required will result
    in the following error:

    `E568: duplicate cscope database not added`

-   Cycle through results:
    -   Next result: `:tnext`
    -   Previous result: `:tprevious`
-   Create a split screen for Cscope results:
    `:scscope find search-type             search-string`\
    (Short form: `:scs f search-type             search-string`)
-   Use command line argument "`:cscope -R`": Scan subdirectories
    recursively
-   Use Cscope ncurses based GUI without vim: `cscope`
    -   ctrl-d: Exit Cscope GUI

#### Cscope command line arguments:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------
  Argument                  Description
  ------------------------- ---------------------------------------------------------------------------------------------------------------------------------
  -R                        Scan subdirectories recursively

  -b                        Build the cross-reference only.

  -C                        Ignore letter case when searching.

  -f`FileName`              Specify Cscope database file name instead of default "cscope.out".

  -I*include-directories*   Look in "include-directories" for any \#include files whose names do not begin with "/".

  -i*Files*                 Scan specified files listed in "Files". File names are separated by linefeed. Cscope uses the default file name "cscope.files".

  -k                        Kernel mode ignores `/usr/include`.\
                            Typical: `cscope -b -q -k`

  -q                        create inverted index database for quick search for large projects.

  -s*DirectoryName*         Use specified directory for source code. Ignored if specified by "-i".

  -u                        Unconditionally build a new cross-reference file..

  -v                        Verbose mode.

  *file1 file2 ...*         List files to cross reference on the command line.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------

#### Cscope environment variable:

  Environment Variable   Description
  ---------------------- -----------------------------------------------------------------------------------------------------------
  CSCOPE\_EDITOR         Editor to use: `/usr/bin/vim`
  EDITOR                 Default: `/usr/bin/vim`
  INCLUDEDIRS            Colon-separated list of directories to search for \#include files.
  SOURCEDIRS             Colon-separated list of directories to search for additional source files.
  VPATH                  Colon-separated list of directories to search. If not set, cscope searches only in the current directory.

------------------------------------------------------------------------

Manually Generating file `cscope.files`

File: `$HOME/bin/gen_cscope` or `/opt/bin/gen_cscope`

``` {.code-box}
#!/bin/bash
find ./ -name "*.[ch]pp" -print > cscope.files
cscope -b -q -k
```

Generates `cscope.files` of ".cpp" and ".hpp" source files for a C++
project.
Note that this generates CScope files in the current working directory.
The CScope files are only usefull if you begin the vim session in the
same directory. Thus if you have a heirarchy of directories, perform
this in the top directory and reference the files to be edited on the
command line with the relative path from the same directory in which the
CScope files were generated.

------------------------------------------------------------------------

Also see:

-   [cscope man
    page](http://man.yolinux.com/cgi-bin/man2html?cgi_command=cscope)
-   [cscope home page](http://cscope.sourceforge.net)
-   [Using cscope with Linux kernel source
    code](http://cscope.sourceforge.net/large_projects.html)

[](){#PLUGINS}

<div class="labelbar">

Vim plugins:

</div>

**Vim default plugins:**

Vim comes with some default plugins which can be found in:

-   Red Hat / CentOS / Fedora:
    -   RHEL4/5: `/usr/share/vim/vim70/autoload/`
    -   Fedora 3:`/usr/share/vim/vim63/plugin/`
-   Ubuntu / Debian:
    -   Ubuntu 6.06: `/usr/share/vim/vim64/plugin/`

**Additional custom plugins:**

User added plugins are added to the user's local directory:
`~/.vim/plugin/` or `~/.vimrc/plugin/`

-   Vim.org: [List of all
    plugins](http://www.vim.org/scripts/script_search_results.php?order_by=creation_date&direction=descending)

<div class="labelbar2">

Default vim plugins:

</div>

#### File Explorer / List Files: `explorer.vim`

Help is available with the following command: `:help file-explorer`

  Command                     Description
  --------------------------- ----------------------------------------------------------------------------------
  :Explore                    List files in your current directory
  :Explore *directory-name*   List files in specified directory
  :Vexplore                   Split with a new vertical window and then list files in your current directory
  :Sexplore                   Split with a new horizontal window and then list files in your current directory

The new window buffer created by ":Vexplore" and ":Sexplore" can be
closed with ":bd" (buffer delete).

<div class="labelbar2">

Additional custom plugins:

</div>

#### CScope: `cscope_maps.vim`

See cscope and vim description and use [in this tutorial
above](#CSCOPE).

------------------------------------------------------------------------

#### Tabbed pages: `minibufexpl.vim`

This plugin allows you to open multiple text files and accessed by their
tabs displayed at the top of the frame.
  Keystroke                Description
  ------------------------ -------------------------------------------------------------------------------------------------
  :bn                      New buffer
  :bd                      Buffer delete
  :b3                      Go to buffer number 3
  ctrl-w followed by "k"   New buffer. Puts curson in upper tabbed portion of window. Navigate with arrow keys or "h"/"l".
  :qa                      Quit vim out of all buffers
  tab                      The "tab" key jumps between tabbed buffers.

Recommended `~/.vimrc` file entry:

``` {.code-box}
"Hide abandon buffers in order to not lose undo history.
set hid
```

This vim directive will allow undo history to remain when switching
buffers.
The new window buffer tab created can be closed with ":bd" (buffer
delete).

Links:

-   [minibufexpl plugin home
    page](http://www.vim.org/scripts/script.php?script_id=159)

------------------------------------------------------------------------

#### Alternate between the commensurate include and source file: `a.vim`

Most usefull when used with the vim plugin "minibufexpl.vim"
Usefull for C/C++ programmers to switch between the source ".cpp" and
commensurate ".hpp" or ".h" file and vice versa.

  Command   Description
  --------- --------------------------------------------------------------------------------------------
  :A        switches to the header file corresponding to the current file being edited (or vise versa)
  :AS       splits and switches
  :AV       vertical splits and switches
  :AT       new tab and switches
  :AN       cycles through matches
  :IH       switches to file under cursor
  :IHS      splits and switches
  :IHV      vertical splits and switches
  :IHT      new tab and switches
  :IHN      cycles through matches

If you are editing `fileX.c` and you enter ":A" in vim, you will be
switched to the file `fileX.h`
Links:

-   [a.vim plugin home
    page](http://www.vim.org/scripts/script.php?script_id=31)

------------------------------------------------------------------------

#### Plug-in Installation:

Example of installation of `a.vim` and `minibufexpl.vim` plug-ins:
-   `mkdir -p ~/.vim/plugin`
-   `cd ~/.vim/plugin`
-   `wget -O a.vim http://www.vim.org/scripts/download_script.php?src_id=7218`
-   `wget -O minibufexpl.vim http://www.vim.org/scripts/download_script.php?src_id=3640`

Note that the URL of the plug-in can be found from the home page of the
plug-in.

<div class="labelbar">

Vim tip:

</div>

Using a mousewheel with vim in an xterm. Place in file
`$HOME/.Xdefaults`

``` {.code-box}
XTerm*VT100.Translations: #override \n\ 
: string("0x9b") string("[64~") \n\ 
: string("0x9b") string("[65~")
```

<div class="labelbar">

Vim Variants and Other Similar Tools:

</div>

-   [ed](http://man.yolinux.com/cgi-bin/man2html?cgi_command=ed) - line
    editor (works on one file at a time)
-   [red](http://man.yolinux.com/cgi-bin/man2html?cgi_command=red) -
    restricted shell version of ed
-   [tr](http://man.yolinux.com/cgi-bin/man2html?cgi_command=tr) -
    translate or delete characters
-   [ex](http://man.yolinux.com/cgi-bin/man2html?cgi_command=ex) - line
    oriented version of vi. Works on multiple files.
-   [sed](http://man.yolinux.com/cgi-bin/man2html?cgi_command=sed) -
    stream editor
-   view - read only version of vi
-   rview - restricted view
-   gvim - GUI version of VIM
-   rvim - restricted vim

<div class="labelbar">

Links:

</div>

-   [**Linux Text Editors**](LinuxTextEditors.html) - overview and list
-   [The vim home page](http://www.vim.org)
-   [Fast vi tutorial](http://www.jerrywang.net/vi/)
-   [Troubleshooters.com: VI and
    VIM](http://www.troubleshooters.com/lpm/200212/200212.htm)
-   [Vim as an XML/XHTML editor](http://www.pinkjuice.com/howto/vimxml/)

<div class="labelbar-h2">

![vim books](images/book40.gif) Books:

</div>

  ----------------------------------------------------- ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![ultimate guide to vi](../BOOKS/1503721.gif)         "The Ultimate Guide to VI and EX Text Editors"\                                      [![Amazon.com](images/Amazon-BuyABook88x31.gif)](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http://www.amazon.com/exec/obidos/ASIN/0805344608/&tag=yolinux-20)\
                                                        Hewlet Packard Corporation\                                                          
                                                        ISBN \#0-8053-4460-8, Addison-Wesley Pub Co., Benjamin/Cummings Publishing Company   

  ![Learn vi](../BOOKS/059652983X.jpg)                  "Learning the vi and vim Editors (7th edition)\                                      [![Amazon.com](images/Amazon-BuyABook88x31.gif)](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http://www.amazon.com/exec/obidos/ASIN/059652983X/&tag=yolinux-20)\
                                                        by Arnold Robbins, Elbert Hannah, Linda Lamb\                                        
                                                        ISBN \#059652983X, O'Reilly                                                          

  ![vi improved](../BOOKS/0735710015.01.MZZZZZZZ.jpg)   "Vi iMproved (VIM)\                                                                  [![Amazon.com](images/Amazon-BuyABook88x31.gif)](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http://www.amazon.com/exec/obidos/ASIN/0735710015/&tag=yolinux-20)\
                                                        by Steve Oualline\                                                                   
                                                        ISBN \#0735710015, Sams (1st edition)                                                
  ----------------------------------------------------- ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<div class="lineHR">

<div id="disqus_thread">

</div>

Please enable JavaScript to view the [comments powered by
Disqus.](https://disqus.com/?ref_noscript)

</div>

</div>

<div id="rightcol">

<div id="bookmark">

   \
[![Bookmark and
Share](http://s7.addthis.com/static/btn/lg-bookmark-en.gif){width="125"
height="16"}](http://www.addthis.com/bookmark.php?v=250&pub=yolinux)

</div>

Advertisements

<div align="center">

[![](images/LinuxPlusMagazine.gif)](http://www.lpmagazine.org)

</div>

 

</div>

</div>

<div class="row">

<div id="yo-footer">

<div class="col-sm-4">

**[YoLinux.com Home Page](http://www.yolinux.com){.footer}\
[YoLinux Tutorial Index](http://www.yolinux.com/TUTORIALS/){.footer} |
[Terms](http://www.yolinux.com/YoLinux-Terms.html){.footer}\
[Privacy Policy](http://www.yolinux.com/privacy.html){.footer} |
[Advertise with
us](http://www.yolinux.com/YoLinux-Advertising.html){.footer} |
[Feedback Form](http://www.yolinux.com/YoLinuxEmailForm.html){.footer}
|**\
Unauthorized copying or redistribution prohibited.

</div>

<div class="col-sm-4">

+--------------------------------------+--------------------------------------+
|                                      | [![Bookmark and                      |
|                                      | Share](http://s7.addthis.com/static/ |
|                                      | btn/lg-bookmark-en.gif){width="125"  |
|                                      | height="16"}](http://www.addthis.com |
|                                      | /bookmark.php?v=250&pub=yolinux)     |
+--------------------------------------+--------------------------------------+

</div>

<div class="col-sm-4">

<div align="right">

[to top of page](#TOP){.footer}\

</div>

</div>

</div>

</div>

<div id="copyright">

Copyright © 1999 - 2018 by *Greg Ippolito*

</div>

![vi power](images/vipower.gif)

</div>

<div style="display: none;">

![Quantcast](//pixel.quantserve.com/pixel/p-ebIBcaVUngFBQ.gif){width="1"
height="1"}

</div>
