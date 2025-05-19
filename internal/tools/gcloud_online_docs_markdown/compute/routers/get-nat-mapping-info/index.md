# gcloud compute routers get-nat-mapping-info  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info)*

**NAME**

: **gcloud compute routers get-nat-mapping-info - display NAT Mapping information in a router**

**SYNOPSIS**

: **`gcloud compute routers get-nat-mapping-info` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#NAME)` [`[--nat-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#--nat-name)`=`NAT_NAME`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#--region)`=`REGION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: ```
gcloud compute routers get-nat-mapping-info
```

shows a mapping of IP:port-ranges allocated to each VM's interface that is
configured to use NAT via the specified router.

**EXAMPLES**

: To show NAT mappings from all NATs in router 'r1' in region 'us-central1', run:

```
gcloud compute routers get-nat-mapping-info r1 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to get NAT mapping info.

**FLAGS**

: **--nat-name**:
The NAT name to filter out NAT mapping information

**--region**:
Region of the router to get NAT mapping info. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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
gcloud alpha compute routers get-nat-mapping-info
```

```
gcloud beta compute routers get-nat-mapping-info
```