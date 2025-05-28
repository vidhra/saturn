# gcloud dns record-sets transaction remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove)*

**NAME**

: **gcloud dns record-sets transaction remove - append a record-set deletion to the transaction**

**SYNOPSIS**

: **`gcloud dns record-sets transaction remove` `[RRDATAS](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#RRDATAS)` [`[RRDATAS](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#RRDATAS)` …] `[--name](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#--name)`=`NAME` `[--ttl](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#--ttl)`=`TTL` `[--type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#--type)`=`TYPE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#ZONE)` [`[--transaction-file](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#--transaction-file)`=`TRANSACTION_FILE`; default="transaction.yaml"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command appends a record-set deletion to the transaction.

**EXAMPLES**

: To remove an A record, run:

```
gcloud dns record-sets transaction remove --zone=MANAGED_ZONE --name=my.domain. --ttl=1234 --type=A "1.2.3.4"
```

To remove a TXT record with multiple data values, run:

```
gcloud dns record-sets transaction remove --zone=MANAGED_ZONE --name=my.domain. --ttl=2345 --type=TXT "Hello world" "Bye world"
```

**POSITIONAL ARGUMENTS**

: **`RRDATAS` [`RRDATAS` …]**:
DNS name of the record-set to be removed.

**REQUIRED FLAGS**

: **--name**:
DNS name of the record-set to be removed.

**--ttl**:
TTL for the record-set to be removed.

**--type**:
Type of the record-set to be removed.

**--zone**:
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
gcloud alpha dns record-sets transaction remove
```

```
gcloud beta dns record-sets transaction remove
```