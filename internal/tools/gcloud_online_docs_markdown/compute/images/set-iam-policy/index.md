# gcloud compute images set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/images/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/images/set-iam-policy)*

**NAME**

: **gcloud compute images set-iam-policy - set the IAM policy for a Compute Engine image**

**SYNOPSIS**

: **`gcloud compute images set-iam-policy` `[IMAGE](https://cloud.google.com/sdk/gcloud/reference/compute/images/set-iam-policy#IMAGE)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/compute/images/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/images/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for the given image as defined in a JSON or YAML file.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
'policy.json' and set it for the image `my-image`:

```
gcloud compute images set-iam-policy my-image policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **Image resource - The image to set IAM policy for. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `image` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`IMAGE`**:
ID of the image or fully qualified identifier for the image.
To set the `image` attribute:

- provide the argument `image` on the command line.**

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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

: This command uses the `compute/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute images set-iam-policy
```

```
gcloud beta compute images set-iam-policy
```