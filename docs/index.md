This site contains the project documentation for the
`instant-repo` project.
Its aim is to provide a ready-to-go project skeleton that has been built according to best practices.

## Table of Contents

The documentation follows the best practice for
project documentation as described by Daniele Procida
in the [Diátaxis documentation framework](https://diataxis.fr/)
and consists of four separate parts:

1. [Tutorials](tutorials.md)
2. [How-To Guides](how-to-guides.md)
3. [Reference](reference.md)
4. [Explanation](explanation.md)

In addition to that, the following is also included

- [Information about the Author](author.md)
- [Automated Changelog](changelog.md)
- [Information about the Project's License](license.md)
- [Statement of Motivation](motivation.md)

Quickly find what you're looking for depending on
your use case by looking at the different pages.

## Project Overview

::: src.instant_repo

## Project Setup

Install project dependencies from `pyproject.toml`:

<!-- termynal -->

```
$ poetry install
---> 100%
Installed
```

Install pre-commit hooks from `.pre-commit-config.yaml`:

<!-- termynal -->

```
$ pre-commit install
---> 100%
Installed
```

Run the main `app.py` via:

```
poetry run python3 app.py
```

Run the docs locally via:

```
poetry run mkdocs serve
```

Run the tests via:

```
poetry run pytest tests/.
```

## Acknowledgements

This project template bundles many of the best practices I'm learning at work through my peers, and seniors. It also includes a lot of wisdom of the crowd from various corners of the internet, so I'm thankful for everyone out there who spends time & resources to help out beginners!
