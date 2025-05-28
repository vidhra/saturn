# gcloud components list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components/list](https://cloud.google.com/sdk/gcloud/reference/components/list)*

**NAME**

: **gcloud components list - list the status of all Google Cloud CLI components**

**SYNOPSIS**

: **`gcloud components list` [`[--only-local-state](https://cloud.google.com/sdk/gcloud/reference/components/list#--only-local-state)`] [`[--show-platform](https://cloud.google.com/sdk/gcloud/reference/components/list#--show-platform)`] [`[--show-versions](https://cloud.google.com/sdk/gcloud/reference/components/list#--show-versions)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/components/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/components/list#--limit)`=`LIMIT`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/components/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command lists all the available components in the Google Cloud CLI. For
each component, the command lists the following information:

- Status on your local workstation: not installed, installed (and up to date), and
update available (installed, but not up to date)
- Name of the component (a description)
- ID of the component (used to refer to the component in other [gcloud components]
commands)
- Size of the component

**EXAMPLES**

: To list the status of all Google Cloud CLI components, run:

```
gcloud components list
```

To show the currently installed version (if any) and the latest available
version of each component, run:

```
gcloud components list --show-versions
```

**FLAGS**

: **--only-local-state**:
Only show locally installed components.

**--show-platform**:
Show operating system and architecture of all components

**--show-versions**:
Show installed and available versions of all components.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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