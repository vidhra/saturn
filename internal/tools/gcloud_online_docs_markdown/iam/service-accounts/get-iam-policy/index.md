# gcloud iam service-accounts get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy)*

**NAME**

: **gcloud iam service-accounts get-iam-policy - get the IAM policy for a service account**

**SYNOPSIS**

: **`gcloud iam service-accounts get-iam-policy` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy#SERVICE_ACCOUNT)` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command gets the IAM policy for a service account. If formatted as JSON,
the output can be edited and used as a policy file for set-iam-policy. The
output includes an "etag" field identifying the version emitted and allowing
detection of concurrent policy updates; see $ [gcloud iam
service-accounts set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy) for additional details.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.
When managing IAM roles, you can treat a service account either as a resource or
as an identity. This command is to get the iam policy of a service account
resource. There are other gcloud commands to manage IAM policies for other types
of resources. For example, to manage IAM policies on a project, use the `$
[gcloud projects](https://cloud.google.com/sdk/gcloud/reference/projects)` commands.

**EXAMPLES**

: To print the IAM policy for a given service account, run:

```
gcloud iam service-accounts get-iam-policy my-iam-account@my-project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **`SERVICE_ACCOUNT`**:
The service account whose policy to get. The account should be formatted either
as a numeric service account ID or as an email, like this: 123456789876543212345
or my-iam-account@somedomain.com.

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
gcloud alpha iam service-accounts get-iam-policy
```

```
gcloud beta iam service-accounts get-iam-policy
```