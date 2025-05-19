# gcloud alpha builds reject  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/reject](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/reject)*

**NAME**

: **gcloud alpha builds reject - reject a pending build**

**SYNOPSIS**

: **`gcloud alpha builds reject` `[BUILD](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/reject#BUILD)` [`[--comment](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/reject#--comment)`=`COMMENT`] [`[--url](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/reject#--url)`=`URL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/reject#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Reject a pending build.

**EXAMPLES**

: To reject a pending build with its ID, run:

```
gcloud alpha builds reject build-id
```

To reject multiple pending builds, run the command in a for loop:

```
for i in $(cat build-ids.txt); do gcloud alpha builds reject $i; done
```

**POSITIONAL ARGUMENTS**

: **Build resource - Build. This represents a Cloud resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `build` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BUILD`**:
ID of the build or fully qualified identifier for the build.
To set the `build` attribute:

- provide the argument `build` on the command line.**

**FLAGS**

: **--comment**:
Optional comment to annotate the build's rejection.

**--url**:
Optional URL to annotate the build's rejection.

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

: This command uses the `cloudbuild/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/cloud-build/docs/](https://cloud.google.com/cloud-build/docs/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta builds reject
```