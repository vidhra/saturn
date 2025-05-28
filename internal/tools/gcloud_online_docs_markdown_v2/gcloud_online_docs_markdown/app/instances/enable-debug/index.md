# gcloud app instances enable-debug  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug)*

**NAME**

: **gcloud app instances enable-debug - enable debug mode for an instance (only works on the flexible environment)**

**SYNOPSIS**

: **`gcloud app instances enable-debug` [`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#INSTANCE)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#SERVICE)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#VERSION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: When in debug mode, SSH will be enabled on the VMs, and you can use `[gcloud compute ssh](https://cloud.google.com/sdk/gcloud/reference/compute/ssh)` to login
to them. They will be removed from the health checking pools, but they still
receive requests.
Note that any local changes to an instance will be `lost` if debug
mode is disabled on the instance. New instance(s) may spawn depending on the
app's scaling settings.
Additionally, debug mode doesn't work for applications using the App Engine
standard environment.

**EXAMPLES**

: To enable debug mode for a particular instance, run:

```
gcloud app instances enable-debug --service=s1 --version=v1 i1
```

To enable debug mode for an instance chosen interactively, run:

```
gcloud app instances enable-debug
```

**POSITIONAL ARGUMENTS**

: **[`INSTANCE`]**:
Instance ID to enable debug mode on. If not specified, select instance
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
gcloud beta app instances enable-debug
```