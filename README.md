# phwcookiecutter 

This is a template repo for Python based projects in PHW. 

# Quickstart - set up a repo using this template

- [install the cookiecutter package](https://cookiecutter.readthedocs.io/en/stable/README.html#installation). Note it is usual to work in a virtual environment when installing Python packages.
- In your Command Prompt/Terminal, navigate to the folder where you want to create your project and run `python -m cookiecutter https://{YOUR_PERSONAL_ACCESS_TOKEN}@github.com/Public-Health-Wales/phwcookiecutter.git`
- Enter the details requested.
- Navigate to the newly created repository.
- Run `git init` to initialise it as a git repo. 
- Install tools to support the install: `python -m pip install -U pip setuptools`. Again, note it is usual to work in a virtual environment when installing Python packages.
- Install an editable version of the package: `python -m pip install -e .`. Editable means that it will change as you make updates to the code.  Again, note it is usual to work in a virtual environment when installing Python packages.
- Install the pre-commit hooks: `pre-commit install`. Sometimes there can be errors in this step - to follow up.
- Commit the repo set up. Note that if the pre-commit hooks have been set up, linting may reveal some issues which the hooks auto-correct. You may therefore need to stage any automatically made changes and try the commit a second time. 
- Push to GitHub (create a new repo on GitHub and follow the instructions to push an existing repo).
- Set up branch protection so contributors cannot push directly to the `main` branch. Find this option in repo settings on GitHub.
- Follow the instructions in CONTRIBUTING.md to continue developing. 
  
# What does this do? 

- Sets up a repo with:
  - Standard README 
  - MIT License (Public Health Wales copyright)
  - Standard CONTRIBUTING instructions
  - Suitable folder structure: 
    - src folder containing package. In general, final project code or pipelines should be stored here. 
    - tests folder for tests
    - Folders currently contain examples (which should be removed).
  - pyproject.toml as required to make into a versioned, installable package
  - A standard .gitignore file
  - Setup for precommit hooks covering running tests, linting, basic security checks
  - Issue and pull request templates for use on GitHub 
  - A GitHub Action for linting and testing
  - Version and release management using `bump2version`
  