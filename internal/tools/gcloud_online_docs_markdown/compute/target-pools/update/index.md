# gcloud compute target-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update)*

**NAME**

: **gcloud compute target-pools update - update a Compute Engine target pool**

**SYNOPSIS**

: **`gcloud compute target-pools update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update#--region)`=`REGION`] [`[--security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update#--security-policy)`=`SECURITY_POLICY`] [`[--security-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update#--security-policy-region)`=`SECURITY_POLICY_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-pools update` updates a Compute Engine target
pool.

**EXAMPLES**

: To update the security policy run this:

```
gcloud compute target-pools update TARGET_POOL --security-policy='my-policy'
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the target pool.

**FLAGS**

: **--region**:
Region of the target pool to update. If not specified, you might be prompted to
select a region (interactive mode only).
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

**--security-policy**:
The security policy that will be set for this target pool. To remove the policy
from this target pool set the policy to an empty string.

**--security-policy-region**:
Region of the security policy to operate on. Overrides the default
`compute/region` property value for this command invocation.

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
gcloud alpha compute target-pools update
```

```
gcloud beta compute target-pools update
```