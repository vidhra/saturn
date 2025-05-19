# gcloud alpha ai index-endpoints update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update)*

**NAME**

: **gcloud alpha ai index-endpoints update - update an Vertex AI index endpoint**

**SYNOPSIS**

: **`gcloud alpha ai index-endpoints update` (`[INDEX_ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#INDEX_ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#--region)`=`REGION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update display name of index endpoint `123` under project
`example` in region `us-central1`, run:

```
gcloud alpha ai index-endpoints update --display-name=new-name --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Index endpoint resource - The index endpoint to update. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `index_endpoint` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INDEX_ENDPOINT`**:
ID of the index_endpoint or fully qualified identifier for the index_endpoint.
To set the `name` attribute:

- provide the argument `index_endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the index_endpoint.
To set the `region` attribute:

- provide the argument `index_endpoint` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**FLAGS**

: **--description**:
Description of the index endpoint.

**--display-name**:
Display name of the index endpoint.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud ai index-endpoints update
```

```
gcloud beta ai index-endpoints update
```