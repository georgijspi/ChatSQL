# Makefile

# Define the shell used by Makefile (default is /bin/sh)
SHELL := /bin/bash

# Define the Python interpreter. It's good practice to specify python3 explicitly.
PYTHON := python3

# Define the virtual environment directory
VENV_DIR := env

# Default target executed when no arguments are given to make.
default: setup

# Setup the Python Development Environment
setup: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: requirements.txt
	@test -d $(VENV_DIR) || $(PYTHON) -m venv $(VENV_DIR)
	@source $(VENV_DIR)/bin/activate; pip install -r requirements.txt
	@echo "Virtual environment created and packages installed."

# Cleanup virtual environment
clean:
	@rm -rf $(VENV_DIR)
	@echo "Virtual environment removed."

# This target is used to execute commands within the virtual environment.
# Usage: make run command="<command>"
run:
	@source $(VENV_DIR)/bin/activate; $(command)

.PHONY: default setup clean run
