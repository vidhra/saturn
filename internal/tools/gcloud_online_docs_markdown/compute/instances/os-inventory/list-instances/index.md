# gcloud compute instances os-inventory list-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances)*

**NAME**

: **gcloud compute instances os-inventory list-instances - list instances with specific OS inventory data values**

**SYNOPSIS**

: **`gcloud compute instances os-inventory list-instances` [`[--inventory-filter](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--inventory-filter)`=`INVENTORY_FILTER`] [`[--kernel-version](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--kernel-version)`=`KERNEL_VERSION` `[--os-shortname](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--os-shortname)`=`OS_SHORTNAME` `[--os-version](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--os-version)`=`OS_VERSION` `[--package-name](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--package-name)`=`PACKAGE_NAME` `[--package-version](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--package-version)`=`PACKAGE_VERSION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud compute instances os-inventory list-instances displays all Compute Engine
instances in a project matching an inventory filter. Run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters) to see the
supported filter syntax.

**EXAMPLES**

: To list all instances with OS inventory data in a project in table form, run:

```
gcloud compute instances os-inventory list-instances
```

To list the URIs of all instances whose OS short name contains rhel, run:

```
gcloud compute instances os-inventory list-instances --inventory-filter="ShortName:rhel" --uri
```

To list the URIs of all instances whose OS short name is equal to rhel, run:

```
gcloud compute instances os-inventory list-instances --os-shortname="rhel" --uri
```

To list all instances with package google-cloud-sdk of version 235.0.0-0
installed, run:

```
gcloud compute instances os-inventory list-instances --package-name="google-cloud-sdk" --package-version="235.0.0-0"
```

To list all instances with package name matching a regex ^google-cloud`available for update through apt, run:

```
gcloud compute instances os-inventory list-instances --inventory-filter="PackageUpdates.apt[].Name~^google-cloud*"
```

To list all instances with package update google-cloud-sdk of version greater
than or equal to 235.0.0-0 available through apt, run:

```
gcloud compute instances os-inventory list-instances --inventory-filter="PackageUpdates.apt[].['google-cloud-sdk'].Version>=235.0.0-0"
```

To list all instances missing the Stackdriver monitoring package
stackdriver-agent, run:

```
gcloud compute instances os-inventory list-instances --inventory-filter="NOT(InstalledPackages:stackdriver-agent)"
```

To list all Windows instances with an installed qfe hotfix whose ID equals
KB4462930, run:

```
gcloud compute instances os-inventory list-instances --inventory-filter="InstalledPackages.qfe[].HotFixID=KB4462930"
```

To list all Windows instances with a wua update whose description contains the
word Security, run:

```
gcloud compute instances os-inventory list-instances --inventory-filter="InstalledPackages.wua[].Description:Security"
````

**FLAGS**

: **--inventory-filter**:
Filter expression for matching against OS inventory criteria

**--kernel-version**

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
gcloud alpha compute instances os-inventory list-instances
```

```
gcloud beta compute instances os-inventory list-instances
```