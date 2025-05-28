# gcloud components remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components/remove](https://cloud.google.com/sdk/gcloud/reference/components/remove)*

**NAME**

: **gcloud components remove - remove one or more installed components**

**SYNOPSIS**

: **`gcloud components remove` `[COMPONENT_ID](https://cloud.google.com/sdk/gcloud/reference/components/remove#COMPONENT_ID)` [`[COMPONENT_ID](https://cloud.google.com/sdk/gcloud/reference/components/remove#COMPONENT_ID)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Uninstall all listed components, as well as all components that directly or
indirectly depend on them.
The command lists all components it is about to remove, and asks for
confirmation before proceeding.

**EXAMPLES**

: To remove ``COMPONENT-1``,
``COMPONENT-2``, and all components that
directly or indirectly depend on
``COMPONENT-1`` or
``COMPONENT-2``, type the following:

```
gcloud components remove COMPONENT-1 COMPONENT-2
```

**POSITIONAL ARGUMENTS**

: **`COMPONENT_ID` [`COMPONENT_ID` …]**:
The IDs of the components to be removed.

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