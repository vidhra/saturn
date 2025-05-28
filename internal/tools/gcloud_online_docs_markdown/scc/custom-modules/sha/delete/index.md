# gcloud scc custom-modules sha delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete)*

**NAME**

: **gcloud scc custom-modules sha delete - delete a Security Health Analytics custom module**

**SYNOPSIS**

: **`gcloud scc custom-modules sha delete` `[CUSTOM_MODULE](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete#CUSTOM_MODULE)` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Security Health Analytics custom module.

**EXAMPLES**

: To delete a Security Health Analytics custom module with ID `123456`
for organization `123`, run:

```
gcloud scc custom-modules sha delete 123456 --organization=organizations/123
```

To delete a Security Health Analytics custom module with ID `123456`
for folder `456`, run:

```
gcloud scc custom-modules sha delete 123456 --folder=folders/456
```

To delete a Security Health Analytics custom module with ID `123456`
for project `789`, run:

```
gcloud scc custom-modules sha delete 123456 --project=projects/789
```

**POSITIONAL ARGUMENTS**

: **`CUSTOM_MODULE`**:
ID or the full resource name of the Security Health Analytics custom module. If
you specify the full resource name, you do not need to specify the
--organization, --folder, or --project flags.

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

**API REFERENCE**

: This command uses the `securitycenter/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: This variant is also available:

```
gcloud alpha scc custom-modules sha delete
```