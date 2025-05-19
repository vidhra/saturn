# gcloud compute forwarding-rules export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export)*

**NAME**

: **gcloud compute forwarding-rules export - export a forwarding rule**

**SYNOPSIS**

: **`gcloud compute forwarding-rules export` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export#NAME)` [`[--destination](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export#--destination)`=`DESTINATION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports a forwarding rule's configuration to a file.

**EXAMPLES**

: A forwarding rule can be exported by running:

```
gcloud compute forwarding-rules export NAME --destination=<path-to-file>
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the forwarding rule to export.

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output. For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/ForwardingRule.yaml.

**--global**

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
gcloud alpha compute forwarding-rules export
```

```
gcloud beta compute forwarding-rules export
```