@ECHO OFF
ECHO Setting up links in git-hooks folder

mklink "%~dp0..\.git\hooks\pre-commit" "%~dp0pre-commit"