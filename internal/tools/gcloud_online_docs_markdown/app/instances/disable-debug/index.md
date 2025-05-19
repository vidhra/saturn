# gcloud app instances disable-debug  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug)*

**NAME**

: **gcloud app instances disable-debug - disable debug mode for an instance**

**SYNOPSIS**

: **`gcloud app instances disable-debug` [`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#INSTANCE)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#SERVICE)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#VERSION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: When not in debug mode, SSH will be disabled on the VMs. They will be included
in the health checking pools.
Note that any local changes to an instance will be `lost` if debug
mode is disabled on the instance. New instance(s) may spawn depending on the
app's scaling settings.

**EXAMPLES**

: To disable debug mode for a particular instance, run:

```
gcloud app instances disable-debug --service=s1 --version=v1 i1
```

To disable debug mode for an instance chosen interactively, run:

```
gcloud app instances disable-debug
```

**POSITIONAL ARGUMENTS**

: **[`INSTANCE`]**:
The instance ID to disable debug mode on. If not specified, select instance
interactively. Must uniquely specify (with other flags) exactly one instance

**FLAGS**

: **--service**:
If specified, only match instances belonging to the given service. This affects
both interactive and non-interactive selection.

**--version**:
If specified, only match instances belonging to the given version. This affects
both interactive and non-interactive selection.

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

**NOTES**

: This variant is also available:

```
gcloud beta app instances disable-debug
```