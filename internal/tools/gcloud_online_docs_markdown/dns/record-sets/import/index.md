# gcloud dns record-sets import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import)*

**NAME**

: **gcloud dns record-sets import - import record-sets into your managed-zone**

**SYNOPSIS**

: **`gcloud dns record-sets import` `[RECORDS_FILE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#RECORDS_FILE)` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#ZONE)` [`[--delete-all-existing](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#--delete-all-existing)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#--location)`=`LOCATION`] [`[--replace-origin-ns](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#--replace-origin-ns)`] [`[--zone-file-format](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#--zone-file-format)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command imports record-sets contained within the specified record-sets file
into your managed-zone. Note that NS records for the origin of the zone and the
SOA NS field are not imported since name-servers are managed by Cloud DNS. By
default, record-sets cannot be imported if there are any conflicts. A conflict
exists if an existing record-set has the same name and type as a record-set that
is being imported. In contrast, if the --delete-all-existing flag is used, the
imported record-sets will replace all the records-sets currently in the
managed-zone.

**EXAMPLES**

: To import record-sets from a yaml record-sets file, run:

```
gcloud dns record-sets import YAML_RECORDS_FILE --zone=MANAGED_ZONE
```

To import record-sets from a zone file, run:

```
gcloud dns record-sets import ZONE_FILE --zone-file-format --zone=MANAGED_ZONE
```

To replace all the record-sets in your zone with records from a yaml file, run:

```
gcloud dns record-sets import YAML_RECORDS_FILE --delete-all-existing --zone=MANAGED_ZONE
```

**POSITIONAL ARGUMENTS**

: **`RECORDS_FILE`**:
File from which record-sets should be imported. For examples of YAML-formatted
and BIND zone-formatted records files, refer to [https://cloud.google.com/dns/records#importing_and_exporting_record_sets](https://cloud.google.com/dns/records#importing_and_exporting_record_sets)

**REQUIRED FLAGS**

: **--zone**:
Name of the managed zone whose record sets you want to manage.

**OPTIONAL FLAGS**

: **--delete-all-existing**:
Indicates that all existing record-sets should be deleted before importing the
record-sets in the records-file.

**--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

**--replace-origin-ns**:
Indicates that NS records for the origin of a zone should be imported if defined

**--zone-file-format**:
Indicates that the input records-file is in BIND zone format. If omitted,
indicates that the records-file is in YAML format.

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
gcloud alpha dns record-sets import
```

```
gcloud beta dns record-sets import
```