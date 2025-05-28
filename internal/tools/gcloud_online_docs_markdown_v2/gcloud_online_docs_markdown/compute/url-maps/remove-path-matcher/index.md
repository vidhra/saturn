# gcloud compute url-maps remove-path-matcher  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher)*

**NAME**

: **gcloud compute url-maps remove-path-matcher - remove a path matcher from a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps remove-path-matcher` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher#URL_MAP)` `[--path-matcher-name](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher#--path-matcher-name)`=`PATH_MATCHER_NAME` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps remove-path-matcher` is used to remove a
path matcher from a URL map. When a path matcher is removed, all host rules that
refer to the path matcher are also removed.

**EXAMPLES**

: To remove the path matcher named ``MY-MATCHER``
from the URL map named ``MY-URL-MAP``, you can
use this command:

```
gcloud compute url-maps remove-path-matcher MY-URL-MAP --path-matcher-name=MY-MATCHER
```

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to operate on.

**REQUIRED FLAGS**

: **--path-matcher-name**:
The name of the path matcher to remove.

**OPTIONAL FLAGS**

: **--global**

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
gcloud alpha compute url-maps remove-path-matcher
```

```
gcloud beta compute url-maps remove-path-matcher
```