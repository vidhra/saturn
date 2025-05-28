# gcloud service-directory services set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/service-directory/services/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/set-iam-policy)*

**NAME**

: **gcloud service-directory services set-iam-policy - sets IAM policy for a service**

**SYNOPSIS**

: **`gcloud service-directory services set-iam-policy` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/set-iam-policy#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/set-iam-policy#--location)`=`LOCATION` `[--namespace](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/set-iam-policy#--namespace)`=`NAMESPACE`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets IAM policy for a service.

**EXAMPLES**

: To set an IAM policy to a Service Directory service, run:

```
gcloud service-directory services set-iam-policy my-service --namespace=my-namespace --location=us-east1 policy.json
```

**POSITIONAL ARGUMENTS**

: **Service resource - The Service Directory service to add IAM policy binding to.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The name of the region for the service.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--namespace**:
The name of the namespace for the service.
To set the `namespace` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--namespace` on the command line.**

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

**NOTES**

: These variants are also available:

```
gcloud alpha service-directory services set-iam-policy
```

```
gcloud beta service-directory services set-iam-policy
```