# gcloud compute target-grpc-proxies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/delete](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/delete)*

**NAME**

: **gcloud compute target-grpc-proxies delete - delete one or more target gRPC proxy**

**SYNOPSIS**

: **`gcloud compute target-grpc-proxies delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/delete#NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-grpc-proxies delete` deletes one or more
target gRPC proxies.

**EXAMPLES**

: Delete a global target gRPC proxy by running:

```
gcloud compute target-grpc-proxies delete PROXY_NAME
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the target gRPC proxies to delete.

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
gcloud alpha compute target-grpc-proxies delete
```

```
gcloud beta compute target-grpc-proxies delete
```