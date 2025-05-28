# gcloud services vpc-peerings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update)*

**NAME**

: **gcloud services vpc-peerings update - update a private service connection to a service for a project network**

**SYNOPSIS**

: **`gcloud services vpc-peerings update` `[--network](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update#--async)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update#--force)`] [`[--ranges](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update#--ranges)`=`RANGES`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update#--service)`=`SERVICE`; default="servicenetworking.googleapis.com"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates a private service connection to a service via a VPC
network.

**EXAMPLES**

: To update connection for a network called `my-network` on the current
project to a service called `your-service` with IP CIDR ranges
`google-range-1,google-range-2` for the service to use, run:

```
gcloud services vpc-peerings update --network=my-network --service=your-service --ranges=google-range-1,google-range-2
```

To run the same command asynchronously (non-blocking), run:

```
gcloud services vpc-peerings update --network=my-network --service=your-service --ranges=google-range-1,google-range-2 --async
```

**REQUIRED FLAGS**

: **--network**:
The network in the current project to be peered with the service

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--force**:
If specified, the update call will proceed even if the update can be
destructive.

**--ranges**:
The names of IP CIDR ranges for service to use.

**--service**:
The service to connect to

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
gcloud alpha services vpc-peerings update
```

```
gcloud beta services vpc-peerings update
```