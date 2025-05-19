# gcloud artifacts print-settings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings](https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings)*

**NAME**

: **gcloud artifacts print-settings - print snippets to add to native tools settings files**

**SYNOPSIS**

: **`gcloud artifacts print-settings` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The snippets provide a credentials placeholder and configurations to allow
native tools to interact with Artifact Registry repositories.

**EXAMPLES**

: To print a snippet to add a repository to the Gradle build.gradle file for
repository my-repo in the current project, run:

```
gcloud artifacts print-settings gradle --repository=my-repo
```

To print a snippet to add to the Maven pom.xml file for repository my-repo in
the current project, run:

```
gcloud artifacts print-settings mvn --repository=my-repo
```

To print a snippet to add to the npm .npmrc file for repository my-repo in the
current project, run:

```
gcloud artifacts print-settings npm --repository=my-repo
```

To print a snippet to add to the Python .pypirc and pip.comf files for
repository my-repo in the current project, run:

```
gcloud artifacts print-settings python --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[gradle](https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/gradle)`**:
Print a snippet to add a repository to the Gradle build.gradle file.

**`[mvn](https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/mvn)`**:
Print a snippet to add a Maven repository to the pom.xml file.

**`[npm](https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/npm)`**:
Print credential settings to add to the .npmrc file.

**`[python](https://cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/python)`**:
Print credential settings to add to the .pypirc and pip.conf files.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts print-settings
```

```
gcloud beta artifacts print-settings
```