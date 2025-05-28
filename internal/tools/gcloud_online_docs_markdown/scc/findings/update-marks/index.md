# gcloud scc findings update-marks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks)*

**NAME**

: **gcloud scc findings update-marks - update Security Command Center finding's security marks**

**SYNOPSIS**

: **`gcloud scc findings update-marks` `[FINDING](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#FINDING)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--location)`=`LOCATION`; default="global"] [`[--security-marks](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--security-marks)`=[`KEY`=`VALUE`,…]] [`[--source](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--source)`=`SOURCE`; default="-"] [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--start-time)`=`START_TIME`] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--update-mask)`=`UPDATE_MASK`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update Security Command Center finding's security marks.

**EXAMPLES**

: Selectively update security mark `Key1` with value `v1` on
testFinding. Note that other security marks on `testFinding` are
untouched:

```
gcloud scc findings update-marks `testFinding` --organization=123456 --source=5678 --security-marks="key1=v1" --update-mask="marks.markKey1"
```

Update all security marks on `testFinding`, under project
`example-project` and source `5678`:

```
gcloud scc findings update-marks projects/example-project/sources/5678/findings/testFinding --security-marks="key1=v1,key2=v2"
```

Update all security marks on `testFinding`, under folder
`456` and source `5678`:

```
gcloud scc findings update-marks folders/456/sources/5678/findings/testFinding --security-marks="key1=v1,key2=v2"
```

Update all security marks on `testFinding`, under organization
`123456` and source `5678`:

```
gcloud scc findings update-marks `testFinding` --organization=123456 --source=5678 --security-marks="key1=v1,key2=v2"
```

Delete all security marks on `testFinding`:

```
gcloud scc findings update-marks `testFinding` --organization=123456 --source=5678 --security-marks=""
```

Update all security marks on `testFinding`, under project
`example-project`, source `5678` and
`location=eu`:

```
gcloud scc findings update-marks projects/example-project/sources/5678/findings/testFinding --security-marks="key1=v1,key2=v2" --location=eu
```

**POSITIONAL ARGUMENTS**

: **`FINDING`**:
ID of the finding or fully qualified identifier for the finding.

**FLAGS**

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

**--security-marks**:
SecurityMarks resource to be passed as the request body. It's a key=value pair
separated by comma (,). For example: --security-marks="key1=val1,key2=val2".

**--source**:
Source id. Defaults to all sources.

**--start-time**:
Time at which the updated SecurityMarks take effect. See `$ [gcloud topic](https://cloud.google.com/sdk/gcloud/reference/topic) datetimes` for
information on supported time formats.

**--update-mask**:
Use update-mask if you want to selectively update marks represented by
--security-marks flag. For example: --update-mask="marks.key1,marks.key2". If
you want to override all the marks for the given finding either skip the
update-mask flag or provide an empty value (--update-mask '') for it.

**--folder**

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

: These variants are also available:

```
gcloud alpha scc findings update-marks
```

```
gcloud beta scc findings update-marks
```