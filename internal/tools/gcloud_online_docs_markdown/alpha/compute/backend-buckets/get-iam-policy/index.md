# gcloud alpha compute backend-buckets get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy)*

**NAME**

: **gcloud alpha compute backend-buckets get-iam-policy - get the IAM policy for a Compute Engine backend bucket**

**SYNOPSIS**

: **`gcloud alpha compute backend-buckets get-iam-policy` `[BACKEND_BUCKET](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy#BACKEND_BUCKET)` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute backend-buckets
get-iam-policy` displays the IAM policy associated with a Compute Engine
backend bucket in a project. If formatted as JSON, the output can be edited and
used as a policy file for set-iam-policy. The output includes an "etag" field
identifying the version emitted and allowing detection of concurrent policy
updates; see $ {parent} set-iam-policy for additional details.

**EXAMPLES**

: To print the IAM policy for a given backend bucket, run:

```
gcloud alpha compute backend-buckets get-iam-policy my-backend-bucket
```

**POSITIONAL ARGUMENTS**

: **Backend bucket resource - The network to display the IAM policy for. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backend_bucket` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKEND_BUCKET`**:
ID of the backend bucket or fully qualified identifier for the backend bucket.
To set the `backend_bucket` attribute:

- provide the argument `backend_bucket` on the command line.**

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

: This command uses the `compute/alpha` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-buckets get-iam-policy
```

```
gcloud beta compute backend-buckets get-iam-policy
```