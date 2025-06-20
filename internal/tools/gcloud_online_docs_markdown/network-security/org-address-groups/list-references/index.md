# gcloud network-security org-address-groups list-references  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references)*

**NAME**

: **gcloud network-security org-address-groups list-references - lists References of an Organization Address Group**

**SYNOPSIS**

: **`gcloud network-security org-address-groups list-references` (`[ADDRESS_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#ADDRESS_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#--organization)`=`ORGANIZATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Lists References of an Organization Address Group.

**EXAMPLES**

: To list References of address group named my-address-group.

```
gcloud network-security org-address-groups list-references my-address-group
```

**POSITIONAL ARGUMENTS**

: **Address group resource - address group group help. The arguments in this group
can be used to specify the attributes of this resource.
This must be specified.

**`ADDRESS_GROUP`**:
ID of the address group or fully qualified identifier for the address group.
To set the `address_group` attribute:

- provide the argument `ADDRESS_GROUP` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `ADDRESS_GROUP` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
Organization number.
To set the `organization` attribute:

- provide the argument `ADDRESS_GROUP` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

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
gcloud alpha network-security org-address-groups list-references
```

```
gcloud beta network-security org-address-groups list-references
```