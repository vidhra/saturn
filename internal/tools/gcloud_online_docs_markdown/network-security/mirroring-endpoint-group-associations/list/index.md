# gcloud network-security mirroring-endpoint-group-associations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list)*

**NAME**

: **gcloud network-security mirroring-endpoint-group-associations list - list Mirroring Endpoint Group Associations**

**SYNOPSIS**

: **`gcloud network-security mirroring-endpoint-group-associations list` [`[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list#--location)`=`LOCATION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List mirroring endpoint group associations.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To list mirroring endpoint group associations in project `my-project`
and location `global`, run:
$ [gcloud
network-security mirroring-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations) \
```
list --project=my-project --location=global
```

OR
$ [gcloud
network-security mirroring-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations) \
```
list --location=global
```

OR
$ [gcloud
network-security mirroring-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations) \
```
list --location=projects/my-project/locations/global
```

**FLAGS**

: **Location resource - The location for a list operation This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- Location of the Mirroring Endpoint Group Association. Defaults to global with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- Location of the Mirroring Endpoint Group Association. Defaults to global.**

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
gcloud alpha network-security mirroring-endpoint-group-associations list
```

```
gcloud beta network-security mirroring-endpoint-group-associations list
```