# gcloud compute url-maps validate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate)*

**NAME**

: **gcloud compute url-maps validate - validate a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps validate` [`[--load-balancing-scheme](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate#--load-balancing-scheme)`=`LOAD_BALANCING_SCHEME`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate#--source)`=`SOURCE`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Runs static validation for the UrlMap. In particular, the tests of the provided
UrlMap will be run. Calling this method does NOT create or update the UrlMap.

**EXAMPLES**

: A URL map can be validated by running:

```
gcloud compute url-maps validate --source=<path-to-file>
```

**FLAGS**

: **--load-balancing-scheme**:
Specifies the load balancer type this validation request is for. Use
`EXTERNAL_MANAGED` for global external Application Load Balancer. Use
`EXTERNAL` for classic Application Load Balancer.
Other load balancer types are not supported. For more information, refer to [Choosing
a load balancer](https://cloud.google.com/load-balancing/docs/choosing-load-balancer/).
If unspecified, the load balancing scheme will be inferred from the backend
service resources this URL map references. If that can not be inferred (for
example, this URL map only references backend buckets, or this URL map is for
rewrites and redirects only and doesn't reference any backends),
`EXTERNAL` will be used as the default type.
If specified, the scheme must not conflict with the load balancing scheme of the
backend service resources this URL map references.
`LOAD_BALANCING_SCHEME` must be one of:
`EXTERNAL`, `EXTERNAL_MANAGED`.

**--source**:
Path to a YAML file containing configuration export data. The YAML file must not
contain any output-only fields. Alternatively, you may omit this flag to read
from standard input. For a schema describing the export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/UrlMap.yaml.

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
gcloud alpha compute url-maps validate
```

```
gcloud beta compute url-maps validate
```