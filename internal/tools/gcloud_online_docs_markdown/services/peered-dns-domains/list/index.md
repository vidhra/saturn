# gcloud services peered-dns-domains list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/list](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/list)*

**NAME**

: **gcloud services peered-dns-domains list - list the peered DNS domains for a private service connection**

**SYNOPSIS**

: **`gcloud services peered-dns-domains list` `[--network](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/list#--network)`=`NETWORK` [`[--service](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/list#--service)`=`SERVICE`; default="servicenetworking.googleapis.com"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command lists the peered DNS domains for a private service connection.

**EXAMPLES**

: To list the peered DNS domains for a private service connection between service
``peering-service`` and the consumer network
``my-network`` in the current project, run:

```
gcloud services peered-dns-domains list --network=my-network --service=peering-service
```

**REQUIRED FLAGS**

: **--network**:
Network in the consumer project peered with the service.

**OPTIONAL FLAGS**

: **--service**:
Name of the service to list the peered DNS domains for.

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
gcloud alpha services peered-dns-domains list
```

```
gcloud beta services peered-dns-domains list
```