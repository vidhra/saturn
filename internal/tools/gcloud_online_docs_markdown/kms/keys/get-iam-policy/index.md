# gcloud kms keys get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy)*

**NAME**

: **gcloud kms keys get-iam-policy - get the IAM policy for a key**

**SYNOPSIS**

: **`gcloud kms keys get-iam-policy` (`[KEY](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#KEY)` : `[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#--keyring)`=`KEYRING` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Gets the IAM policy for the given key.
Returns an empty policy if the resource does not have a policy set.

**EXAMPLES**

: The following command gets the IAM policy for the key `frodo` within
the keyring `fellowship` and location `global`:

```
gcloud kms keys get-iam-policy frodo --keyring=fellowship --location=global
```

**POSITIONAL ARGUMENTS**

: **Key resource - The KMS key resource. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- set the property `core/project`.

This must be specified.

**`KEY`**:
ID of the key or fully qualified identifier for the key.
To set the `key` attribute:

- provide the argument `key` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--keyring**:
The KMS keyring of the key.
To set the `keyring` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--keyring` on the command line.

**--location**:
The Google Cloud location for the key.
To set the `location` attribute:

- provide the argument `key` on the command line with a fully specified
name;
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

**NOTES**

: These variants are also available:

```
gcloud alpha kms keys get-iam-policy
```

```
gcloud beta kms keys get-iam-policy
```