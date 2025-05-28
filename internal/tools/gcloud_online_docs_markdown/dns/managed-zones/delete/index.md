# gcloud dns managed-zones delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete)*

**NAME**

: **gcloud dns managed-zones delete - delete an empty Cloud DNS managed-zone**

**SYNOPSIS**

: **`gcloud dns managed-zones delete` `[ZONE_NAME](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete#ZONE_NAME)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command deletes an empty Cloud DNS managed-zone. An empty managed-zone has
only SOA and NS record-sets.

**EXAMPLES**

: To delete an empty managed-zone, run:

```
gcloud dns managed-zones delete my-zone
```

To delete an empty zonal managed-zone in us-east1-c, run:

```
gcloud dns managed-zones delete my-zone --location=us-east1-c
```

**POSITIONAL ARGUMENTS**

: **`ZONE_NAME`**:
The name of the empty managed-zone to be deleted.

**FLAGS**

: **--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

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
gcloud alpha dns managed-zones delete
```

```
gcloud beta dns managed-zones delete
```