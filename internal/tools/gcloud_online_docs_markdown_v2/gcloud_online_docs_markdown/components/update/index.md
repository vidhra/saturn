# gcloud components update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components/update](https://cloud.google.com/sdk/gcloud/reference/components/update)*

**NAME**

: **gcloud components update - update all of your installed components to the latest version**

**SYNOPSIS**

: **`gcloud components update` [`[--version](https://cloud.google.com/sdk/gcloud/reference/components/update#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Ensure that the latest version of all installed components is installed on the
local workstation.
The command lists all components it is about to update, and asks for
confirmation before proceeding.
By default, this command will update all components to their latest version.
This can be configured by using the `--version` flag to choose a
specific version to update to. This version may also be a version older than the
one that is currently installed, thus allowing you to downgrade your Google
Cloud CLI installation.
You can see your current Google Cloud CLI version by running:

```
gcloud version
```

To see the latest version of the Google Cloud CLI, run:

```
gcloud components list
```

If you run this command without the `--version` flag and you already
have the latest version installed, no update will be performed.

**EXAMPLES**

: To update all installed components to the latest version:

```
gcloud components update
```

To update all installed components to a fixed Google Cloud CLI version 1.2.3:

```
gcloud components update --version=1.2.3
```

**FLAGS**

: **--version**:
An optional Google Cloud CLI version to update your components to. By default,
components are updated to the latest available version. By selecting an older
version you can downgrade your Google Cloud CLI installation.

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