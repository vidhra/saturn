# gcloud deploy deploy-policies export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/export](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/export)*

**NAME**

: **gcloud deploy deploy-policies export - returns the .yaml definition of the specified deploy policy**

**SYNOPSIS**

: **`gcloud deploy deploy-policies export` (`[DEPLOY_POLICY](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/export#DEPLOY_POLICY)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/export#--region)`=`REGION`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/export#--destination)`=`DESTINATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The exported yaml definition can be applied by `deploy apply`
command.

**EXAMPLES**

: To return the .yaml definition of the deploy policy `test-policy`, in
region `us-central1`, run:

```
gcloud deploy deploy-policies export test-policy --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Deploy policy resource - The name of the Deploy Policy. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `deploy_policy` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DEPLOY_POLICY`**:
ID of the deploy policy or fully qualified identifier for the deploy policy.
To set the `deploy_policy` attribute:

- provide the argument `deploy_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the deploy policy. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `deploy_policy` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output.

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
gcloud alpha deploy deploy-policies export
```

```
gcloud beta deploy deploy-policies export
```