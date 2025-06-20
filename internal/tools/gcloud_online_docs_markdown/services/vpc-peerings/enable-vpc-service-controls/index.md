# gcloud services vpc-peerings enable-vpc-service-controls  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls)*

**NAME**

: **gcloud services vpc-peerings enable-vpc-service-controls - enable VPC Service Controls for the peering connection**

**SYNOPSIS**

: **`gcloud services vpc-peerings enable-vpc-service-controls` `[--network](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls#--async)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls#--service)`=`SERVICE`; default="servicenetworking.googleapis.com"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command configures IPv4 routes and DNS zones applicable to a service
producer VPC network (for example, servicenetworking). The route and DNS
configuration match those recommended for using the restricted.googleapis.com
VIP:
When enabled, Google Cloud makes the following route configuration changes in
the service producer VPC network: Google Cloud removes the IPv4 default route
(destination 0.0.0.0/0, next hop default internet gateway). Google Cloud then
creates an IPv4 route for destination 199.36.153.4/30 using the default internet
gateway next hop.
When enabled, Google Cloud also creates Cloud DNS managed private zones and
authorizes those zones for the service producer VPC network. The zones include
googleapis.com, pkg.dev, gcr.io, and other necessary domains or host names for
Google APIs and services that are compatible with VPC Service Controls. Record
data in the zones resolves all host names to 199.36.153.4, 199.36.153.5,
199.36.153.6, and 199.36.153.7.
When disabled, Google Cloud makes the following route configuration changes in
the service producer VPC network: Google Cloud restores a default route
(destination 0.0.0.0/0, next hop default internet gateway). Google Cloud also
deletes the Cloud DNS managed private zones that provided the host name
overrides.
While enabled, the service producer VPC network can still import static and
dynamic routes from the peered customer network if you enable custom route
export. These custom routes can include a default route. For this reason, this
command is not to be used solely as a means for preventing access to the
internet.

**EXAMPLES**

: To enable VPC Service Controls for a connection peering a network called
`my-network` on the current project to a service called
`your-service`, run:

```
gcloud services vpc-peerings enable-vpc-service-controls --network=my-network --service=your-service
```

To run the same command asynchronously (non-blocking), run:

```
gcloud services vpc-peerings enable-vpc-service-controls --network=my-network --service=your-service --async
```

**REQUIRED FLAGS**

: **--network**:
The network in the current project that is peered with the service.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--service**:
The service to enable VPC service controls for.

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
gcloud alpha services vpc-peerings enable-vpc-service-controls
```

```
gcloud beta services vpc-peerings enable-vpc-service-controls
```