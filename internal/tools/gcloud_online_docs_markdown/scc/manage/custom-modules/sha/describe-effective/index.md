# gcloud scc manage custom-modules sha describe-effective  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective)*

**NAME**

: **gcloud scc manage custom-modules sha describe-effective - get effective the details of a Security Health Analytics effective custom module**

**SYNOPSIS**

: **`gcloud scc manage custom-modules sha describe-effective` `[MODULE_ID_OR_NAME](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective#MODULE_ID_OR_NAME)` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective#--project)`=`PROJECT_ID_OR_NUMBER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the effective details of a Security Health Analytics effective custom
module. It retrieves a custom module with its effective enablement state.

**EXAMPLES**

: To get the effective details of a Security Health Analytics custom module with
ID `123456` for organization `123`, run:

```
gcloud scc manage custom-modules sha describe-effective 123456 --organization=123
```

To get the effective details of a Security Health Analytics custom module with
ID `123456` for folder `456`, run:

```
gcloud scc manage custom-modules sha describe-effective 123456 --folder=456
```

To get the effective details of a Security Health Analytics custom module with
ID `123456` for project `789`, run:

```
gcloud scc manage custom-modules sha describe-effective 123456 --project=789
```

You can also specify the parent more generally:

```
gcloud scc manage custom-modules sha describe-effective 123456 --parent=organizations/123
```

Or just specify the fully qualified module name:

```
gcloud scc manage custom-modules sha describe-effective organizations/123/locations/global/effectiveSecurityHealthAnalyticsCustomModules/123456
```

**POSITIONAL ARGUMENTS**

: **`MODULE_ID_OR_NAME`**:
The custom module ID or name. The expected format is
{parent}/[locations/global]/effectiveSecurityHealthAnalyticsCustomModules/{module_id}
or just {module_id}. Where module_id is a numeric identifier 1-20 characters in
length. Parent is of the form organizations/{id}, projects/{id or name},
folders/{id}.

**FLAGS**

: **--folder**

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

: This variant is also available:

```
gcloud alpha scc manage custom-modules sha describe-effective
```