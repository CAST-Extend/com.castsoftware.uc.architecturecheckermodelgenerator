@echo off
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
REM configure python path if not defined
REM min version to use is Python 3.4
SET PYTHON_PATH_IF_NOT_DEF_IN_ENV=C:\Program Files\CAST\8.3\ThirdParty\Python34
IF "%PYTHONPATH%"=="" SET PYTHONPATH=%PYTHON_PATH_IF_NOT_DEF_IN_ENV%
"%PYTHONPATH%\python" -V
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
REM install the additional python lib required
REM no additional lib requires here 
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

SET SCRIPT_NAME=simple_model.py
SET CMD_OUTPUTFOLDER=-of "C:\Users\mmr\workspace\com.castsoftware.uc.architecturecheckermodelgenerator"

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
ECHO Running the command line 
SET CMD="%PYTHONPATH%\python" "%~dp0%SCRIPT_NAME%" %CMD_OUTPUTFOLDER%
ECHO %CMD%
%CMD%
SET RETURNCODE=%ERRORLEVEL%
ECHO RETURNCODE %RETURNCODE% 

PAUSE