# gcloud dns managed-zones describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe)*

**NAME**

: **gcloud dns managed-zones describe - view the details of a Cloud DNS managed-zone**

**SYNOPSIS**

: **`gcloud dns managed-zones describe` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe#ZONE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays the details of the specified managed-zone.

**EXAMPLES**

: To display the details of your managed-zone, run:

```
gcloud dns managed-zones describe my-zone
```

To display the details of a zonal managed-zone in Zonal Cloud DNS service in
us-east1-c, run:

```
gcloud dns managed-zones describe my-zone --location=us-east1-c
```

**POSITIONAL ARGUMENTS**

: **Zone resource - The name of the managed-zone to be described. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ZONE`**:
ID of the zone or fully qualified identifier for the zone.
To set the `zone` attribute:

- provide the argument `zone` on the command line.**

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
gcloud alpha dns managed-zones describe
```

```
gcloud beta dns managed-zones describe
```