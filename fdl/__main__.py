from enum import Enum
from typing import NewType, TypedDict, Optional

from traitlets import Callable


class InstallType(Enum):
    PACKAGE_MANAGER = "package_manager"
    BINARY_DOWNLOAD = "binary_download"
    GIT_CLONE = "git_clone"


class Status(Enum):
    SUCCESS = "success"  # installed
    FAILURE = "failure"  # failed to install
    SKIP = "skip"        # skipped because already installed
    PENDING = "pending"  # waiting for installation


class State(Enum):
    # Installing the app
    #
    # if InstallType == PACKAGE_MANAGER:
    #   Means the app is installing by package manager
    # elif InstallType == BINARY_DOWNLOAD:
    #   Means the app is moving to /usr/local/bin/
    # else:
    #   Means the app is symlinking to /usr/local/bin/
    INSTALLING = "installing"
    # Download the app from the internet
    #
    # if InstallType == PACKAGE_MANAGER:
    #   Means the package is downloading
    # elif InstallType == BINARY_DOWNLOAD:
    #   Means the binary source is downloading
    # else:
    #   Means the repository is cloneing
    DOWNLOADING = "downloading"
    # Checking if the app is exist
    CHECKING = "checking"


class App(TypedDict):
    name: Optional[str]                   # App name
    install_type: Optional[InstallType]   # Method for installing the app
    state: Optional[State]                # State of the app
    status: Optional[Status]              # Status of the app
    # PACKAGE_MANAGER related attributes
    package_copr_repo_name: Optional[str]
    package_external_repo_url: Optional[str]
    # BINARY_DOWNLOAD related attributes
    binary_download_url: Optional[str]
    binary_download_to: Optional[str]
    # GIT_CLONE related attributes
    git_repo_url: Optional[str]
    git_tag_name: Optional[str]
    git_clone_to: Optional[str]
    git_bin_symlink_to: Optional[str]


class AppWithLog(TypedDict):
    result: App
    logs: list[str]


Transform = NewType('Transform', Callable[[App], AppWithLog])


def wrap_app(app: App) -> AppWithLog:
    return AppWithLog(
        result=app,
        logs=[]
    )


def apply_app(input: AppWithLog, transform: Transform):
    newAppWithLog = transform(input.result)
    return AppWithLog(
        result=newAppWithLog.result,
        logs=input.logs.append(newAppWithLog.logs)
    )


def install(app: App) -> AppWithLog:
    if app.get('install_type') == InstallType.PACKAGE_MANAGER:
        raise NotImplementedError
    elif app.get('install_type') == InstallType.BINARY_DOWNLOAD:
        raise NotImplementedError
    elif app.get('install_type') == InstallType.GIT_CLONE:
        raise NotImplementedError
    return AppWithLog(

    )


def main():
    print("Hello from fdl.")


if __name__ == "__main__":
    main()
