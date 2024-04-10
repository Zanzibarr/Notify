# Notify test cases

Here are listed all test cases I can think of about this software.  
If you find something not going accordingly or have suggestion on how to improve some output or feature, please contact me here <a target="_blank" href="https://www.zanzi.dev/contacts/">www.zanzi.dev/contacts/</a> or open an issue on <a target="_blank" href="https://github.com/Zanzibarr/Notify/issues">GitHub</a>.  

Please follow the format showed [here](test_report_format.md) to fill reports about tests.  

You can also try something that's not listed here to see if any edge case has been handled (for example adding random text or parameters to see what happens).  

Currently it's not supposed to work on Windows, so test those commands on Linux/MacOS.

## Index
- [Installation](#installation)
- [Command Line](#command-line)
- [Python lib](#python-library)

## Installation

Follow all steps in the guide (<a target="_blank" href="https://github.com/Zanzibarr/Notify/blob/main/readme.md">here</a>).  
Expected: successfull installation
- Get working bots
- Try to exit the installation process both and see if files have been created / bot works
- Check for the configuration file to be created correctly

## Command line

```shell
notify -help
```
Expected: print the help message
- check for correct (up-to-date) version
- check for correct installation folders and correct configuration file location
- check for correct links

#

```shell
notify -help <parameters>
```
\<parameters> are **supposed** to be the sending options (in the help message are called *notify commands*)  
Expected: Help message for that sending parameter
- test those parameters:
    - -t
    - -p
    - -a
    - -d
    - -v
    - -exc
- try some other words or commands and see what happens

#

```shell
notify -version
```
Expected: print the version of the isntalled version of the notify

#

```shell
notify -update
```
Expected: up-to-date (if notify is already at the latest version) or a prompt asking for confirmation with new version
- check wether the update is successful:
    - check the version
    - check if the files in the base path are updated

#

```shell
notify -update -dev
```
Expected: a prompt asking for confirmation with new version no matter what version you have
- check wether the update is successful:
    - check the version
    - check if the files in the base path are updated

#

```shell
notify -conf
```
Expected: print the location of the configuration file

#

```shell
notify -conf -add <profile_name> -token <token> <other_parameters>
```
Expected: add to the configuration file a new profile
- If the name was already assigned to a profile, that profile is overwritten
- See the help method to see which parameters can be added
- Test some illegal parameters and see what happens

#

```shell
notify -conf -edit <profile_name> <other_parameters>
```
Expected: edit the specified profile in the configuration file  
- Check for existent or non-existent profiles
- Check with invalid token or parameters

#

```shell
notify -conf -rm <profile_name>
```
Expected: remove the profile specified in the configuration file
- Check for existent or non-existent profiles

#

```shell
notify -conf -set <profile_name>
```
Expected: change the default profile
- check wether the default profile has been changed in the configuration file
- check wether the messages are sent from the right bot
- try with profiles that are non-existent

#

```shell
notify -conf -see
```
Expected: prints the configuration file's content

#

```shell
notify -uninstall
```
Expected: uninstall notify (not the configuration file)
- check for the base path
- check the .bashrc / .zshrc files

#

```shell
notify -prof <profile_name> <other_parameters>
```
Expected: See the help function to see how to use this command
- try not specifying any send option
- try specifying some illegal parameters
- Test sending messages with non-alphanumerical characters

#

Try some of the shortcuts (view the end of the help output).  
Expected: shortcut working as the normal parameter

#

Try combinations of varius parameters of commands to test precedence or error messages.  

#

Try sending messages adding options that are not supposed to be used with that sending option.  


## Python library

Test the various features listed in the <a target="_blank" href="https://github.com/Zanzibarr/Notify/blob/main/docs/python_use.md">python_use</a> file.  
- Try adding illegal values (especially the token or profile name)
- Try not specifying the default parameters
- Check the precedence of token / profile where it's possible to specify both (es load_pofile(...))
- Test the utilities (exception and progress bar)
- Test sending messages with non-alphanumerical characters
- Test the parse_mode (MarkdownV2, ...)