# gcloud compute target-instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update)*

**NAME**

: **gcloud compute target-instances update - update a Compute Engine target instance**

**SYNOPSIS**

: **`gcloud compute target-instances update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update#NAME)` [`[--security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update#--security-policy)`=`SECURITY_POLICY`] [`[--security-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update#--security-policy-region)`=`SECURITY_POLICY_REGION`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-instances update` updates a Compute Engine
target instance.

**EXAMPLES**

: To update the security policy run this:

```
gcloud compute target-instances update TARGET_INSTANCE --security-policy='my-policy'
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target instance to update.

**FLAGS**

: **--security-policy**:
The security policy that will be set for this target instance. To remove the
policy from this target instance set the policy to an empty string.

**--security-policy-region**:
Region of the security policy to operate on. Overrides the default
`compute/region` property value for this command invocation.

**--zone**:
Zone of the target instance to update. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

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
gcloud alpha compute target-instances update
```

```
gcloud beta compute target-instances update
```