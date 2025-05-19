# gcloud compute network-attachments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update)*

**NAME**

: **gcloud compute network-attachments update - update a Google Compute Engine network attachment**

**SYNOPSIS**

: **`gcloud compute network-attachments update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#--description)`=`DESCRIPTION`] [`[--producer-accept-list](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#--producer-accept-list)`=[`ACCEPT_LIST`,…]] [`[--producer-reject-list](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#--producer-reject-list)`=[`REJECT_LIST`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#--region)`=`REGION`] [`[--subnets](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#--subnets)`=`SUBNETS`,[`[SUBNETS](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#SUBNETS)`,…]] [`[--subnets-region](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#--subnets-region)`=`SUBNETS_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-attachments update` is used to update network
attachments. You can update the following fields: description, subnets,
producer-accept-list and producer-reject-list. If you update the
producer-accept-list or producer-reject-list, the full new list should be
specified.

**EXAMPLES**

: To update all the parameters with the new list, run:

```
gcloud compute network-attachments update NETWORK_ATTACHMENT_NAME --region=us-central1 --subnets=MY_SUBNET2 --description='default network attachment' --producer-accept-list=PROJECT5,PROJECT6 --producer-reject-list=PROJECT7,PROJECT8
```

To update a network attachment to change only the subnet to MY_SUBNET3, run:

```
gcloud compute network-attachments update NETWORK_ATTACHMENT_NAME --region=us-central1 --subnets=MY_SUBNET3
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network attachment to update.

**FLAGS**

: **--description**:
An optional, textual description for the network attachment.

**--producer-accept-list**:
Projects that are allowed to connect to this network attachment.

**--producer-reject-list**:
Projects that are not allowed to connect to this network attachment.

**--region**:
Region of the network attachment to update. If not specified, you might be
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

**--subnets**:
The subnetworks provided by the consumer for the producers

**--subnets-region**:
Region of the subnetworks to operate on. Overrides the default
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
gcloud alpha compute network-attachments update
```

```
gcloud beta compute network-attachments update
```