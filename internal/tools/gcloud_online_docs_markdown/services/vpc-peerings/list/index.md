# gcloud services vpc-peerings list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/list](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/list)*

**NAME**

: **gcloud services vpc-peerings list - list connections to a service via VPC peering for a project network**

**SYNOPSIS**

: **`gcloud services vpc-peerings list` `[--network](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/list#--network)`=`NETWORK` [`[--service](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/list#--service)`=`SERVICE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command lists connections of a network to a service via VPC peering for a
project.

**EXAMPLES**

: To list connections of a network called `my-network` to a service
called `your-service`, run:

```
gcloud services vpc-peerings list --network=my-network --service=your-service
```

To list connections of a network against all services, run:

```
gcloud services vpc-peerings list --network=my-network
```

**REQUIRED FLAGS**

: **--network**:
The network in the current project to list connections with the service

**OPTIONAL FLAGS**

: **--service**:
The service to list connections

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
gcloud alpha services vpc-peerings list
```

```
gcloud beta services vpc-peerings list
```