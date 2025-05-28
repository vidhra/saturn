# gcloud components  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components](https://cloud.google.com/sdk/gcloud/reference/components)*

**NAME**

: **gcloud components - list, install, update, or remove Google Cloud CLI components**

**SYNOPSIS**

: **`gcloud components` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/components#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/components#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud components command group lets you control which tools are installed
in the Google Cloud CLI. It can be used to install, update and remove components
of the Google Cloud CLI, ensuring a lean, up-to-date installation.
gcloud components regularly checks whether updates are available for the tools
you already have installed, and gives you the opportunity to upgrade to the
latest version.
Certain components have dependencies. gcloud components will install any
dependencies, and during removal, any dependant components will be uninstalled
automatically.

**EXAMPLES**

: To see all available components:

```
gcloud components list
```

To install a component you don't have:

```
gcloud components install COMPONENT
```

To remove a component you no longer need:

```
gcloud components remove COMPONENT
```

To update all components you have to their latest version:

```
gcloud components update
```

To update all installed components to version 1.2.3:

```
gcloud components update --version 1.2.3
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[repositories](https://cloud.google.com/sdk/gcloud/reference/components/repositories)`**:
Manage additional component repositories for Trusted Tester programs.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[install](https://cloud.google.com/sdk/gcloud/reference/components/install)`**:
Install one or more Google Cloud CLI components.

**`[list](https://cloud.google.com/sdk/gcloud/reference/components/list)`**:
List the status of all Google Cloud CLI components.

**`[reinstall](https://cloud.google.com/sdk/gcloud/reference/components/reinstall)`**:
Reinstall the Google Cloud CLI with the same components you have now.

**`[remove](https://cloud.google.com/sdk/gcloud/reference/components/remove)`**:
Remove one or more installed components.

**`[update](https://cloud.google.com/sdk/gcloud/reference/components/update)`**:
Update all of your installed components to the latest version.