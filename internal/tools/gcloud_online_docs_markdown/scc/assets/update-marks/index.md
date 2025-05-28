# gcloud scc assets update-marks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks](https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks)*

**NAME**

: **gcloud scc assets update-marks - update Cloud Security Command Center asset's security marks**

**SYNOPSIS**

: **`gcloud scc assets update-marks` (`[ASSET](https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks#ASSET)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks#--organization)`=`ORGANIZATION`) [`[--security-marks](https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks#--security-marks)`=[`KEY`=`VALUE`,…]] [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks#--start-time)`=`START_TIME`] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks#--update-mask)`=`UPDATE_MASK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/assets/update-marks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update Cloud Security Command Center asset's security marks.

**EXAMPLES**

: Selectively update value of security mark (key1) with 'val1.1' on asset 5678
under organization 123456. Note that other security marks on the same asset will
not change.

```
gcloud scc assets update-marks 5678 --organization=123456 --security-marks="key1=val1.1" --update-mask="marks.key1"
```

Update value of security mark (key1) and delete other marks on asset 5678 under
organization 123456:

```
gcloud scc assets update-marks 5678 --organization=123456 --security-marks="key1=updatedVal"
```

Update value of security mark (key1) and delete other marks on asset 5678 under
project example-project:

```
gcloud scc assets update-marks projects/example-project/assets/5678 --security-marks="key1=updatedVal"
```

Update value of security mark (key1) and delete other marks on asset 5678 under
folder 456:

```
gcloud scc assets update-marks folders/456/assets/5678 --security-marks="key1=updatedVal"
```

Delete all security marks on asset 5678 under organization 123456:

```
gcloud scc assets update-marks 5678 --organization=123456 --security-marks=""
```

**POSITIONAL ARGUMENTS**

: **Asset resource - The asset to be used for the SCC (Security Command Center)
command. The arguments in this group can be used to specify the attributes of
this resource.
This must be specified.

**`ASSET`**:
ID of the asset or fully qualified identifier for the asset.
To set the `asset` attribute:

- provide the argument `asset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
(Optional) If the full resource name isn't provided e.g. organizations/123, then
provide the organization id which is the suffix of the organization. Example:
organizations/123, the id is 123.
To set the `organization` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line;
- Set the organization property in configuration using `gcloud config set
scc/organization` if it is not specified in command line..**

**FLAGS**

: **--security-marks**:
SecurityMarks resource to be passed as the request body. It's a key=value pair
separated by comma (,). For example: --security-marks="key1=val1,key2=val2".

**--start-time**:
Time at which the updated SecurityMarks take effect. See `$ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for information on supported time formats.

**--update-mask**:
Use update-mask if you want to selectively update marks represented by
--security-marks flag. For example: --update-mask="marks.key1,marks.key2". If
you want to override all the marks for the given asset either skip the
update-mask flag or provide an empty value (--update-mask '') for it.

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

: This command uses the `securitycenter/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: These variants are also available:

```
gcloud alpha scc assets update-marks
```

```
gcloud beta scc assets update-marks
```