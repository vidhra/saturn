# gcloud services peered-dns-domains delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete)*

**NAME**

: **gcloud services peered-dns-domains delete - delete a peered DNS domain for a private service connection**

**SYNOPSIS**

: **`gcloud services peered-dns-domains delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete#NAME)` `[--network](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete#--async)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete#--service)`=`SERVICE`; default="servicenetworking.googleapis.com"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command deletes a peered DNS domain from a private service connection.

**EXAMPLES**

: To delete a peered DNS domain called `example-com` from a private
service connection between service `peering-service` and the consumer
network `my-network` in the current project, run:

```
gcloud services peered-dns-domains delete example-com --network=my-network --service=peering-service
```

To run the same command asynchronously (non-blocking), run:

```
gcloud services peered-dns-domains delete example-com --network=my-network --service=peering-service --async
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the peered DNS domain to delete.

**REQUIRED FLAGS**

: **--network**:
The network in the consumer project peered with the service.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--service**:
The name of the service to delete a peered DNS domain for.

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
gcloud alpha services peered-dns-domains delete
```

```
gcloud beta services peered-dns-domains delete
```