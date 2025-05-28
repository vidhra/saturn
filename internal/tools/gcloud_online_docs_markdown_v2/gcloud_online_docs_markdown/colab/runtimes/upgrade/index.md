# gcloud colab runtimes upgrade  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/upgrade](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/upgrade)*

**NAME**

: **gcloud colab runtimes upgrade - upgrade a runtime**

**SYNOPSIS**

: **`gcloud colab runtimes upgrade` (`[RUNTIME](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/upgrade#RUNTIME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/upgrade#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/upgrade#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/upgrade#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Upgrade a Colab Enterprise notebook runtime.

**EXAMPLES**

: To upgrade a runtime with id 'my-runtime' in region 'us-central1', run:

```
gcloud colab runtimes upgrade my-runtime --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Runtime resource - Unique name of the runtime to upgrade. This was optionally
provided by setting --runtime-id in the create runtime command, or was
system-generated if unspecified. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `runtime` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RUNTIME`**:
ID of the runtime or fully qualified identifier for the runtime.
To set the `name` attribute:

- provide the argument `runtime` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the runtime.
To set the `region` attribute:

- provide the argument `runtime` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `colab/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud beta colab runtimes upgrade
```