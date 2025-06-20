# gcloud ai index-endpoints describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/index-endpoints/describe](https://cloud.google.com/sdk/gcloud/reference/ai/index-endpoints/describe)*

**NAME**

: **gcloud ai index-endpoints describe - gets detailed index endpoint information about the given index endpoint id**

**SYNOPSIS**

: **`gcloud ai index-endpoints describe` (`[INDEX_ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/ai/index-endpoints/describe#INDEX_ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/ai/index-endpoints/describe#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/index-endpoints/describe#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: Describe an index endpoint `123` of project `example` in
region `us-central1`, run:

```
gcloud ai index-endpoints describe 123 --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Index endpoint resource - The index endpoint to describe. The arguments in this
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
gcloud alpha ai index-endpoints describe
```

```
gcloud beta ai index-endpoints describe
```