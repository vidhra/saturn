# gcloud compute network-attachments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create)*

**NAME**

: **gcloud compute network-attachments create - create a Google Compute Engine network attachment**

**SYNOPSIS**

: **`gcloud compute network-attachments create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#NAME)` `[--subnets](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#--subnets)`=`SUBNETS`,[`[SUBNETS](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#SUBNETS)`,…] [`[--connection-preference](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#--connection-preference)`=`CONNECTION_PREFERENCE`; default=`"ACCEPT_AUTOMATIC"`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#--description)`=`DESCRIPTION`] [`[--producer-accept-list](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#--producer-accept-list)`=[`ACCEPT_LIST`,…]] [`[--producer-reject-list](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#--producer-reject-list)`=[`REJECT_LIST`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#--region)`=`REGION`] [`[--subnets-region](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#--subnets-region)`=`SUBNETS_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-attachments create` is used to create network
attachments. A service consumer creates network attachments and makes it
available to producers. Service producers then use a multi-NIC VM to form a
bi-directional, non-NAT'd communication channel.

**EXAMPLES**

: ```
gcloud compute network-attachments create NETWORK_ATTACHMENT_NAME --region=us-central1 --subnets=MY_SUBNET --connection-preference=ACCEPT_MANUAL --producer-accept-list=PROJECT1,PROJECT2 --producer-reject-list=PROJECT3,PROJECT4
```

To create a network attachment with a textual description, run:

```
gcloud compute network-attachments create NETWORK_ATTACHMENT_NAME --region=us-central1 --subnets=MY_SUBNET --connection-preference=ACCEPT_MANUAL --producer-accept-list=PROJECT1,PROJECT2 --producer-reject-list=PROJECT3,PROJECT4 --description='default network attachment'
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network attachment to create.

**REQUIRED FLAGS**

: **--subnets**:
The subnetworks provided by the consumer for the producers

**OPTIONAL FLAGS**

: **--connection-preference**:
The connection preference of network attachment. The value can be set to
ACCEPT_AUTOMATIC or ACCEPT_MANUAL. An ACCEPT_AUTOMATIC network attachment is one
that always accepts the connection from producer NIC. An ACCEPT_MANUAL network
attachment is one that requires an explicit addition of the producer project id
or project number to the producer accept list.
`CONNECTION_PREFERENCE` must be one of:
`ACCEPT_AUTOMATIC`, `ACCEPT_MANUAL`.

**--description**:
An optional, textual description for the network attachment.

**--producer-accept-list**:
Projects that are allowed to connect to this network attachment.

**--producer-reject-list**:
Projects that are not allowed to connect to this network attachment.

**--region**:
Region of the network attachment to create. If not specified, you might be
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
gcloud alpha compute network-attachments create
```

```
gcloud beta compute network-attachments create
```