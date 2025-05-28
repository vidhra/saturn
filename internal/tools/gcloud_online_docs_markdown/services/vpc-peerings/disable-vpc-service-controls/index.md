# gcloud services vpc-peerings disable-vpc-service-controls  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/disable-vpc-service-controls](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/disable-vpc-service-controls)*

**NAME**

: **gcloud services vpc-peerings disable-vpc-service-controls - disable VPC Service Controls for the peering connection**

**SYNOPSIS**

: **`gcloud services vpc-peerings disable-vpc-service-controls` `[--network](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/disable-vpc-service-controls#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/disable-vpc-service-controls#--async)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/disable-vpc-service-controls#--service)`=`SERVICE`; default="servicenetworking.googleapis.com"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/disable-vpc-service-controls#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command disables VPC Service Controls for the peering connection.
The local default route (destination 0.0.0.0/0, next hop default internet
gateway) is recreated in the service producer VPC network. After the route is
recreated, the service producer VPC network cannot import a custom default route
from the peering connection to the customer VPC network.

**EXAMPLES**

: To disable VPC Service Controls for a connection peering a network called
`my-network` on the current project to a service called
`your-service`, run:

```
gcloud services vpc-peerings disable-vpc-service-controls --network=my-network --service=your-service
```

To run the same command asynchronously (non-blocking), run:

```
gcloud services vpc-peerings disable-vpc-service-controls --network=my-network --service=your-service --async
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
gcloud alpha services vpc-peerings disable-vpc-service-controls
```

```
gcloud beta services vpc-peerings disable-vpc-service-controls
```