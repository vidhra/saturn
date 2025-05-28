# gcloud dns record-sets export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export)*

**NAME**

: **gcloud dns record-sets export - export your record-sets into a file**

**SYNOPSIS**

: **`gcloud dns record-sets export` `[RECORDS_FILE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export#RECORDS_FILE)` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export#ZONE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export#--location)`=`LOCATION`] [`[--zone-file-format](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export#--zone-file-format)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command exports the record-sets contained within the specified managed-zone
into a file. The formats you can export to are YAML records format (default) and
BIND zone file format.

**EXAMPLES**

: To export record-sets into a yaml file, run:

```
gcloud dns record-sets export records.yaml --zone=examplezonename
```

To export record-sets into a BIND zone formatted file instead, run:

```
gcloud dns record-sets export pathto.zonefile --zone=examplezonename --zone-file-format
```

Similarly, to import record-sets into a BIND zone formatted zone file, run:

```
gcloud dns record-sets import pathto.zonefile --zone-file-format --zone=examplezonename
```

**POSITIONAL ARGUMENTS**

: **`RECORDS_FILE`**:
File to which record-sets should be exported.

**REQUIRED FLAGS**

: **--zone**:
Name of the managed zone whose record sets you want to manage.

**OPTIONAL FLAGS**

: **--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

**--zone-file-format**:
Indicates that records-file should be in the zone file format. When using this
flag, expect the record-set to be exported to a BIND zone formatted file. If you
omit this flag, the record-set is exported into a YAML formatted records file.
Note, this format flag determines the format of the output recorded in the
records-file; it is different from the global `--format` flag which
affects console output alone.

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
gcloud alpha dns record-sets export
```

```
gcloud beta dns record-sets export
```