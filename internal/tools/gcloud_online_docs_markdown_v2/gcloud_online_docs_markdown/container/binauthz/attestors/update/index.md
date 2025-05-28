# gcloud container binauthz attestors update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/update](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/update)*

**NAME**

: **gcloud container binauthz attestors update - update an existing Attestor**

**SYNOPSIS**

: **`gcloud container binauthz attestors update` `[ATTESTOR](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/update#ATTESTOR)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/update#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update an existing Attestor `my_attestor`:

```
gcloud container binauthz attestors update my_attestor --description="my new attestor description"
```

**POSITIONAL ARGUMENTS**

: **Attestor resource - The attestor to update. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `ATTESTOR` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ATTESTOR`**:
ID of the attestor or fully qualified identifier for the attestor.
To set the `name` attribute:

- provide the argument `ATTESTOR` on the command line.**

**FLAGS**

: **--description**:
The new description for the attestor

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

: These variants are also available:

```
gcloud alpha container binauthz attestors update
```

```
gcloud beta container binauthz attestors update
```