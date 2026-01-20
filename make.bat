@echo off
if "%1" == "" goto help

if "%1" == "install" goto install
if "%1" == "lint" goto lint
if "%1" == "format" goto format
if "%1" == "test" goto test
if "%1" == "build" goto build

:help
echo Usage: make.bat [install|lint|format|test|build]
goto end

:install
pip install -r requirements.txt
pip install -r requirements-dev.txt
goto end

:lint
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
goto end

:format
black .
goto end

:test
pytest
goto end

:build
docker build -t wine-quality-api .
goto end

:end
