# gcloud components install  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components/install](https://cloud.google.com/sdk/gcloud/reference/components/install)*

**NAME**

: **gcloud components install - install one or more Google Cloud CLI components**

**SYNOPSIS**

: **`gcloud components install` `COMPONENT-IDS` [`COMPONENT-IDS` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components/install#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Ensure that each of the specified components (as well as any dependent
components) is installed on the local workstation. Components are installed
without performing any upgrades to your existing CLI installation. All
components are installed at the current version of your CLI.
Components that are available for installation can be viewed by running:

```
gcloud components list
```

Installing a given component will also install all components on which it
depends. The command lists all components it is about to install, and asks for
confirmation before proceeding.
``gcloud components install`` installs
components from the version of the Google Cloud CLI you currently have
installed. You can see your current version by running:

```
gcloud version
```

If you want to update your Google Cloud CLI installation to the latest available
version, use:

```
gcloud components update
```

**EXAMPLES**

: The following command installs ``COMPONENT-1``,
``COMPONENT-2``, and all components that they
depend on:

```
gcloud components install COMPONENT-1 COMPONENT-2
```

**POSITIONAL ARGUMENTS**

: **`COMPONENT-IDS` [`COMPONENT-IDS` …]**:
The IDs of the components to be installed.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.