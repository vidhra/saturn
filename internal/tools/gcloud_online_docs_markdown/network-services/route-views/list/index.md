# gcloud network-services route-views list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list)*

**NAME**

: **gcloud network-services route-views list - route View for a Mesh or Gateway**

**SYNOPSIS**

: **`gcloud network-services route-views list` (`[--gateway](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list#--gateway)`=`GATEWAY`     | `[--mesh](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list#--mesh)`=`MESH`) [`[--location](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list#--location)`=`LOCATION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list#--page-size)`=`PAGE_SIZE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all Route Views for a Mesh or Gateway

**EXAMPLES**

: List Route Views for a mesh.

```
gcloud network-services route-views list --mesh projects/-/locations/-/meshes/mesh1
gcloud network-services route-views list --project $PROJECT --location $LOCATION --mesh projects/-/locations/-/meshes/mesh1 List Route Views for a gateway.
```

```
gcloud network-services route-views list --gateway projects/-/locations/-/gateways/gateway1
gcloud network-services route-views list --project $PROJECT --location $LOCATION --gateway projects/-/locations/-/gateways/gateway1
```

**REQUIRED FLAGS**

: **Parent of the Route View
Exactly one of these must be specified:

**Gateway resource - Parent Gateway This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--gateway` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--gateway` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--gateway**:
ID of the gateway or fully qualified identifier for the gateway.
To set the `gateway` attribute:

- provide the argument `--gateway` on the command line.**

**Mesh resource - Parent Mesh This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--mesh` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--mesh` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--mesh**:
ID of the mesh or fully qualified identifier for the mesh.
To set the `mesh` attribute:

- provide the argument `--mesh` on the command line.****

**FLAGS**

: **Location resource - Location of the parent This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

**LIST COMMAND FLAGS**

: **--limit**:
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
gcloud alpha network-services route-views list
```