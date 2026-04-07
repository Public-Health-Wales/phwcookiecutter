# phwcookiecutter 

This is a template repo for Python based projects in PHW. 

- To set up a repo using the template, see [Quickstart](#quickstart---set-up-a-repo-using-this-template).
- To find out what the template contains, see [What does this do?](#what-does-this-do)
- To develop your own cookiecutter based on this one, [fork this repo](https://github.com/Public-Health-Wales/phwcookiecutter/fork).
- To suggest changes or fixes to this cookiecutter, [add an issue](https://github.com/Public-Health-Wales/phwcookiecutter/issues) or [contact the maintainers](mailto:phw.dkrdatascience@wales.nhs.uk). 

# Quickstart - set up a repo using this template

**This is a template repo which can be used in conjunction with the cookiecutter package to set up a repo which looks like the template.** Running the cookiecutter command will directly use the version of this repo from GitHub, so you don't need to clone this repo unless you want to add to the template. 

- Many of these steps will involve installing Python packages. It is usual to work in a virtual environment when installing Python packages (e.g. conda/pip). Set up an environment to work in as you usually would.
- [Install the cookiecutter package](https://cookiecutter.readthedocs.io/en/stable/README.html#installation): `python -m pip install --user cookiecutter`.
- In your Command Prompt/Terminal, navigate to the folder where you want to create your project and run `python -m cookiecutter https://github.com/Public-Health-Wales/phwcookiecutter.git`. If you are asked about whether it is okay to delete and re-download the cookiecutter, say yes. 
- Enter the details requested to set up the repo.
- Navigate to the newly created repository.
- Run `git init` to initialise it as a git repo. 
- Install tools to support the install: `python -m pip install -U pip setuptools`. 
- Install an editable version of the package: `python -m pip install -e .`. Editable means that it will change as you make updates to the code.  Again, note it is usual to work in a virtual environment when installing Python packages.
- Install the pre-commit hooks: `python -m pre_commit install`. This step can be a bit fussy with respect to how things are installed and set up - please report any problems.
- Add any strings you want to check commits for to `.nocommitstrings` (one line per string, no quotation marks). Take care not to commit this file (it is covered by the `.gitignore`). Note pre-commit hooks can be turned off or not run so (as with the secret detection pre-commit hook), this is an extra layer of safety rather than something that should be relied on in itself to prevent secrets being committed.
- Complete the CODEOWNERS file following example format within the template.
- `git add` ("stage") the repo set up. We like to do this manually in VS Code so that you can see the files you're adding and be doubly sure you don't commit anything you don't mean to.
- `git commit` all the changes you have added. We like to do this from Command Prompt/Terminal, so that you can see any messages about the tests passing or failing. Note that if the pre-commit hooks have been set up, linting may reveal some issues which the hooks auto-correct. If any of the pre-commit hooks fail, you have not made a commit, and so you will need to stage any automatically made changes and try the commit a second time. 
- Push to GitHub (create a new repo on GitHub and follow the instructions to push an existing repo).
- Set up branch protection so contributors cannot push directly to the `main` branch. Find this option in repo settings on GitHub.
- Add your collaborators to the repo with an appropriate level of access. Find this option in repo settings on GitHub. 
- Follow the instructions in CONTRIBUTING_en.md to continue developing. 
  
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
  - An empty config.ini file. This should not be committed or pushed (and is in the .gitignore). Use this for aspects of config such as file paths. The config file should live in the root directory to avoid confusion with multiple versions. 
  - Setup for precommit hooks covering running tests, linting, basic security checks
  - Issue and pull request templates for use on GitHub 
  - A GitHub Action for linting and testing
  - Version and release management using `bump-my-version`
