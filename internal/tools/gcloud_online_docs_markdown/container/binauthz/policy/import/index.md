# gcloud container binauthz policy import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/import](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/import)*

**NAME**

: **gcloud container binauthz policy import - import a Binary Authorization policy to the current project**

**SYNOPSIS**

: **`gcloud container binauthz policy import` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/import#POLICY_FILE)` [`[--strict-validation](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/import#--strict-validation)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command accepts a description of the desired policy in the form of a
YAML-formatted file. A representation of the current policy can be retrieved
using the $ [gcloud container
binauthz policy export](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export) command. One method of modifying the policy is to run
`$ [gcloud
container binauthz policy export](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export)`, dump the contents to a file, modify
the policy file to reflect the desired new policy, and provide this modified
file to `$ gcloud container binauthz policy import`.

**EXAMPLES**

: To update the current project's policy:

```
gcloud container binauthz policy export > my_policy.yaml
```

```
edit my_policy.yaml
```

```
gcloud container binauthz policy import my_policy.yaml
```

**POSITIONAL ARGUMENTS**

: **`POLICY_FILE`**:
The file containing the YAML-formatted policy description.

**FLAGS**

: **--strict-validation**:
Whether to perform additional checks on the validity of policy contents.

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
gcloud alpha container binauthz policy import
```

```
gcloud beta container binauthz policy import
```