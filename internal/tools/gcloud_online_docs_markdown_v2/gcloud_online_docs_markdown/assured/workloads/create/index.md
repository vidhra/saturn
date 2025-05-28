# gcloud assured workloads create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create)*

**NAME**

: **gcloud assured workloads create - create a new Assured Workloads environment**

**SYNOPSIS**

: **`gcloud assured workloads create` `[--billing-account](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--billing-account)`=`BILLING_ACCOUNT` `[--compliance-regime](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--compliance-regime)`=`COMPLIANCE_REGIME` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--display-name)`=`DISPLAY_NAME` `[--location](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--organization)`=`ORGANIZATION` [`[--enable-sovereign-controls](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--enable-sovereign-controls)`=`ENABLE_SOVEREIGN_CONTROLS`] [`[--external-identifier](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--external-identifier)`=`EXTERNAL_IDENTIFIER`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--next-rotation-time](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--next-rotation-time)`=`NEXT_ROTATION_TIME`] [`[--partner](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--partner)`=`PARTNER`] [`[--partner-permissions](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--partner-permissions)`=[`KEY`=`VALUE`,…]] [`[--partner-services-billing-account](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--partner-services-billing-account)`=`PARTNER_SERVICES_BILLING_ACCOUNT`] [`[--provisioned-resources-parent](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--provisioned-resources-parent)`=`PROVISIONED_RESOURCES_PARENT`] [`[--resource-settings](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--resource-settings)`=[`KEY`=`VALUE`,…]] [`[--rotation-period](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#--rotation-period)`=`ROTATION_PERIOD`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Assured Workloads environment

**EXAMPLES**

: The following example command creates a new Assured Workloads environment with
these properties:

- belonging to an organization with ID 123
- located in the `us-central1` region
- display name `Test-Workload`
- compliance regime `FEDRAMP_MODERATE`
- billing account `billingAccounts/456`
- first key rotation set for 10:15am on the December 30, 2020
- key rotation interval set for every 48 hours
- with the label: key = 'LabelKey1', value = 'LabelValue1'
- with the label: key = 'LabelKey2', value = 'LabelValue2'
- provisioned resources parent 'folders/789'
- with custom project id 'my-custom-id' for consumer project
- with external identifier for the workload of 'external-id'

```
gcloud assured workloads create --organization=123 --location=us-central1 --display-name=Test-Workload --compliance-regime=FEDRAMP_MODERATE --billing-account=billingAccounts/456 --next-rotation-time=2020-12-30T10:15:00.00Z --rotation-period=172800s --labels=LabelKey1=LabelValue1,LabelKey2=LabelValue2 --provisioned-resources-parent=folders/789 --resource-settings=consumer-project-id=my-custom-id --external-identifier=external-id
```

The following example command creates a new Partner Assured Workloads, with the
following properties:

- belonging to an organization with ID 123
- located in the `me-central2` region
- display name `Test-Workload`
- partner `CNTXT`
- partner services billing account `billingAccounts/789`
- billing account `billingAccounts/456`
- data logs viewer partner permission enabled
- first key rotation set for 10:15am on the December 30, 2020
- key rotation interval set for every 48 hours
- with the label: key = 'LabelKey1', value = 'LabelValue1'
- with the label: key = 'LabelKey2', value = 'LabelValue2'
- provisioned resources parent 'folders/789'
- with custom project id 'my-custom-id' for consumer project
- with external identifier for the workload of 'external-id'

```
gcloud assured workloads create --organization=123 --location=me-central2 --display-name=Test-Workload --compliance-regime=ASSURED_WORKLOADS_FOR_PARTNERS --partner=SOVEREIGN_CONTROLS_BY_CNTXT --partner-services-billing-account=billingAccounts/01BF3F-2C6DE5-30C607 --partner-permissions=data-logs-viewer=true --billing-account=billingAccounts/456 --next-rotation-time=2020-12-30T10:15:00.00Z --rotation-period=172800s --labels=LabelKey1=LabelValue1,LabelKey2=LabelValue2 --provisioned-resources-parent=folders/789 --resource-settings=consumer-project-id=my-custom-id --external-identifier=external-id
```

**REQUIRED FLAGS**

: **--billing-account**:
The billing account of the new Assured Workloads environment, for example,
billingAccounts/0000AA-AAA00A-A0A0A0

**--compliance-regime**:
The compliance regime of the new Assured Workloads environment.
`COMPLIANCE_REGIME` must be one of:
`assured-workloads-for-partners`,
`au-regions-and-us-support`, `ca-protected-b`,
`ca-regions-and-support`, `canada-controlled-goods`,
`cjis`, `eu-regions-and-support`,
`fedramp-high`, `fedramp-moderate`,
`healthcare-and-life-sciences-controls`,
`healthcare-and-life-sciences-controls-us-support`,
`hipaa`, `hitrust`, `il2`, `il4`,
`il5`, `irs-1075`, `isr-regions`,
`isr-regions-and-support`, `itar`,
`jp-regions-and-support`,
`ksa-regions-and-support-with-sovereignty-controls`,
`regional-controls`, `us-regional-access`.

**--display-name**:
The display name of the new Assured Workloads environment

**--location**:
The location of the new Assured Workloads environment. For a current list of
supported LOCATION values, see [Assured
Workloads locations](https://cloud.google.com/assured-workloads/docs/locations).

**--organization**:
The parent organization of the new Assured Workloads environment, provided as an
organization ID

**OPTIONAL FLAGS**

: **--enable-sovereign-controls**:
If true, enable sovereign controls for the new Assured Workloads environment,
currently only supported by EU_REGIONS_AND_SUPPORT

**--external-identifier**:
The external identifier of the new Assured Workloads environment

**--labels**:
The labels of the new Assured Workloads environment, for example,
LabelKey1=LabelValue1,LabelKey2=LabelValue2

**--next-rotation-time**:
The next rotation time of the KMS settings of new Assured Workloads environment,
for example, 2020-12-30T10:15:30.00Z

**--partner**:
The partner choice when creating a workload managed by local trusted partners.
`PARTNER` must be one of:
`local-controls-by-s3ns`, `sovereign-controls-by-cntxt`,
`sovereign-controls-by-cntxt-no-ekm`,
`sovereign-controls-by-psn`,
`sovereign-controls-by-sia-minsait`,
`sovereign-controls-by-t-systems`.

**--partner-permissions**:
The partner permissions for the partner regime, for example,
data-logs-viewer=true/false

**--partner-services-billing-account**:
Billing account necessary for purchasing services from Sovereign Partners. This
field is required for creating SIA/PSN/CNTXT partner workloads. The caller
should have 'billing.resourceAssociations.create' IAM permission on this
billing-account. The format of this string is
billingAccounts/AAAAAA-BBBBBB-CCCCCC

**--provisioned-resources-parent**:
The parent of the provisioned projects, for example, folders/{FOLDER_ID}

**--resource-settings**:
A comma-separated, key=value map of custom resource settings such as custom
project ids, for example: consumer-project-id={CONSUMER_PROJECT_ID} Note:
Currently only consumer-project-id, consumer-project-name,
encryption-keys-project-id, encryption-keys-project-name and keyring-id are
supported. The encryption-keys-project-id, encryption-keys-project-name and
keyring-id settings can be specified only if KMS settings are provided

**--rotation-period**:
The rotation period of the KMS settings of the new Assured Workloads
environment, for example, 172800s

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
gcloud alpha assured workloads create
```

```
gcloud beta assured workloads create
```