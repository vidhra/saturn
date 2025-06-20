# gcloud network-services route-views describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/describe](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/describe)*

**NAME**

: **gcloud network-services route-views describe - route View for a Mesh or Gateway**

**SYNOPSIS**

: **`gcloud network-services route-views describe` (`[--route-view](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/describe#--route-view)`=`ROUTE_VIEW` : `[--gateway](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/describe#--gateway)`=`GATEWAY` `[--location](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/describe#--location)`=`LOCATION` `[--mesh](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/describe#--mesh)`=`MESH`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-services/route-views/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Route Views for a Mesh or Gateway

**EXAMPLES**

: Describe a Route Views for a Mesh

```
gcloud network-services route-views describe --project=$PROJECT_ID --location=$LOCATION --mesh mesh1 --route-view $ROUTE_VIEW_ID
gcloud network-services route-views describe --route-view=projects/-/locations/-/meshes/-/routeViews/$ROUTE_VIEW_ID
```

Describe a Route Views for a Gateway

```
gcloud network-services route-views describe --project=$PROJECT_ID --location=$LOCATION --gateway gateway1 --route-view $ROUTE_VIEW_ID
gcloud network-services route-views describe --route-view=projects/-/locations/-/gateways/-/routeViews/$ROUTE_VIEW_ID
```

**REQUIRED FLAGS**

: **Mesh or gateway route view resource - RouteView to describe The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--route-view` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [networkservices.projects.locations.meshes.routeViews,
networkservices.projects.locations.gateways.routeViews].

This must be specified.

**--route-view**:
ID of the mesh_or_gateway_route_view or fully qualified identifier for the
mesh_or_gateway_route_view.
To set the `route_view` attribute:

- provide the argument `--route-view` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--gateway**:
Parent Gateway of the mesh_or_gateway_route_view
To set the `gateway` attribute:

- provide the argument `--route-view` on the command line with a fully
specified name;
- provide the argument `--gateway` on the command line. Must be
specified for resource of type
[networkservices.projects.locations.gateways.routeViews].

**--location**:
Location of the mesh_or_gateway_route_view
To set the `location` attribute:

- provide the argument `--route-view` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--mesh**:
Parent Mesh of the mesh_or_gateway_route_view
To set the `mesh` attribute:

- provide the argument `--route-view` on the command line with a fully
specified name;
- provide the argument `--mesh` on the command line. Must be specified
for resource of type [networkservices.projects.locations.meshes.routeViews].**

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
gcloud alpha network-services route-views describe
```