# gcloud scc findings bulk-mute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute)*

**NAME**

: **gcloud scc findings bulk-mute - bulk mute Security Command Center findings based on a filter**

**SYNOPSIS**

: **`gcloud scc findings bulk-mute` `[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute#--filter)`=`FILTER` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute#--project)`=`PROJECT`) [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute#--location)`=`LOCATION`; default="global"] [`[--mute-state](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute#--mute-state)`=`MUTE_STATE`; default="muted"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Bulk mute Security Command Center findings based on a filter.

**EXAMPLES**

: To bulk mute findings given organization
``123`` based on a filter on category that
equals ``XSS_SCRIPTING``, run:

```
gcloud scc findings bulk-mute --organization=organizations/123 --filter="category=\"XSS_SCRIPTING\""
```

To bulk mute findings given folder ``123``
based on a filter on category that equals
``XSS_SCRIPTING``, run:

```
gcloud scc findings bulk-mute --folder=folders/123 --filter="category=\"XSS_SCRIPTING\""
```

To bulk mute findings given project ``123``
based on a filter on category that equals
``XSS_SCRIPTING``, run:

```
gcloud scc findings bulk-mute --project=projects/123 --filter="category=\"XSS_SCRIPTING\""
```

To bulk mute findings given organization
``123`` based on a filter on category that
equals ``XSS_SCRIPTING`` and
`location=eu` run:

```
gcloud scc findings bulk-mute --organization=organizations/123 --filter="category=\"XSS_SCRIPTING\"" --location=locations/eu
```

**REQUIRED FLAGS**

: **--filter**:
Expression that identifies findings that should be muted.

**--folder**

**OPTIONAL FLAGS**

: **--location**:
When data residency controls are enabled, this attribute specifies the location
in which the resource is located and applicable. The `location`
attribute can be provided as part of the fully specified resource name or with
the `--location` argument on the command line. The default location
is `global`. NOTE: If you override the endpoint to a [regional
endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data
location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated
to the default location that is specified when data residency controls are
enabled for Security Command Center.

**--mute-state**:
Desired mute state of the finding. `MUTE_STATE` must be
one of: `muted`, `undefined`.

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

**API REFERENCE**

: This command uses the Security Command Center API. For more information, see [Security
Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)

**NOTES**

: This variant is also available:

```
gcloud alpha scc findings bulk-mute
```