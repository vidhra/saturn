# gcloud compute target-https-proxies export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export)*

**NAME**

: **gcloud compute target-https-proxies export - export a target HTTPS proxy**

**SYNOPSIS**

: **`gcloud compute target-https-proxies export` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export#NAME)` [`[--destination](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export#--destination)`=`DESTINATION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports a target HTTPS proxy's configuration to a file. This configuration can
be imported at a later time.

**EXAMPLES**

: A target HTTPS proxy can be exported by running:

```
gcloud compute target-https-proxies export NAME --destination=<path-to-file>
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target HTTPS proxy to export.

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output. For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/TargetHttpsProxy.yaml.

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
gcloud alpha compute target-https-proxies export
```

```
gcloud beta compute target-https-proxies export
```