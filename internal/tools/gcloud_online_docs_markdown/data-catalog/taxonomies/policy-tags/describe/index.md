# gcloud data-catalog taxonomies policy-tags describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/describe](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/describe)*

**NAME**

: **gcloud data-catalog taxonomies policy-tags describe - describe a Policy Tag Manager Policy tag**

**SYNOPSIS**

: **`gcloud data-catalog taxonomies policy-tags describe` (`[POLICY_TAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/describe#POLICY_TAG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/describe#--location)`=`LOCATION` `[--taxonomy](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/describe#--taxonomy)`=`TAXONOMY`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Policy Tag Manager Policy tag.

**EXAMPLES**

: To describe the Policy Tag 'POLICY_TAG' in the taxonomy 'TAXONOMY', run:

```
gcloud data-catalog taxonomies policy-tags describe POLICY_TAG --taxonomy='TAXONOMY' --location='LOCATION'
```

**POSITIONAL ARGUMENTS**

: **Policy tag resource - Policy tag to describe. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `policy_tag` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`POLICY_TAG`**:
ID of the policy tag or fully qualified identifier for the policy tag.
To set the `policy_tag` attribute:

- provide the argument `policy_tag` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the policy tag.
To set the `location` attribute:

- provide the argument `policy_tag` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--taxonomy**:
Taxonomy of the policy tag.
To set the `taxonomy` attribute:

- provide the argument `policy_tag` on the command line with a fully
specified name;
- provide the argument `--taxonomy` on the command line.**

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

: This command uses the `datacatalog/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/data-catalog/docs/](https://cloud.google.com/data-catalog/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha data-catalog taxonomies policy-tags describe
```

```
gcloud beta data-catalog taxonomies policy-tags describe
```