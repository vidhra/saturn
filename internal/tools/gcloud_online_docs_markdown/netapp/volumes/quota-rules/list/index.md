# gcloud netapp volumes quota-rules list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list)*

**NAME**

: **gcloud netapp volumes quota-rules list - list Cloud NetApp Volume QuotaRules**

**SYNOPSIS**

: **`gcloud netapp volumes quota-rules list` [`[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#--location)`=`LOCATION`] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#--volume)`=`VOLUME`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Lists Cloud NetApp Volume QuotaRules.

**EXAMPLES**

: The following command lists all QuotaRules in the given location and volume:

```
gcloud netapp volumes quota-rules list --location=us-central1 --volume=vol1
```

**FLAGS**

: **Location resource - The location in which to list Volume QuotaRules. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- uses all locations by default. with a fully specified name;
- set the property `netapp/location` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- uses all locations by default.;
- set the property `netapp/location`.**

**Volume resource - The volume for which quota rule applies. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--volume**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `--volume` on the command line.**

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

: This variant is also available:

```
gcloud beta netapp volumes quota-rules list
```