# gcloud compute url-maps remove-host-rule  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule)*

**NAME**

: **gcloud compute url-maps remove-host-rule - remove a host rule from a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps remove-host-rule` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule#URL_MAP)` `[--host](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule#--host)`=`HOST` [`[--delete-orphaned-path-matcher](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule#--delete-orphaned-path-matcher)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps remove-host-rule` is used to remove a host
rule from a URL map. When a host rule is removed, its path matcher is only
removed if it is not referenced by any other host rules and
`--delete-orphaned-path-matcher` is provided.

**EXAMPLES**

: To remove a host rule that contains the host `example.com` from the
URL map named `MY-URL-MAP`, you can use this command:

```
gcloud compute url-maps remove-host-rule MY-URL-MAP --host=example.com
```

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to operate on.

**REQUIRED FLAGS**

: **--host**:
One of the hosts in the host rule to remove.

**OPTIONAL FLAGS**

: **--delete-orphaned-path-matcher**:
If provided and a path matcher is orphaned as a result of this command, the
command removes the orphaned path matcher instead of failing.

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
gcloud alpha compute url-maps remove-host-rule
```

```
gcloud beta compute url-maps remove-host-rule
```