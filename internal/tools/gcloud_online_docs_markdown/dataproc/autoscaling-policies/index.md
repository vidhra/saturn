# gcloud dataproc autoscaling-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies)*

**NAME**

: **gcloud dataproc autoscaling-policies - create and manage Dataproc autoscaling policies**

**SYNOPSIS**

: **`gcloud dataproc autoscaling-policies` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and manage Dataproc autoscaling policies.

**EXAMPLES**

: To see the list of all autoscaling policies, run:

```
gcloud dataproc autoscaling-policies list
```

To view the details of an autoscaling policy, run:

```
gcloud dataproc autoscaling-policies describe my_policy
```

To view just the non-output only fields of an autoscaling policy, run:

```
gcloud dataproc autoscaling-policies export my_policy --destination policy-file.yaml
```

To create or update an autoscaling policy, run:

```
gcloud dataproc autoscaling-policies import my_policy --source policy-file.yaml
```

To delete an autoscaling policy, run:

```
gcloud dataproc autoscaling-policies delete my_policy
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/delete)`**:
Delete an autoscaling policy.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/describe)`**:
Describe an autoscaling policy.

**`[export](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/export)`**:
Export an autoscaling policy.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/get-iam-policy)`**:
Get IAM policy for an autoscaling policy.

**`[import](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/import)`**:
Import an autoscaling policy.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/list)`**:
List autoscaling policies.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/set-iam-policy)`**:
Set IAM policy for an autoscaling policy.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc autoscaling-policies
```

```
gcloud beta dataproc autoscaling-policies
```