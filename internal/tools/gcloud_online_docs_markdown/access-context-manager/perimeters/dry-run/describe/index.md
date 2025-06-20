# gcloud access-context-manager perimeters dry-run describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/describe](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/describe)*

**NAME**

: **gcloud access-context-manager perimeters dry-run describe - display the dry-run mode configuration for a Service Perimeter**

**SYNOPSIS**

: **`gcloud access-context-manager perimeters dry-run describe` (`[PERIMETER](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/describe#PERIMETER)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/describe#--policy)`=`POLICY`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The dry-run mode configuration is presented as a diff against the enforcement
mode configuration. '+' indicates additions in `spec`,'-' indicates
removals from `status` and entries without either of those indicate
that they are the same across the dry-run and the enforcement mode
configurations. When a particular field is completely empty, it will not be
displayed.
Note: When this command is executed on a Service Perimeter with no explicit
dry-run mode configuration, the effective dry-run mode configuration is
inherited from the enforcement mode configuration, and thus, the enforcement
mode configuration is displayed in such cases.

**EXAMPLES**

: To display the dry-run mode configuration for a Service Perimeter:

```
gcloud access-context-manager perimeters dry-run describe my-perimeter
```

Sample output:

```
===
  name: my_perimeter
  title: My Perimeter
  type: PERIMETER_TYPE_REGULAR
  resources:
+   projects/123
-   projects/456
    projects/789
  restrictedServices:
+   bigquery.googleapis.com
-   storage.googleapis.com
    bigtable.googleapis.com
  vpcAccessibleServices:
+   allowedServices:
+     bigquery.googleapis.com
-     storage.googleapis.com
+   enableRestriction: true
```

**POSITIONAL ARGUMENTS**

: **Perimeter resource - The service perimeter to describe. The arguments in this
group can be used to specify the attributes of this resource.
This must be specified.

**`PERIMETER`**:
ID of the perimeter or fully qualified identifier for the perimeter.
To set the `perimeter` attribute:

- provide the argument `perimeter` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--policy**:
The ID of the access policy.
To set the `policy` attribute:

- provide the argument `perimeter` on the command line with a fully
specified name;
- provide the argument `--policy` on the command line;
- set the property `access_context_manager/policy`.**

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
gcloud alpha access-context-manager perimeters dry-run describe
```

```
gcloud beta access-context-manager perimeters dry-run describe
```