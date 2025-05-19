# gcloud container binauthz policy export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export)*

**NAME**

: **gcloud container binauthz policy export - export the Binary Authorization policy for the current project**

**SYNOPSIS**

: **`gcloud container binauthz policy export` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This function's default output is a valid policy YAML file. If dumped to a file
and edited, the new policy can be provided to the `$ [gcloud container binauthz
policy](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy) import` command to cause these edits to be reflected in the
project policy.

**EXAMPLES**

: To export the current project's policy:

```
gcloud container binauthz policy export > my_policy.yaml
```

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
gcloud alpha container binauthz policy export
```

```
gcloud beta container binauthz policy export
```