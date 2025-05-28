# gcloud scc manage custom-modules sha describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe)*

**NAME**

: **gcloud scc manage custom-modules sha describe - get the details of a Security Health Analytics custom module**

**SYNOPSIS**

: **`gcloud scc manage custom-modules sha describe` `[MODULE_ID_OR_NAME](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe#MODULE_ID_OR_NAME)` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe#--project)`=`PROJECT_ID_OR_NUMBER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the details of a Security Health Analytics custom module. It does not
resolve INHERITED enablement states to ENABLED or DISABLED for modules created
at ancestor levels. For example, if the module is enabled at the ancestor level,
modules for all child resources will have the enablement state set to INHERITED.
Use `[gcloud
scc manage custom-modules sha describe-effective](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/describe-effective)` to retrieve a custom
module with its effective enablement state.

**EXAMPLES**

: To get the details of a Security Health Analytics custom module with ID
`123456` for organization `123`, run:

```
gcloud scc manage custom-modules sha describe 123456 --organization=123
```

To get the details of a Security Health Analytics custom module with ID
`123456` for folder `456`, run:

```
gcloud scc manage custom-modules sha describe 123456 --folder=456
```

To get the details of a Security Health Analytics custom module with ID
`123456` for project `789`, run:

```
gcloud scc manage custom-modules sha describe 123456 --project=789
```

You can also specify the parent more generally:

```
gcloud scc manage custom-modules sha describe 123456 --parent=organizations/123
```

Or just specify the fully qualified module name:

```
gcloud scc manage custom-modules sha describe organizations/123/locations/global/securityHealthAnalyticsCustomModules/123456
```

**POSITIONAL ARGUMENTS**

: **`MODULE_ID_OR_NAME`**:
The custom module ID or name. The expected format is
{parent}/[locations/global]/securityHealthAnalyticsCustomModules/{module_id} or
just {module_id}. Where module_id is a numeric identifier 1-20 characters in
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
gcloud alpha scc manage custom-modules sha describe
```