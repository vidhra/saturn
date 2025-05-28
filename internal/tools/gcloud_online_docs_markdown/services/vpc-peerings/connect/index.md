# gcloud services vpc-peerings connect  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect)*

**NAME**

: **gcloud services vpc-peerings connect - connect to a service via VPC peering for a project network**

**SYNOPSIS**

: **`gcloud services vpc-peerings connect` `[--network](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect#--network)`=`NETWORK` `[--ranges](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect#--ranges)`=`RANGES` [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect#--async)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect#--service)`=`SERVICE`; default="servicenetworking.googleapis.com"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command connects a private service connection to a service via a VPC
network.

**EXAMPLES**

: To connect a network called `my-network` on the current project to a
service called `your-service` with IP CIDR ranges
`google-range-1,google-range-2` for the service to use, run:

```
gcloud services vpc-peerings connect --network=my-network --service=your-service --ranges=google-range-1,google-range-2
```

To run the same command asynchronously (non-blocking), run:

```
gcloud services vpc-peerings connect --network=my-network --service=your-service --ranges=google-range-1,google-range-2 --async
```

**REQUIRED FLAGS**

: **--network**:
The network in the current project to be peered with the service

**--ranges**:
The names of IP CIDR ranges for service to use.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha services vpc-peerings connect
```

```
gcloud beta services vpc-peerings connect
```