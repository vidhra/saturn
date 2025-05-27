# gcloud container hub update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/update](https://cloud.google.com/sdk/gcloud/reference/container/hub/update)*

**NAME**

: **gcloud container hub update - update a fleet**

**SYNOPSIS**

: **`gcloud container hub update` [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE` `[--binauthz-policy-bindings](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--binauthz-policy-bindings)`=[`name`=`BINAUTHZ_POLICY`] `[--security-posture](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--security-posture)`=`SECURITY_POSTURE` `[--workload-vulnerability-scanning](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--workload-vulnerability-scanning)`=`WORKLOAD_VULNERABILITY_SCANNING`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The project specified does not exist.
- The project specified already has a fleet.
- The active account does not have permission to access the given project.

**EXAMPLES**

: To update the display name of the fleet in project
`example-foo-bar-1` to `updated-name`, run:

```
gcloud container hub update --display-name=updated-name --project=example-foo-bar-1
```

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
Display name of the fleet to be created (optional). 4-30 characters,
alphanumeric and [ '"!-] only.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--binauthz-evaluation-mode**

**--clear-labels**

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
gcloud alpha container hub update
```

```
gcloud beta container hub update
```