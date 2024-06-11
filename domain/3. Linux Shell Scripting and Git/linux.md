# 1.0 Linux Basics and Command Line

## 1.1 Introduction to Linux

- Linux History and Philosophy
- Origins of Linux, GNU/Linux
- Open Source Movement
- Popular Linux Distributions
- Overview of Ubuntu, Fedora, CentOS
- Understanding Desktop Environments
  - GNOME, KDE, XFCE

## 1.2 Command Line Basics

- Terminal Fundamentals
- Accessing the Terminal
- Basic Navigation Commands
  - `cd`, `ls`, `pwd`
- Directory Structures
  - Home, Root, Bin, and Other Directories
- Absolute vs Relative Paths
- File Management Commands
  - `touch`, `mkdir`, `cp`, `mv`, `rm`

## 1.3 Working with Files and Text Editors

- File Operations
  - Copying: `cp source_file destination_directory`
  - Moving: `mv source_file destination`
  - Removing: `rm file`
- Searching Within Files with `grep`
  - `grep pattern filename`
- Introduction to Nano and Vim
- Basic Operations:
  - Nano: `nano filename`
  - Vim: `vim filename`
- Vim Modes and Navigation
  - Normal mode, Insert mode, Command mode
  - Navigation: `h`, `j`, `k`, `l`, `gg`, `G`, etc.

## 1.4 Basic File System Structure and Permissions

- Exploring Linux File System Hierarchy
  - `ls /`, `ls /home`, etc.
- Standard Directories and Their Roles
- File Permissions and Ownership
  - `ls -l filename`
  - `chmod permissions filename`
  - `chown user:group filename`
- Reading and Modifying File Permissions

## 1.5 Remote System Access

- Accessing remote system using SSH
  - `ssh username@hostname`
- Copy Files from/to remote System
  - `scp local_file username@hostname:/remote/path`
  - `scp username@hostname:/remote/file local_path`
