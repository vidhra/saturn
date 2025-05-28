# gcloud dns record-sets transaction describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe)*

**NAME**

: **gcloud dns record-sets transaction describe - describe the transaction**

**SYNOPSIS**

: **`gcloud dns record-sets transaction describe` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe#ZONE)` [`[--transaction-file](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe#--transaction-file)`=`TRANSACTION_FILE`; default="transaction.yaml"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays the contents of the transaction.

**EXAMPLES**

: To look at the contents of the transaction, run:

```
gcloud dns record-sets transaction describe --zone=MANAGED_ZONE
```

**REQUIRED FLAGS**

: **--zone**:
Name of the managed zone whose record sets you want to manage.

**OPTIONAL FLAGS**

: **--transaction-file**:
Path of the file which contains the transaction.

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
gcloud alpha dns record-sets transaction describe
```

```
gcloud beta dns record-sets transaction describe
```