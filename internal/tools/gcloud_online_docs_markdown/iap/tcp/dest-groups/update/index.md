# gcloud iap tcp dest-groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update)*

**NAME**

: **gcloud iap tcp dest-groups update - update the IAP TCP Destination Group resource**

**SYNOPSIS**

: **`gcloud iap tcp dest-groups update` `[GROUP_NAME](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update#GROUP_NAME)` `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update#--region)`=`REGION` (`[--fqdn-list](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update#--fqdn-list)`=`FQDN_LIST` `[--ip-range-list](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update#--ip-range-list)`=`IP_RANGE_LIST`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the IAP TCP Destination Group resource.

**EXAMPLES**

: To update a DestGroup with name ``GROUP_NAME``,
in region ``REGION`` with ip ranges
``CIDR1``,
``CIDR2`` in the current project run:

```
gcloud iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --ip-range-list=CIDR1,CIDR2
```

To update a DestGroup with name ``GROUP_NAME``,
in region ``REGION`` with fqdns
``FQDN1``,
``FQDN2`` in the current project run:

```
gcloud iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --fqdn-list=FQDN1,FQDN2
```

To update a DestGroup with name ``GROUP_NAME``,
in region ``REGION`` with fqdns
``FQDN1``,
``FQDN2`` and ip ranges
``CIDR1``,
``CIDR2`` in the project
``PROJECT_ID`` run:

```
gcloud iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --fqdn-list=FQDN1,FQDN2 --ip-range-list=CIDR1,CIDR2 --project=PROJECT_ID
```

To clear the fqdn list in a DestGroup with name
``GROUP_NAME``, in region
``REGION`` in the current project run:

```
gcloud iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --fqdn-list=""
```

To clear the ip range list in a DestGroup with name
``GROUP_NAME``, in region
``REGION`` in the current project run:

```
gcloud iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --ip-range-list=""
```

**POSITIONAL ARGUMENTS**

: **`GROUP_NAME`**:
Name of the Destination Group.

**REQUIRED FLAGS**

: **--region**:
Region of the Destination Group.

**--fqdn-list**

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
gcloud alpha iap tcp dest-groups update
```

```
gcloud beta iap tcp dest-groups update
```