# gcloud infra-manager previews export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/export](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/export)*

**NAME**

: **gcloud infra-manager previews export - export preview results**

**SYNOPSIS**

: **`gcloud infra-manager previews export` (`[PREVIEW](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/export#PREVIEW)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/export#--location)`=`LOCATION`) [`[--file](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/export#--file)`=`FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command generates a signed url to download a preview results.

**EXAMPLES**

: Export preview results for `my-preview`:

```
gcloud infra-manager previews export projects/p1/locations/us-central1/previews/my-preview
```

**POSITIONAL ARGUMENTS**

: **Preview resource - the preview to be used as parent. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `PREVIEW` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PREVIEW`**:
ID of the preview or fully qualified identifier for the preview.
To set the `preview` attribute:

- provide the argument `PREVIEW` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the preview.
To set the `location` attribute:

- provide the argument `PREVIEW` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

**FLAGS**

: **--file**:
File name for preview export artifacts. It is optional and it specifies the
filename or complete path for the downloaded preview export artifacts. If only a
file path is provided, the artifacts will be downloaded as "preview" within that
directory. If a filename is included, the artifacts will be downloaded with that
name.

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