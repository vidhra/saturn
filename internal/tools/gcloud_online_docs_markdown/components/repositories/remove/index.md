# gcloud components repositories remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components/repositories/remove](https://cloud.google.com/sdk/gcloud/reference/components/repositories/remove)*

**NAME**

: **gcloud components repositories remove - remove a registered Trusted Test component repository**

**SYNOPSIS**

: **`gcloud components repositories remove` [`[URL](https://cloud.google.com/sdk/gcloud/reference/components/repositories/remove#URL)` …] [`[--all](https://cloud.google.com/sdk/gcloud/reference/components/repositories/remove#--all)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components/repositories/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove a registered Trusted Tester component repository from the list of
repositories used by the component manager. After removing a repository, you can
run: $ [gcloud components
update](https://cloud.google.com/sdk/gcloud/reference/components/update) to revert back to the standard version of any components that were
installed from that repository.

**EXAMPLES**

: To be prompted for registered Trusted Tester component repositories to remove
run:

```
gcloud components repositories remove
```

**POSITIONAL ARGUMENTS**

: **[`URL` …]**:
Zero or more URLs for the component repositories you want to remove. If none are
given, you will be prompted to choose which existing repository you want to
remove.

**FLAGS**

: **--all**:
Remove all registered repositories.

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