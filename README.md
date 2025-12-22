# RunIfExists

Run a file or script if a specified file exists. Build complex workflows with Run If Exists.

[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/dseichter/RunIfExists/total)](https://github.com/dseichter/RunIfExists/releases)
![ruff](https://github.com/dseichter/RunIfExists/actions/workflows/ruff.yml/badge.svg)
![trivy](https://github.com/dseichter/RunIfExists/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_RunIfExists&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_RunIfExists)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=dseichter_RunIfExists)

## About

![Run If Exists](/images/runifexists.png "Run If Exists")

After almost 6 years, I have revised my tool **Run If Exists** and offer exactly the same function as last in 2016. Start applications as soon as a defined file exists. Define several different configurations and launch them in parallel so you can run multiple applications at once.

## Installation and configuration

The installation of Run If Exists is, like on my others tools, very simple. Download the executable file and define the program or script you want to run and the startup file that will make the defined program run. Activate the startup using the Activate button. For testing, you can have an empty start file created (via the Create Startfile button) or create a shortcut directly on your desktop.

Use the menu to access our website or check directly if an update is available.

Please make sure that a possibly existing file is overwritten when creating the start file (button “Create Startfile”). Therefore, check the correct spelling of your start file beforehand.

The start file is automatically deleted after execution. Therefore, do not necessarily use the startup file as a data source for your scripts, as this may make debugging more difficult.

If you have a new requirement that you would like me to add to Run If Exists, please do not hesitate to let me know. I will be very happy to extend the features so that the tool can be of even greater help to you.

## Workflows

You can also define more extensive workflows with Run If Exists. This depends on the applications or scripts you use.

You can also configure the processing of parallel tasks. Here it is important that a start file is read by several configurations at the same time. The only thing you have to pay attention to here is that you can actually execute the program or script to be started at the same time.

Since my program treats each process separately and does not perform any plausibility check to the other configurations, I cannot prevent the following:

* Endless loops
* High resource utilization
* Data loss

Therefore please check this carefully.

Run If Exists was created in the style of [IFTTT](https://en.wikipedia.org/wiki/IFTTT "IFTTT") (if this, than that) or its alternatives. However, with the goal of limiting itself to local scripts.

# Contributing

If you want to contribute by fixing an issue, add a new function or just optimize something, a simple instruction how to start development.

## Start development

Create and activate an environment by running the following command:

```python -m venv .venv```

```.venv/Scripts/activate```

Install the required dependencies

```pip install -r src/requirements.txt```

To run the application:

```python src/runifexists.py```


## 📄 License

GPL 3.0 — see [LICENSE](LICENSE) file at the root of the repository for details.

## Icons
 
GitHubIssueClient uses [Google Material Symbols](https://fonts.google.com/icons) within its code for UI icons.  
Material Symbols are licensed under the [Apache License 2.0](https://github.com/google/material-design-icons/blob/master/LICENSE) and are free for use in open source projects.