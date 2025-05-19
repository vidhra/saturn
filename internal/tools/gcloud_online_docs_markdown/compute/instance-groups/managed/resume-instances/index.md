# gcloud compute instance-groups managed resume-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances)*

**NAME**

: **gcloud compute instance-groups managed resume-instances - resume the suspended instances in a managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed resume-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances#INSTANCE)`,…] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed resume-instances` resumes one
or more instances from a managed instance group, thereby increasing the
targetSize and reducing the targetSuspendedSize of the group.
The command returns the operation status per instance, which might be
``FAIL``,
``SUCCESS``, or
``MEMBER_NOT_FOUND``.
``MEMBER_NOT_FOUND`` is returned only for
regional groups when the gcloud command-line tool wasn't able to resolve the
zone from the instance name.

**EXAMPLES**

: To resume an instance from a managed instance group in the us-central1-a zone,
run:

```
gcloud compute instance-groups managed resume-instances example-managed-instance-group --zone=us-central1-a --instances=example-instance
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--instances**:
Names of instances to resume.

**OPTIONAL FLAGS**

: **--region**

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
gcloud alpha compute instance-groups managed resume-instances
```

```
gcloud beta compute instance-groups managed resume-instances
```