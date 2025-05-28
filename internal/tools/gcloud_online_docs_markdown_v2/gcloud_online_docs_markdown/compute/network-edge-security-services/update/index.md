# gcloud compute network-edge-security-services update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update)*

**NAME**

: **gcloud compute network-edge-security-services update - update a network edge security service**

**SYNOPSIS**

: **`gcloud compute network-edge-security-services update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update#--description)`=`DESCRIPTION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update#--region)`=`REGION`] [`[--security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update#--security-policy)`=`SECURITY_POLICY`] [`[--security-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update#--security-policy-region)`=`SECURITY_POLICY_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-edge-security-services update` is used to
update network edge security services.

**EXAMPLES**

: To attach a new security policy 'my-policy' to a network edge security service
with the name 'my-service' in region 'us-central1', run:

```
gcloud compute network-edge-security-services update my-service --security-policy=my-policy --region=us-central1
```

To remove the security policy attached to a network edge security service with
the name 'my-service' in region 'us-central1', run:

```
gcloud compute network-edge-security-services update my-service --security-policy="" --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network edge security service to update.

**FLAGS**

: **--description**:
An optional, textual description for the network edge security service.

**--region**:
Region of the network edge security service to update. Overrides the default
`compute/region` property value for this command invocation.

**--security-policy**:
The security policy that will be set for this network edge security service. To
remove the policy from this network edge security service set the policy to an
empty string.

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
gcloud alpha compute network-edge-security-services update
```

```
gcloud beta compute network-edge-security-services update
```