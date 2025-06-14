# gcloud kms inventory search-protected-resources  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources)*

**NAME**

: **gcloud kms inventory search-protected-resources - searches the resources protected by a key**

**SYNOPSIS**

: **`gcloud kms inventory search-protected-resources` `[--scope](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--scope)`=`ORGANIZATION_ID` (`[--keyname](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--keyname)`=`KEYNAME` : `[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--keyring)`=`KEYRING` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--location)`=`LOCATION`) [`[--resource-types](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--resource-types)`=[`RESOURCE_TYPES`,…]] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/inventory/search-protected-resources#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud kms inventory search-protected-resources` returns a list of
the resources a key is protecting within the specified organization.

**EXAMPLES**

: To view the protected resources for the key `puppy` and organization
number `1234` run:

```
gcloud kms inventory search-protected-resources --keyname=puppy --scope=1234
```

**REQUIRED FLAGS**

: **--scope**:
Organization ID.

**Key resource - The KMS key resource. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--keyname` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**--keyname**:
ID of the key or fully qualified identifier for the key.
To set the `key` attribute:

- provide the argument `--keyname` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--keyring**:
The KMS keyring of the key.
To set the `keyring` attribute:

- provide the argument `--keyname` on the command line with a fully
specified name;
- provide the argument `--keyring` on the command line.

**--location**:
The Google Cloud location for the key.
To set the `location` attribute:

- provide the argument `--keyname` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--resource-types**:
A list of resource types that this request searches for. If empty, it will
search all the [trackable
resource types](https://cloud.google.com/kms/docs/view-key-usage#tracked-resource-types).
Regular expressions are also supported. For example:

- ``compute.googleapis.com.*`` snapshots
resources whose type starts with
``compute.googleapis.com``.
- ``.*Image`` snapshots resources whose type ends
with ``Image``.
- ``.*Image.*`` snapshots resources whose type
contains ``Image``.

See [RE2](https://github.com/google/re2/wiki/Syntax) for all
supported regular expression syntax. If the regular expression does not match
any supported resource type, an
``INVALID_ARGUMENT`` error will be returned.

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

**NOTES**

: These variants are also available:

```
gcloud alpha kms inventory search-protected-resources
```

```
gcloud beta kms inventory search-protected-resources
```