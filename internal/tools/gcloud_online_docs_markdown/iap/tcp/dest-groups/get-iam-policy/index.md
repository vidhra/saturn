# gcloud iap tcp dest-groups get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy)*

**NAME**

: **gcloud iap tcp dest-groups get-iam-policy - get IAM policy for an IAP TCP Destination Group resource**

**SYNOPSIS**

: **`gcloud iap tcp dest-groups get-iam-policy` `[--dest-group](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy#--dest-group)`=`DEST_GROUP` `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy#--region)`=`REGION` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud iap tcp dest-groups get-iam-policy` displays the IAM policy
associated with an IAP TCP Destination Group resource. If formatted as JSON, the
output can be edited and used as a policy file for set-iam-policy. The output
includes an "etag" field identifying the version emitted and allowing detection
of concurrent policy updates; see $ [gcloud iap tcp
dest-groups set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/set-iam-policy) for additional details.

**EXAMPLES**

: To get the IAM policy for the TCP Destination Group resource with name
'my-group' and located in the region 'us-west1' within the active project, run:

```
gcloud iap tcp dest-groups get-iam-policy --dest-group='my-group' --region='us-west1'
```

To get the IAM policy for the TCP Destination Group resource with name
'my-group' and located in the region 'us-west1' within project 'project', run:

```
gcloud iap tcp dest-groups get-iam-policy --dest-group='my-group' --region='us-west1' --project='project'
```

**REQUIRED FLAGS**

: **--dest-group**:
Name of the Destination Group.

**--region**:
Region of the Destination Group.

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

**NOTES**

: These variants are also available:

```
gcloud alpha iap tcp dest-groups get-iam-policy
```

```
gcloud beta iap tcp dest-groups get-iam-policy
```