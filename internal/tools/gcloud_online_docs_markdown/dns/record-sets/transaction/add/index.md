# gcloud dns record-sets transaction add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add)*

**NAME**

: **gcloud dns record-sets transaction add - append a record-set addition to the transaction**

**SYNOPSIS**

: **`gcloud dns record-sets transaction add` `[RRDATAS](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#RRDATAS)` [`[RRDATAS](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#RRDATAS)` …] `[--name](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#--name)`=`NAME` `[--ttl](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#--ttl)`=`TTL` `[--type](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#--type)`=`TYPE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#ZONE)` [`[--transaction-file](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#--transaction-file)`=`TRANSACTION_FILE`; default="transaction.yaml"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command appends a record-set addition to the transaction.
For a guide detailing how to manage records, see: [https://cloud.google.com/dns/records/](https://cloud.google.com/dns/records/)

**EXAMPLES**

: To add an A record with an IP address of "1.2.3.4", domain name of "my.domain.",
and a managed zone "MANAGED_ZONE", run:

```
gcloud dns record-sets transaction add "1.2.3.4" --name=my.domain. --ttl=1234 --type=A --zone=MANAGED_ZONE
```

To add a TXT record with multiple data values while specifying time to live as
14400 seconds, run:

```
gcloud dns record-sets transaction add "Hello world" "Bye world" --name=my.domain. --ttl=14400 --type=TXT --zone=MANAGED_ZONE
```

**POSITIONAL ARGUMENTS**

: **`RRDATAS` [`RRDATAS` …]**:
DNS data (Address/CNAME/MX info, etc.) of the record-set to add. This is RDATA;
the format of this information varies depending on the type and class of the
resource record.

**REQUIRED FLAGS**

: **--name**:
DNS or domain name of the record-set to add.

**--ttl**:
TTL (time to live) for the record-set to add.

**--type**:
DNS record type of the record-set to add.

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
gcloud alpha dns record-sets transaction add
```

```
gcloud beta dns record-sets transaction add
```