# Instant Repo 🍜

> Choose a self-explaining name for your project.

## Description

> Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of **Features** or a **Background** subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

This is a template repository that can be used/forked to easily create new projects from a well-established starting basis. It includes best practices that I have come across, including

- dependency management via [Poetry](https://python-poetry.org/docs/)
- pre-commit hooks for formatters & linters via [Ruff](https://docs.astral.sh/ruff/) and `mypy`
- [semantic versioning](https://semver.org/), [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) & automated [Changelog](https://keepachangelog.com/en/1.1.0/) releases via `commitizen`
- automated documenation via `mkdocs`, following the [Diátaxis documentation framework](https://diataxis.fr/)
- a proper project structure / skeleton with dedicated folders for various different files:

```
.
├── .github                 # GitHub Actions workflows (CICD)
├── config                  # Configuration files
├── docs                    # Documentation files
├── logs                    # Log files
├── scripts                 # Shell scripts for local use or the CICD
│   ├── cicd                   # CICD scripts
│   └── local                  # local scripts (e.g. build/run api, ui, ...)
├── services                # Files for additional services such as a DB / API
├── src                     # Source files
│   └── instant_repo
│       └── commons               # Shared utility files
├── tests                   # Automated tests
│   ├── acceptance             # Acceptance tests
│   ├── integration            # Integration tests
│   └── unit                   # Unit tests
```

- a proper [README.md](README.md), following <https://www.makeareadme.com/>
- a proper logging setup for dev & prod environments, both in the terminal and exported into log files
- a proper CICD skeleton via GitHub Actions with `qa`, `bump` and `deploy` jobs
- a proper testing suite, with automated uploads to the free Teamscale alternative [Codecov](https://about.codecov.io/)
- an [MIT License](https://opensource.org/license/mit)

Note that some directories of the above described project structure only contain a placeholder `.gitkeep` file.

Finally, while there exist tools for creating project templates such as [copier](https://copier.readthedocs.io/en/stable/) or [backstage](https://backstage.io/), I feel that creating a personalized one from scratch is a very rewarding learning process, and I can only recommend you to do the same.

## Badges

> On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use [Shields](https://shields.io/) to add some to your README. Many services also have instructions for adding a badge.

## Visuals

> Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like [ttygif](https://github.com/icholy/ttygif) can help, but check out [Asciinema](https://asciinema.org/) for a more sophisticated method.

## Installation

> Within a particular ecosystem, there may be a common way of installing things, such as using [Yarn](https://yarnpkg.com/), [NuGet](https://www.nuget.org/), or [Homebrew](https://brew.sh/). However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

This project template is meant to be forked into its very own pet project repository, or used directly as a template repository. Once a new pet project has been created from this template, follow these steps to start from a fresh state:

### Setup GitHub Actions & Protect main branch

If not already done, in your GitHub Developer Settings, create a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-token) named `GITHUB_ACTIONS`, set its expiration to `No expiration`, and select `repo` as scope. Make sure to copy the token to your clipboard before moving on.

Add your copied `GITHUB_ACTIONS` token to the new repo via Settings > Secrets and variables > Actions > New repository secret, and name it `PERSONAL_ACCESS_TOKEN`.

Optionally, you can protect the `main` branch of this project such that PRs are necessary to push changes into changes into it, via repo Settings > Branches > Branch protection rules > Protect matching branches > Require a pull request before merging.

### Setup Codecov

Log into Codecov with your GitHub account and click on `Configure` next to the newly created repo to create a `CODECOV_TOKEN`. As before, make sure to copy this token to your clipboard and head back to GitHub.

Add your copied `CODECOV_TOKEN` to the new repo via Settings > Secrets and variables > Actions > New repository secret, and name it `CODECOV_TOKEN`.

### Setup GitHub pages

The documentation is hosted via GitHub pages through the `.github/workflows/ci.yaml`. This has to be initialized in the repo Settings > Pages > Build and deployment > Source > Deploy from a branch, > Branch > gh-pages > / (root) > Save

### Reset project versions

- delete the `CHANGELOG.md` (with the first push, it will be created anew)
- in the `pyproject.toml`, change up the `[tool.poetry]` section according to your liking, esp. regarding the `name` and `description` of the new project
- still within the `pyproject.toml`, reset the `[tool.poetry]/version` and `[tool.commitizen]/version` back to `0.1.0`, and remove the `__instant_repo_version` version file
- in `src/instant_repo/__init__.py`, reset the `__version__` back to `0.1.0`, and keep the `__instant_repo_version__`, if you want to keep a link upon which version of this project template the new pet project builds upon
- rename all `instant-repo` and `instant_repo` references to the new pet project name (`shift+command+R` or `+H` in most IDEs); don't forget the subdirectory below `src`

Finally, change up the `README.md` and existing `docs` as you please.

### Install project dependencies

This project assumes a generic Python development setup on your machine. For a more detailed setup guide, refer to my (upcoming) [dev-setup project](https://github.com/niklasbaier/dev-setup).

Install the appropriate version of Python (set it before in the `.pythion-version` file):

```
pyenv install <.python-version
```

Install the appropriate version of `poetry` (set it before in the `.poetry-version` file) via `pipx`:

```
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions in global scope

POETRY_VERSION=$(cat .poetry-version)
pipx install "poetry==$POETRY_VERSION"
```

Install the project dependencies from the `pyproject.toml` via:

```
poetry install
```

Install the pre-commit hooks from the `.pre-commit-config.yaml` via:

```
poetry run pre-commit install
```

## Usage

> Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

To run the main `src/instant_repo/app.py` file:

```
poetry run python3 app.py
```

To serve the documentation locally on your [localhost](http://127.0.0.1:8000/):

```
poetry run mkdocs serve
```

To run the tests

```
poetry run pytest tests/.
```

To run the pre-commit hooks manually:

```
poetry run pre-commit run --all
```

For development, it pays to follow the best practices of the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) and [PEP 8](https://peps.python.org/pep-0008/).

It also makes sense to work in dedicated feature branches that relate to specific issues, and then open up PRs to merge into `main`. Once a push or merge into `main` has been successful, a version bump and automated changelog update will be triggered by the `bump` job of the CICD, as well as the creation of a new release tag, and a deployment of the updated docs to Github pages.

## Support

> Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap

> If you have ideas for releases in the future, it is a good idea to list them in the README.

While updates to this repository will most likely come in rather unregular intervals (once I have learned something new & worthwile), I already have some ideas in mind, such as:

- alternative branches for specific use cases, e.g. for DB / API services, a UI skeleton, an ML-focused project that utilizes MLflow / Metaflow, etc.
- cli commands via `click`
- feature flags

## Contributing

> State if you are open to contributions and what your requirements are for accepting them.

> For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

> You can also document commands to [lint the code](https://stackoverflow.com/questions/8503559/what-is-linting) or [run tests](https://en.wikipedia.org/wiki/Test_automation). These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a [Selenium](https://www.selenium.dev/) server for testing in a browser.

## Authors and acknowledgment

> Show your appreciation to those who have contributed to the project.

This project template bundles many of the best practices I'm learning at work through my peers, and seniors. It also includes a lot of wisdom of the crowd from various corners of the internet, so I'm thankful for everyone out there who spends time & resources to help out beginners!

## License

> For open source projects, say how it is [licensed](https://choosealicense.com/).

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Project status

> If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
