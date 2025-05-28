# gcloud tasks queues set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/queues/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/set-iam-policy)*

**NAME**

: **gcloud tasks queues set-iam-policy - set the IAM policy for a queue**

**SYNOPSIS**

: **`gcloud tasks queues set-iam-policy` (`[QUEUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/set-iam-policy#QUEUE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/set-iam-policy#--location)`=`LOCATION`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command replaces the existing IAM policy for a queue, given a queue and a
file encoded in JSON or YAML that contains the IAM policy. If the given policy
file specifies an "etag" value, then the replacement will succeed only if the
policy already in place matches that etag. (An etag obtained via
`get-iam-policy` will prevent the replacement if the policy for the
queue has been subsequently updated.) A policy file that does not contain an
etag value will replace any existing policy for the queue.

**EXAMPLES**

: To set the IAM policy for a queue:

```
gcloud tasks queues set-iam-policy my-queue policy-file.json
```

**POSITIONAL ARGUMENTS**

: **Queue resource - The queue for which to set the IAM policy. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `queue` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`QUEUE`**:
ID of the queue or fully qualified identifier for the queue.
To set the `queue` attribute:

- provide the argument `queue` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `queue` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `cloudtasks/v2` API. The full documentation for
this API can be found at: [https://cloud.google.com/tasks/](https://cloud.google.com/tasks/)

**NOTES**

: These variants are also available:

```
gcloud alpha tasks queues set-iam-policy
```

```
gcloud beta tasks queues set-iam-policy
```