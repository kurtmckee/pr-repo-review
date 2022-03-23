# PC: Pre-commit
## PC0xx: pre-commit-hooks

from __future__ import annotations

from typing import Any


class PreCommit:
    requires = {"PY006"}

    @classmethod
    def check(cls, precommit: dict[str, Any]) -> bool:
        "Must have {cls.repo} repo in pre-commit config"
        for repo in precommit["repos"]:
            match repo:
                # pylint: disable-next=no-member
                case {"repo": cls.repo}:  # type: ignore[attr-defined]
                    return True
        return False


class PC100(PreCommit):
    "Has pre-commit-hooks"
    repo = "https://github.com/pre-commit/pre-commit-hooks"


class PC110(PreCommit):
    "Uses black"
    repo = "https://github.com/psf/black"


class PC120(PreCommit):
    "Uses isort"
    repo = "https://github.com/PyCQA/isort"


class PC130(PreCommit):
    "Uses flake8"
    repo = "https://github.com/pycqa/flake8"


class PC131(PreCommit):
    "Adds flake8-bugbear"
    requires = {"PC130"}

    @staticmethod
    def check(precommit: dict[str, Any]) -> bool:
        "Must have flake8-bugbear in additional_dependencies"
        for repo in precommit["repos"]:
            match repo:
                case {"repo": "https://github.com/pycqa/flake8"}:
                    for hook in repo["hooks"]:
                        match hook:
                            case {"additional_dependencies": list(x)}:
                                return "flake8-bugbear" in x
        return False


class PC140(PreCommit):
    "Uses mypy"
    repo = "https://github.com/pre-commit/mirrors-mypy"


class PC150(PreCommit):
    "Uses PyUpgrade"
    repo = "https://github.com/asottile/pyupgrade"


class PC160(PreCommit):
    "Uses codespell"
    repo = "https://github.com/codespell-project/codespell"


class PC170(PreCommit):
    "Uses PyGrep hooks"
    repo = "https://github.com/pre-commit/pygrep-hooks"
