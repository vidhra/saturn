# gcloud kms ekm-connections get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy)*

**NAME**

: **gcloud kms ekm-connections get-iam-policy - get the IAM policy for an ekm connection**

**SYNOPSIS**

: **`gcloud kms ekm-connections get-iam-policy` (`[EKM_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy#EKM_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Displays the IAM policy associated with an ekm connection. If formatted as JSON,
the output can be edited and used as a policy file for
`set-iam-policy`. The output includes an "etag" field identifying the
version emitted and allowing detection of concurrent policy updates; see $ [gcloud kms
ekm-connections set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/set-iam-policy) for additional details.

**EXAMPLES**

: To print the IAM policy for a given ekm connection, run:

```
gcloud kms ekm-connections get-iam-policy --location=my-location my-ekmconnection
```

**POSITIONAL ARGUMENTS**

: **Ekm connection resource - The ekm connection for which to get the IAM policy
binding. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `ekm_connection` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`EKM_CONNECTION`**:
ID of the ekm connection or fully qualified identifier for the ekm connection.
To set the `ekm_connection` attribute:

- provide the argument `ekm_connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the resource.
To set the `location` attribute:

- provide the argument `ekm_connection` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `cloudkms/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/kms/](https://cloud.google.com/kms/)

**NOTES**

: These variants are also available:

```
gcloud alpha kms ekm-connections get-iam-policy
```

```
gcloud beta kms ekm-connections get-iam-policy
```