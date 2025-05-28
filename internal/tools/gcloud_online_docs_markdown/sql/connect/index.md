# gcloud sql connect  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/connect](https://cloud.google.com/sdk/gcloud/reference/sql/connect)*

**NAME**

: **gcloud sql connect - connects to a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql connect` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/connect#INSTANCE)` [`[--database](https://cloud.google.com/sdk/gcloud/reference/sql/connect#--database)`=`DATABASE`, `[-d](https://cloud.google.com/sdk/gcloud/reference/sql/connect#-d)` `[DATABASE](https://cloud.google.com/sdk/gcloud/reference/sql/connect#DATABASE)`] [`[--user](https://cloud.google.com/sdk/gcloud/reference/sql/connect#--user)`=`USER`, `[-u](https://cloud.google.com/sdk/gcloud/reference/sql/connect#-u)` `[USER](https://cloud.google.com/sdk/gcloud/reference/sql/connect#USER)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/connect#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Connects to a Cloud SQL instance.
This command temporarily changes the authorized networks for this instance to
allow the connection from your IP address.
This command isn't supported for Cloud SQL instances with only private IP
addresses.
NOTE: If you're connecting from an IPv6 address, or are constrained by certain
organization policies (restrictPublicIP, restrictAuthorizedNetworks), consider
running the beta version of this command to avoid error by connecting through
the Cloud SQL proxy: `[gcloud beta sql connect](https://cloud.google.com/sdk/gcloud/reference/beta/sql/connect)`

**EXAMPLES**

: To connect to a Cloud SQL instance, run:

```
gcloud sql connect my-instance --user=root
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**FLAGS**

: **--database**:
The SQL Server database to connect to.

**--user**:
Cloud SQL instance user to connect as.

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
gcloud alpha sql connect
```

```
gcloud beta sql connect
```