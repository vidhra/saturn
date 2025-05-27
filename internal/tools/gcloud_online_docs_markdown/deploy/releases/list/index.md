# gcloud deploy releases list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list)*

**NAME**

: **gcloud deploy releases list - list releases**

**SYNOPSIS**

: **`gcloud deploy releases list` [`[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#--region)`=`REGION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List the releases for a specified delivery pipeline.

**EXAMPLES**

: To list the releases for delivery pipeline 'test-pipeline', in region
'us-central1', run:

```
gcloud deploy releases list --delivery-pipeline=test-pipeline --region=us-central1
```

**FLAGS**

: **Delivery pipeline resource - The delivery pipeline for which you want to list
the releases. The arguments in this group can be used to specify the attributes
of this resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
To set the `project` attribute:

- provide the argument `--delivery-pipeline` on the command line with a
fully specified name;
- set the property `deploy/delivery_pipeline` with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--delivery-pipeline**:
ID of the delivery_pipeline or fully qualified identifier for the
delivery_pipeline.
To set the `delivery-pipeline` attribute:

- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
Location of the delivery_pipeline.
To set the `region` attribute:

- provide the argument `--delivery-pipeline` on the command line with a
fully specified name;
- set the property `deploy/delivery_pipeline` with a fully specified
name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

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

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--uri**:
Print a list of resource URIs instead of the default output, and change the
command output to a list of URIs. If this flag is used with
`--format`, the formatting is applied on this URI list. To display
URIs alongside other keys instead, use the `uri()` transform.

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

**API REFERENCE**

: This command uses the `clouddeploy/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/deploy/](https://cloud.google.com/deploy/)

**NOTES**

: These variants are also available:

```
gcloud alpha deploy releases list
```

```
gcloud beta deploy releases list
```