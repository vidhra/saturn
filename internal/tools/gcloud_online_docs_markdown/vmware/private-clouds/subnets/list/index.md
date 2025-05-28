# gcloud vmware private-clouds subnets list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list)*

**NAME**

: **gcloud vmware private-clouds subnets list - list subnets in a VMware Engine private cloud**

**SYNOPSIS**

: **`gcloud vmware private-clouds subnets list` (`[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#--private-cloud)`=`PRIVATE_CLOUD` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List subnets in a VMware Engine private cloud.

**EXAMPLES**

: To list subnets that belong to the private cloud `my-privatecloud` in
project `my-project` and zone `us-east2-b`, run:

```
gcloud vmware private-clouds subnets list --private-cloud=my-privatecloud --location=us-east2-b --project=my-project
```

Or:

```
gcloud vmware private-clouds subnets list --private-cloud=my-privatecloud
```

In the above example, the project and the location are taken from gcloud
properties `core/project` and `compute/zone`,
respectively.
To list subnets that belong to all the private clouds in project
`my-project` and zone `us-east2-b`, run:

```
gcloud vmware private-clouds subnets list --private-cloud=- --location=us-east2-b --project=my-project
```

Or:

```
gcloud vmware private-clouds subnets list --private-cloud=-
```

In the above example, the project and the location are taken from gcloud
properties `core/project` and `compute/zone`,
respectively.
To list subnets for all private clouds in all locations in project
`my-project`, run:

```
gcloud vmware private-clouds subnets list --private-cloud=- --location=- --project=my-project
```

Or:

```
gcloud vmware private-clouds subnets list --private-cloud=- --location=-
```

In the last example, the project is taken from gcloud properties
`core/project`.

**REQUIRED FLAGS**

: **Private cloud resource - private_cloud. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--private-cloud` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--private-cloud**:
ID of the private cloud or fully qualified identifier for the private cloud.
To set the `private-cloud` attribute:

- provide the argument `--private-cloud` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `--private-cloud` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.**

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