# gcloud alpha artifacts print-settings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings)*

**NAME**

: **gcloud alpha artifacts print-settings - print snippets to add to native tools settings files**

**SYNOPSIS**

: **`gcloud alpha artifacts print-settings` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The snippets provide a credentials placeholder and
configurations to allow native tools to interact with Artifact Registry
repositories.

**EXAMPLES**

: To print a snippet to add a repository to the Gradle build.gradle file for
repository my-repo in the current project, run:

```
gcloud alpha artifacts print-settings gradle --repository=my-repo
```

To print a snippet to add to the Maven pom.xml file for repository my-repo in
the current project, run:

```
gcloud alpha artifacts print-settings mvn --repository=my-repo
```

To print a snippet to add to the npm .npmrc file for repository my-repo in the
current project, run:

```
gcloud alpha artifacts print-settings npm --repository=my-repo
```

To print a snippet to add to the Python .pypirc and pip.comf files for
repository my-repo in the current project, run:

```
gcloud alpha artifacts print-settings python --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[apt](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/apt)`**:
`(ALPHA)` Print settings to add to the sources.list.d directory.

**`[gradle](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/gradle)`**:
`(ALPHA)` Print a snippet to add a repository to the Gradle
build.gradle file.

**`[mvn](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn)`**:
`(ALPHA)` Print a snippet to add a Maven repository to the pom.xml
file.

**`[npm](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/npm)`**:
`(ALPHA)` Print credential settings to add to the .npmrc file.

**`[python](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/python)`**:
`(ALPHA)` Print credential settings to add to the .pypirc and
pip.conf files.

**`[yum](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/yum)`**:
`(ALPHA)` Print settings to add to the yum.repos.d directory.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts print-settings
```

```
gcloud beta artifacts print-settings
```