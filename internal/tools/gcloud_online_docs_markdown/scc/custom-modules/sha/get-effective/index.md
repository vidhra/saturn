# gcloud scc custom-modules sha get-effective  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get-effective](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get-effective)*

**NAME**

: **gcloud scc custom-modules sha get-effective - get the details of a Security Health Analytics custom module with effective enablement state**

**SYNOPSIS**

: **`gcloud scc custom-modules sha get-effective` `[CUSTOM_MODULE](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get-effective#CUSTOM_MODULE)` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get-effective#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get-effective#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get-effective#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get-effective#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the details of a Security Health Analytics custom module. For inherited
custom modules, the get-effective command resolves INHERITED enablement states
to ENABLED or DISABLED. For example, if an inherited custom module is enabled at
the ancestor level, then the get-effective command displays the enablement state
as ENABLED instead of INHERITED in a child folder or project.

**EXAMPLES**

: To get the details of a Security Health Analytics custom module 123456 with its
effective enablement state from organization `123`, run:

```
gcloud scc custom-modules sha get-effective 123456 --organization=organizations/123
```

To get the details of a Security Health Analytics custom module 123456 with its
effective enablement state from folder `456`, run:

```
gcloud scc custom-modules sha get-effective 123456 --folder=folders/456
```

To get the details of a Security Health Analytics custom module 123456 with its
effective enablement state from project `789`, run:

```
gcloud scc custom-modules sha get-effective 123456 --project=projects/789
```

**POSITIONAL ARGUMENTS**

: **`CUSTOM_MODULE`**:
ID or the full resource name of the effective Security Health Analytics custom
module. If you specify the full resource name, you do not need to specify the
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
gcloud alpha scc custom-modules sha get-effective
```