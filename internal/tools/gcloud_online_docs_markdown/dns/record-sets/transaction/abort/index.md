# gcloud dns record-sets transaction abort  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort)*

**NAME**

: **gcloud dns record-sets transaction abort - abort transaction**

**SYNOPSIS**

: **`gcloud dns record-sets transaction abort` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort#ZONE)` [`[--transaction-file](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort#--transaction-file)`=`TRANSACTION_FILE`; default="transaction.yaml"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command aborts the transaction and deletes the transaction file.

**EXAMPLES**

: To abort the transaction, run:

```
gcloud dns record-sets transaction abort --zone=MANAGED_ZONE
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
gcloud alpha dns record-sets transaction abort
```

```
gcloud beta dns record-sets transaction abort
```