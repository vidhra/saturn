# gcloud compute resource-policies create group-placement  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement)*

**NAME**

: **gcloud compute resource-policies create group-placement - create a Compute Engine group placement resource policy**

**SYNOPSIS**

: **`gcloud compute resource-policies create group-placement` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement#NAME)` [`[--availability-domain-count](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement#--availability-domain-count)`=`AVAILABILITY_DOMAIN_COUNT`] [`[--collocation](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement#--collocation)`=`COLLOCATION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement#--description)`=`DESCRIPTION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement#--region)`=`REGION`] [`[--vm-count](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement#--vm-count)`=`VM_COUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Compute Engine Group Placement Resource Policy.

**EXAMPLES**

: To create a Compute Engine group placement policy with two availability domains,
run:
```
gcloud compute resource-policies create group-placement my-resource-policy --region=REGION --availability-domain-count=2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the resource policy to operate on.

**FLAGS**

: **--availability-domain-count**:
Number of availability domain in the group placement policy.

**--collocation**:
Collocation specifies whether to place VMs inside the sameavailability domain on
the same low-latency network. `COLLOCATION` must be one
of:

**`collocated`**:
Low network latency between more VMs placed on the same availability domain.

**`unspecified-collocation`**:
Unspecified network latency between VMs placed on the same availability domain.
This is the default behavior.

**--description**:
An optional, textual description for the backend.

**--region**:
Region of the resource policy to operate on. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--vm-count**:
Number of instances targeted by the group placement policy. Google does not
recommend that you use this flag unless you use a compact policy and you want
your policy to work only if it contains this exact number of VMs.

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
gcloud alpha compute resource-policies create group-placement
```

```
gcloud beta compute resource-policies create group-placement
```